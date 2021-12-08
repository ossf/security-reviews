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
- Code-Review
- External-Review
Issues-Identified: Non-Severe
Package-URLs:
- pkg:pkg:github.com/standardnotes/snjs
- pkg:github.com/standardnotes/SNCrypto
Review-Date: 2020-09-08
Scope: Implementation/Partial
Schema-Version: 1.0
SPDX-License-Identifier: CC-BY-4.0
---

### Summary

From March 2 through March 6, 2020, Standard Notes engaged Trail of Bits to review the security of SNJS and SNCrypto. Trail of Bits conducted this assessment for one person-week with two engineers working from commit b9d7b79 on branch 004 from the standardnotes/snjs repository, along with commit 0059a66 on branch 004 of the standardnotes/sncrypto repository.

### Details

The manual review of the codebase revealed four findings. Trail of Bits reported one medium-severity issue, TOB-SNOTES-001, related to insecure passwords. The remaining three, TOB-SNOTES-002–TOB-SNOTES-004, are informational findings related to values leaked to timing side-channels, and values not being cleared after they are no longer needed.

### Methodology

No methodology was provided.

### External References

Report: https://github.com/trailofbits/publications/blob/master/reviews/StandardNotes.pdf

### Disclaimer

All security reviews are conducted on a "best-effort" basis against a software
component at a point in time. We make no guarantee as to the quality or completeness
of any review. If you believe any content is inaccurate, we encourage you to open
an issue or submit a pull request with a correction or improvement.

### License

This text is released under at least the
[Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt).
Externally-referenced content may be licensed differently.
