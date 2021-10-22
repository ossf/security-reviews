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
- pkg:github.com/westerndigitalcorporation/sweet-b
Review-Date: 2020-01-24
Scope: Implementation (Partial)
Schema-Version: 1.0
SPDX-License-Identifier: CC-BY-4.0
---

### Summary

From January 13 through January 24, 2020, Trail of Bits reviewed the security of Sweet B, a library that provides elliptic curve operations over 256-bit prime fields and a set of supporting hash-based primitives. Trail of Bits conducted this assessment over the course of four person-weeks with three engineers working from commit 02d41f4d of sweet-b.

### Details

Instruction trace analysis identified a potential misconfiguration that could produce functions that are not constant time (TOB-SB-001) and that undue trust was placed in the behavior of certain libc functions (TOB-SB-003). Finally, Trail of Bits completed manual review of the elliptic curve and prime-field implementations. Also, they identified potentially error-prone functions (TOB-SB-002) and issues related to the ECDSA API (TOB-SB-005).

### Methodology

No methodology was provided.

### External References

Report: https://github.com/trailofbits/publications/blob/master/reviews/SweetB.pdf

### Disclaimer

All security reviews are conducted on a "best-effort" basis against a software
component at a point in time. We make no guarantee as to the quality or completeness
of any review. If you believe any content is inaccurate, we encourage you to open
an issue or submit a pull request with a correction or improvement.

### License

This text is released under at least the
[Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt).
Externally-referenced content may be licensed differently.
