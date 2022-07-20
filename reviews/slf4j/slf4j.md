---
Publication-State: Active
Access: Public
Reviewers:
- Organization: Open Source Technology Improvement Fund
  Associated-With-Project: false
  Compensation-Source: External
Domain: Security
Methodology:
- External-Review
- Code-Review
Issues-Identified: Non-Severe
Package-URLs:
- pkg:github/qos-ch/slf4j
Review-Date: 2022-03-20
Scope: Implementation/Full
Schema-Version: 1.0
SPDX-License-Identifier: CC-BY-4.0
---

### Summary

Simple Logging Facade for Java, slf4j, is identified in the Harvard Census II results as one of the most widely-deployed logging frameworks. The security and supply chain review was facilitated by Open Source Technology Improvement Fund and carried out by Include Security.

### Details

The results of the security audit are three (1 Low Risk, 2 Informational) findings, a documented threat model, and a Supply Chain Security review against SLSA. As a result of this review, slf4j, logback, and reload4j (a new fork of log4j 1.x with security fixes) are now reproducible builds, which substantially increases the difficulty of a supply-chain attack.

All findings identified through this security audit have been fixed and validated. See below for the full report. 

### Methodology

A combination of manual code auditing, dynamic analysis, and
static analysis was used to perform the audit.


### External References

A link to the full report is available for free at: https://ostif.org/our-audit-of-slf4j-is-complete/

### Disclaimer

All security reviews are conducted on a "best-effort" basis against a software
component at a point in time. We make no guarantee as to the quality or completeness
of any review. If you believe any content is inaccurate, we encourage you to open
an issue or submit a pull request with a correction or improvement.

### License

This text is released under at least the
[Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt).
Externally-referenced content may be licensed differently.
