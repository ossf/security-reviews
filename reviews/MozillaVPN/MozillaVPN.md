---
Publication-State: Active
Access: Public
Reviewers:
- Organization: Cure53
  Associated-With-Project: false
  Compensation-Source: External
Domain: Security
Methodology: 
- Code-Review
Issues-Identified: Non-Severe
Package-URLs:
- pkg:github/mozilla-mobile/mozilla-vpn-client
Review-Date: 2021-03-20
Scope: Implementation/Partial
Schema-Version: 1.0
SPDX-License-Identifier: CC-BY-4.0

---

### Summary

Article on review: https://blog.mozilla.org/en/mozilla/news/mozilla-vpn-completes-independent-security-audit-by-cure53/

Mozilla published an independent security audit of its Mozilla VPN, which provides encryption and device-level protection of your connection and information when you are on the Web, from Cure53, an unbiased cybersecurity firm based in Berlin with more than 15 years of running software testing and code auditing.

### Details

Here’s a summary of the items discovered within this security audit that were medium or higher severity:

FVP-02-014: Cross-site WebSocket hijacking (High)

Mozilla VPN client, when put in debug mode, exposes a WebSocket interface to localhost to trigger events and retrieve logs (most of the functional tests are written on top of this interface). As the WebSocket interface was used only in pre-release test builds, no customers were affected.  Cure53 has verified that this item has been properly fixed and the security risk no longer exists.

FVP-02-001: VPN leak via captive portal detection (Medium)

Mozilla VPN client allows sending unencrypted HTTP requests outside of the tunnel to specific IP addresses, if the captive portal detection mechanism has been activated through settings.  However, the captive portal detection algorithm requires a plain-text HTTP trusted endpoint to operate. Firefox, Chrome, the network manager of MacOS and many applications have a similar solution enabled by default. Mozilla VPN utilizes the Firefox endpoint.  Ultimately, we have accepted this finding as the user benefits of captive portal detection outweigh the security risk.

FVP-02-016: Auth code could be leaked by injecting port (Medium)

When a user wants to log into Mozilla VPN, the VPN client will make a request to https://vpn.mozilla.org/api/v2/vpn/login/windows to obtain an authorization URL. The endpoint takes a port parameter that will be reflected in a <img> element after the user signs into the web page. It was found that the port parameter could be of an arbitrary value. Further, it was possible to inject the @ sign, so that the request will go to an arbitrary host instead of localhost (the site’s strict Content Security Policy prevented such requests from being sent). We fixed this issue by improving the port number parsing in the REST API component. The fix includes several tests to prevent similar errors in the future.

### Conclusion

During the independent audit, there were two medium and one high severity issues that were discovered.


### Methodology

For optimal delineation of the scope, the work was split into five separate work packages
(WPs), mirroring a schema of having a dedicated WP for each app. The WP structure,
therefore, can be elaborate as follows:

• WP1: Security Tests & Code Audits against Mozilla VPN Qt5 App for macOS

• WP2: Security Tests & Code Audits against Mozilla VPN Qt5 App for Linux

• WP3: Security Tests & Code Audits against Mozilla VPN Qt5 App for Windows

• WP4: Security Tests & Code Audits against Mozilla VPN Qt5 App for iOS

• WP5: Security Tests & Code Audits against Mozilla VPN Qt5 App for Android

### External References

• [Full Report](https://blog.mozilla.org/security/files/2021/08/FVP-02-report.final_.pdf)  


### Disclaimer

All security reviews are conducted on a "best-effort" basis against a software
component at a point in time. We make no guarantee as to the quality or completeness
of any review. If you believe any content is inaccurate, we encourage you to open
an issue or submit a pull request with a correction or improvement.

### License

This text is released under at least the
[Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt).
Externally-referenced content may be licensed differently.

