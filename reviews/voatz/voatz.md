---
Publication-State: Active
Access: Public
Reviewers:
  Organization: Trail of Bits
  Associated-With-Project: False
  Compensation-Source: External
Domain: Security
Methodology:
- Static-Analysis
- Code-Review
- External-Review
Issues-Identified: Severe
Package-URL(s):
- Voatz Core Server
- Voatz Android Client
- Voatz iOS client
- Voatz Administrative Web Interface
Review-Date: 2020-03-12
Scope: Implementation (Full)
Schema-Version: 1.0
SPDX-License-Identifier: CC-BY-4.0
---

### Summary

Tusk Philanthropies and Voatz engaged Trail of Bits to review the security of the Voatz mobile voting platform. Trail of Bits conducted this assessment over the course of twelve (12) person-weeks with five (5) engineers working from commit hash 3443f4a of the Voatz Core Server repository, commit hash 07d1adb of the Voatz Android Client, commit hash d8436c1 of the Voatz iOS client, and commit hash 69d7a8b of the Voatz Administrative Web Interface.

### Details

The assessment resulted in forty-eight (48) findings, of which a third are high severity, another quarter medium severity, and the remainder a combination of low, undetermined, and informational severity. The high-severity findings are related to:
* Cryptography, e.g., improper use of cryptographic algorithms, as well as ad hoc cryptographic protocols
* Data exposure, e.g., sensitive credentials available to Voatz developers and personally identifiable information that can be leaked to attackers, and 
* Data validation, e.g., a family of findings related to reliance on unvalidated data provided by the clients.

### Methodology

No methodology was provided.

### External References

Report - Security Review: https://github.com/trailofbits/publications/blob/master/reviews/voatz-securityreview.pdf
Report - Threat Model: https://github.com/trailofbits/publications/blob/master/reviews/voatz-threatmodel.pdf 

### Disclaimer

All security reviews are conducted on a "best-effort" basis against a software
component at a point in time. We make no guarantee as to the quality or completeness
of any review. If you believe any content is inaccurate, we encourage you to open
an issue or submit a pull request with a correction or improvement.

### License

This text is released under at least the
[Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt).
Externally-referenced content may be licensed differently.
