---
Publication-State: Active
Access: Public
Reviewers:
- Organization: Trail of Bits
  Associated-With-Project: false
  Compensation-Source: non-project
- Organization: TrustInSoft
  Associated-With-Project: false
  Compensation-Source: non-project  
Domain: Security
Methodology:
- External-Review
Issues-Identified: Non-Severe
Package-URLs:
- pkg:github/madler/zlib@1.2.8
Review-Date: 2016-09-30
Scope: Implementation/Partial
Schema-Version: 1.0
SPDX-License-Identifier: CC-BY-4.0
---

### Summary

Five security issues were identified (one medium-risk, four low-risk), all related to undefined behavior. All but one (low risk) issue was fixed before the report was published in September 2016. Users are encouraged to update to the latest stable version (1.2.11 at the time of this writing).

### Details

This assessment resulted in five findings, four of which have been fixed and are described in detail within the [report](https://github.com/trailofbits/publications/blob/master/reviews/zlib.pdf).

The remaining issue, which was not identified as fixed in the report, has to do with accessing a character buffer using a pointer to an unsigned int. This violated strict aliasing rules and could cause undefined behavior; however, when tested in 2016, compilers produced correct code for the construction. There are further recommendations on potential fixes in the report.

### Methodology

Trail of Bits states that they used an automated vulnerability tool ("CRS") developed for the DARPA Cyber Grand Challenge, augmented by a verification toolkit created by TrustInSoft (TIS-Interpreter) and human review. The testing focused on typical usage scenarios (compression, decompression, Gzip) with emphasis on memory safety and undefined behavior.

### External References

* [Zlib Automated Security Assessment](https://github.com/trailofbits/publications/blob/master/reviews/zlib.pdf)
* [Zlib Repository](https://github.com/madler/zlib)

### Disclaimer

All security reviews are conducted on a "best-effort" basis against a software
component at a point in time. We make no guarantee as to the quality or completeness
of any review. If you believe any content is inaccurate, we encourage you to open
an issue or submit a pull request with a correction or improvement.

### License

This text is released under at least the
[Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt).
Externally-referenced content may be licensed differently.
