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
- Dynamic-Analysis
- Code-Review
- External-Review
Issues-Identified: Severe
Package-URL(s):
- pkg:github.com/helm/helm/tree/v3.3.0-rc.1
Review-Date: 2020-08-10
Scope: Implementation (Full)
Schema-Version: 1.0
SPDX-License-Identifier: CC-BY-4.0
---

### Summary

From July 27 through August 5, 2020, Trail of Bits reviewed the security of Helm and conducted this assessment over the course of three person-weeks with two engineers working from v3.3.0-rc.1 (c2dfaa) from the Helm repository.

### Details

The assessment revealed a total of 14 findings ranging from medium to informational severity. Overall, the Helm codebase maturity could be improved. In some areas, it does not perform the necessary data validation, and in others the implementation either does not match the expected functionality or is not fully documented. These gaps can affect the security posture of the system since Helm users may make incorrect assumptions.

### Methodology

No methodology was provided.

### External References

Report: https://github.com/trailofbits/publications/blob/master/reviews/Helm.pdf

### Disclaimer

All security reviews are conducted on a "best-effort" basis against a software
component at a point in time. We make no guarantee as to the quality or completeness
of any review. If you believe any content is inaccurate, we encourage you to open
an issue or submit a pull request with a correction or improvement.

### License

This text is released under at least the
[Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt).
Externally-referenced content may be licensed differently.
