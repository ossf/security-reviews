---
Publication-State: Active
Access: Public
Reviewers:
- Name: Mario Heiderich
  Email: mario@cure53.de
  Organization: Cure53
  Associated-With-Project: False
  Compensation-Source: Non-Project
Domain: Security
Methodology:
- Static-Analysis
- Dynamic-Analysis
- Code-Review
- External-Review
Issues-Identified: Non-Severe
Package-URLs:
- pkg:cargo/rustls@0.16.0
- pkg:cargo/ring
- pkg:cargo/webpki
- pkg:cargo/sct.rs
- pkg:cargo/rustls-native-certs
Review-Date: 2020-06-15
Scope: Implementation/Full
Schema-Version: 1.0
SPDX-License-Identifier: CC-BY-4.0
---

### Summary

In May and June 2020, Cure53 completed a security audit of rustls (a TLS library written in Rust) along with some of its key dependencies such as ring and webpki.

### Details

There were two informational and two minor-severity findings. See the report for the full details.

This evaluation was funded by the Linux Foundation (LF) Cloud Native Computing Foundation (CNCF).

### Methodology

Audit split into two parts: rustls and key dependencies. The authors ran static tools, tests, and code robustness analysis; the latter was via human review of the source code.

### External References

https://github.com/rustls/rustls/blob/master/audit/TLS-01-report.pdf

https://jbp.io/2020/06/14/rustls-audit.html

### Disclaimer

All security reviews are conducted on a "best-effort" basis against a software
component at a point in time. We make no guarantee as to the quality or completeness
of any review. If you believe any content is inaccurate, we encourage you to open
an issue or submit a pull request with a correction or improvement.

### License

This text is released under at least the
[Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt).
Externally-referenced content may be licensed differently.
