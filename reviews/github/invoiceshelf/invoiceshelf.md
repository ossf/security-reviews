---
Publication-State: Active
Access: Public
Reviewers:
- Name: Santosh Kumar Puppala
  Email: santhoshkumar7794@gmail.com
  Associated-With-Project: false
  Compensation-Source: None
Domain: Security
Methodology:
- Code-Review
- Dynamic-Analysis
Issues-Identified: Severe
Package-URLs:
- pkg:github/InvoiceShelf/InvoiceShelf
Review-Date: 2026-08-09
Scope: Implementation/Partial
Schema-Version: 1.0
SPDX-License-Identifier: CC-BY-4.0

---

### Summary

InvoiceShelf is a self-hosted invoicing application (PHP/Laravel + Vue), a fork of Crater, that supports multiple companies in a single installation. This review covers the user-management area of its REST API at release v2.4.0, examined through source review and a live dynamic proof of concept.

The review identified one severe object-level authorization flaw, now tracked as CVE-2026-55610 (GHSA-vgx6-6cqr-m8qr, High, CVSS 8.7, CWE-639). In a multi-company installation, any user who is an Owner of one company could read and overwrite any user account belonging to any other company on the same installation. The endpoint resolves the target user by global primary key, and the authorizing policy verified only that the requester owned their own company — never that the target user belonged to that company. The result was cross-tenant disclosure of user records and full account takeover, including email and password overwrite and re-assignment of the victim into the attacker's company as a super administrator.

The issue affects versions `<= 2.4.0` and is fixed in `2.4.1`. Installations running a single company are not exposed to the cross-tenant impact; multi-company installations on affected versions should upgrade.

### Details

The affected route is `GET`/`PUT /api/v1/users/{user}`, declared at `routes/api.php:461` under the `auth:sanctum`, company, and Bouncer middleware stack. The controller methods `show(User $user)` and `update(UserRequest, User $user)` in `app/Http/Controllers/V1/Admin/Users/UsersController.php` rely on Laravel implicit route-model binding, which resolves the `{user}` parameter by its global primary key with no company scope applied — there is no `resolveRouteBinding` override, no global scope on the model, and no `RouteServiceProvider` constraint.

Authorization is delegated to `app/Policies/UserPolicy.php`, whose `view()` and `update()` methods both reduce to:

```php
if ($user->isOwner()) {
    return true;
}
```

`isOwner()` in `app/Models/User.php` evaluates only the requester's own header-selected company:

```php
Company::find(request()->header('company'))->owner_id == $this->id;
```

The target user's company is never compared against the requester's. `CompanyMiddleware` constrains the `company` header to one the requester actually belongs to, but it never constrains the `{user}` route parameter, so an Owner can address any user id in the installation.

The write path compounds the impact: `User::updateFromRequest()` persists `name`, `email`, and `password` from the request payload, then calls `$this->companies()->sync(...)` and `Bouncer::sync()->roles(...)`. Those calls are consumed by authentication and authorization, so the victim can be moved into the attacker's company with an elevated role rather than merely edited.

The same file demonstrates that tenant isolation was the intended design. The sibling `destroy()` path is scoped with `User::whereCompany(...)` and carries the in-code comment that a user from one company must not delete accounts belonging to another. The `view` and `update` paths simply omit that scope, which is what makes this a missing-check flaw rather than an intended capability.

A dynamic proof of concept confirmed the behavior on the shipped Docker image `invoiceshelf/invoiceshelf:2.4.0`. With two companies and a user belonging only to the second, the Owner of the first company issued `GET /api/v1/users/{id}` for that user and received `200` with the record, then issued `PUT` to overwrite the email and password and re-sync the user into the attacker's company as super administrator, also `200`. As a negative control, a non-owner member of the first company received `403` on the same `GET`, confirming that the route is access-controlled in general and that the defect is specifically the missing target-company check for Owners.

The maintainer's remediation adds the missing check in `UserPolicy`, verifying that the target user belongs to the requester's company after the owner check (mirroring the `destroy()` scoping), and shipped it in v2.4.1.

### Conclusion

The reviewed area contained one severe cross-tenant authorization defect, scoped to a single missing ownership check on one policy path, with a clear remediation that the maintainer applied promptly in the next patch release. The surrounding code shows deliberate tenant-isolation intent elsewhere, and the fix brings the affected paths in line with it. Operators running InvoiceShelf `<= 2.4.0` with more than one company on a single installation should treat this as high priority and upgrade to `2.4.1` or later; single-company deployments are not exposed to the cross-tenant impact. This review is partial in scope: it examined the user-management API paths related to the finding and does not constitute a full audit of the application.

### Methodology

Source review was performed against the code at release tag v2.4.0, tracing the route declaration, controller binding, policy, and model methods along the request path. A dynamic proof of concept was then run against the official `invoiceshelf/invoiceshelf:2.4.0` Docker image to confirm the behavior and to verify a negative control. The finding was reported to the maintainer under coordinated disclosure via GitHub private vulnerability reporting; the details above reflect the published advisory after the fix was released.

### External References

- [GHSA-vgx6-6cqr-m8qr](https://github.com/InvoiceShelf/InvoiceShelf/security/advisories/GHSA-vgx6-6cqr-m8qr)
- [CVE-2026-55610 (NVD)](https://nvd.nist.gov/vuln/detail/CVE-2026-55610)
- [InvoiceShelf repository](https://github.com/InvoiceShelf/InvoiceShelf)

### Disclaimer

All security reviews are conducted on a "best-effort" basis against a software
component at a point in time. We make no guarantee as to the quality or completeness
of any review. If you believe any content is inaccurate, we encourage you to open
an issue or submit a pull request with a correction or improvement.

### License

This text is released under at least the
[Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt).
Externally-referenced content may be licensed differently.
