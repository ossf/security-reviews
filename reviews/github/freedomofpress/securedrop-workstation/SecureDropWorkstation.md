---
Publication-State: Active
Access: Public
Reviewers:
  Organization: Trail of Bits
  Associated-With-Project: False
  Compensation-Source: External
Domain: Security
Methodology:
- External-Review
Issues-Identified: Severe
Package-URL(s):
- pkg:github.com/freedomofpress/securedrop-workstation
Review-Date: 2020-12-18
Scope: Implementation (Full)
Schema-Version: 1.0
SPDX-License-Identifier: CC-BY-4.0
---

### Summary

The Freedom of Press Foundation engaged Trail of Bits to review the security of the SecureDrop Workstation. Trail of Bits conducted this assessment over the course of 6 person-weeks with 2 engineers assessing SecureDrop Workstation 0.5.0. SecureDrop is an open-source whistleblower submission system maintained by Freedom of the Press Foundation, a non-profit organization based in the United States. Over 75 news outlets worldwide use the system to communicate with sources.

### Details

Assessment of the SecureDrop Workstation codebase resulted in 26 findings ranging from informational to high severity. Notable, the high severity finding details case where a malicious SecureDrop server could create files in arbitrary paths in the sd-app VM, which may allow for code execution.

### Methodology

No methodology was provided.

### External References

Report: https://github.com/trailofbits/publications/blob/master/reviews/SecureDropWorkstation.pdf

### Disclaimer

All security reviews are conducted on a "best-effort" basis against a software
component at a point in time. We make no guarantee as to the quality or completeness
of any review. If you believe any content is inaccurate, we encourage you to open
an issue or submit a pull request with a correction or improvement.

### License

This text is released under at least the
[Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt).
Externally-referenced content may be licensed differently.
