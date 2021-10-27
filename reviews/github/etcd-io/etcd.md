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
- pkg:github.com/etcd-io/etcd
Review-Date: 2020-02-07
Scope: Non-Implementation
Schema-Version: 1.0
SPDX-License-Identifier: CC-BY-4.0
---

### Summary

From January 21 through January 31, 2020, the Linux Foundation engaged Trail of Bits to review the security of etcd. Trail of Bits conducted this assessment over the course of four person-weeks with four engineers working from release 3.4.3 of the etcd-io/etcd repository.

### Details

The assessment revealed a total of 17 findings ranging from high- to informational-severity. Overall, the etcd codebase represents a mature and heavily adopted product. However, there are many edge-cases not caught by the current test suite, and there are areas where the expected functionality of etcd does not match its implementation. These gaps can affect the security posture of the system since etcd gateway users may make inaccurate assumptions.

### Methodology

No methodology was provided.

### External References

Report: https://github.com/trailofbits/publications/blob/master/reviews/OPAGatekeeper.pdf

### Disclaimer

All security reviews are conducted on a "best-effort" basis against a software
component at a point in time. We make no guarantee as to the quality or completeness
of any review. If you believe any content is inaccurate, we encourage you to open
an issue or submit a pull request with a correction or improvement.

### License

This text is released under at least the
[Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt).
Externally-referenced content may be licensed differently.
