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
Issues-Identified: Severe
Package-URLs:
- pkg:github/kubeedge/kubeedge
Review-Date: 2022-05-01
Scope: Implementation/Full
Schema-Version: 1.0
SPDX-License-Identifier: CC-BY-4.0
---

### Summary

KubeEdge is built upon Kubernetes and extends native containerized application orchestration and device management to hosts at the Edge. An audit was facilitated by OSTIF and funded by CNCF. 

### Details

The result of this engagement is the finding and fixing of multiple medium severity issues, threat modeling, and integration to OSS Fuzz. 10 fuzzers in total were written, and these fuzzers were set up to run in the CI for pull requests. Several issues were found by the fuzzers, including 2 of the 8 CVEs.

### Methodology

A combination of manual code auditing, dynamic analysis using a custom fuzzing harness, and static analysis was used to perform the audit.


### External References

A link to the full report is available for free at:(https://ostif.org/our-audit-of-kubeedge-is-complete-multiple-security-issues-found-and-fixed/)

### Disclaimer

All security reviews are conducted on a "best-effort" basis against a software
component at a point in time. We make no guarantee as to the quality or completeness
of any review. If you believe any content is inaccurate, we encourage you to open
an issue or submit a pull request with a correction or improvement.

### License

This text is released under at least the
[Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt).
Externally-referenced content may be licensed differently.
