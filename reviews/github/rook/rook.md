---
Publication-State: Active
Access: Public
Reviewers:
-  Organization: Trail of Bits
   Associated-With-Project: False
   Compensation-Source: External
Domain: Security
Methodology:
- Static-Analysis
- Dynamic-Analysis
- Code-Review
- External-Review
- Fuzzing
Issues-Identified: Severe
Package-URLs:
- pkg:github.com/rook/rook/tree/release-1.1
Review-Date: 2019-12-19
Scope: Non-Implementation
Schema-Version: 1.0
SPDX-License-Identifier: CC-BY-4.0
---

### Summary

From December 2 through December 19, 2019, Rook worked with Trail of Bits to review the security of the storage orchestration system for Kubernetes, also named Rook. Trail of Bits conducted this assessment over the course of two person-weeks with two engineers working from the release-1.1 branch of the rook/rook repository.

### Details

The assessment resulted in 13 findings ranging from High to Low in severity.

### Methodology

The week-long assessment consisted of manual review, static analysis, and operational analysis with a focus on common Go mistakes, security-critical configuration, and protocol use.

### External References

Report: https://github.com/trailofbits/publications/blob/master/reviews/rook.pdf

### Disclaimer

All security reviews are conducted on a "best-effort" basis against a software
component at a point in time. We make no guarantee as to the quality or completeness
of any review. If you believe any content is inaccurate, we encourage you to open
an issue or submit a pull request with a correction or improvement.

### License

This text is released under at least the
[Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt).
Externally-referenced content may be licensed differently.
