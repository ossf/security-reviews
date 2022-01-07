---
Publication-State: Active
Access: Public
Reviewers:
- Organization: AdaLogics, Open Source Technology Improvement Fund
  Associated-With-Project: False
  Compensation-Source: Non-Project
Domain: Security
Methodology:
- Dynamic-Analysis
- Code-Review
- External-Review
- Fuzzing
Issues-Identified: Severe
Package-URLs:
- pkg:github/fluxcd/flux2
Review-Date: 2021-09-01
Scope: Implementation (Full)
Schema-Version: 1.0
SPDX-License-Identifier: CC-BY-4.0
---

### Summary

The primary aim was to assess Flux’s fundamental security posture and to identify next steps in its security story. The audit was commissioned by the CNCF, and facilitated by OSTIF (the Open Source Technology Improvement Fund). ADA Logics was quickly brought into the picture, and spent a month on the audit.

### Details

First CVE in Flux

Let’s start with what will likely interest you as a Flux user. The engagement uncovered a privilege escalation vulnerability in Flux that could enable users to gain cluster admin privileges. The issue has been fixed and is assigned CVE 2021-41254, and the full disclosure advisory is available at the following link::

CVE-2021-41254: Privilege escalation to cluster admin on multi-tenant Flux.

Description:


Users that can create Kubernetes Secrets, Service Accounts and Flux Kustomization objects, could execute commands inside the kustomize-controller container by embedding a shell script in a Kubernetes Secret. This can be used to run kubectl commands under the Service Account of kustomize-controller, thus allowing an authenticated Kubernetes user to gain cluster admin privileges.

Impact: 

Multi-tenant environments where non-admin users have permissions to create Flux Kustomization objects are affected by this issue.

Fix:

This vulnerability was fixed in kustomize-controller v0.15.0 (included in Flux v0.18.0) released on 2021-10-08. Starting with v0.15, the kustomize-controller no longer executes shell commands on the container OS and the kubectl binary has been removed from the container image.

### Methodology

Manual review, fuzzing integration

### External References

https://ostif.org/our-audit-of-flux2-is-complete/

### Disclaimer

All security reviews are conducted on a "best-effort" basis against a software
component at a point in time. We make no guarantee as to the quality or completeness
of any review. If you believe any content is inaccurate, we encourage you to open
an issue or submit a pull request with a correction or improvement.

### License

This text is released under at least the
[Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt).
Externally-referenced content may be licensed differently.
