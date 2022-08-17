---
Publication-State: Active
Access: Public
Reviewers:
  Associated-With-Project: False
  Compensation-Source: External
Domain: Security
Methodology:
- Dynamic-Analysis
- Code-Review
- External-Review
- Fuzzing
Issues-Identified: Severe
Package-URL(s):
- pkg: github/cri-o/cri-o
Review-Date: 2022-06-13
Scope: Implementation (Full)
Schema-Version: 1.0
SPDX-License-Identifier: CC-BY-4.0
---

### Summary

Open Source Technology Improvement Fund is thrilled to report the results of a security audit of CRI-O. CRI-O is an open source software (OSS) project that is an implementation of the Kubernetes Container Runtime Interface. It can run any OCI-compatible container, providing an enormous number of applications and environments. 

The primary security finding of the work is a single high-severity issue. A few minor issues were found as well, however, the Audit Team’s view from completing this engagement is that CRI-O is a well-written project that has a high level of security assurance.

### Details

The high severity finding is a denial of service attack on a given cluster by way of resource exhaustion of nodes. The attack is performed by way of pod creation, which means any user that can create a pod can cause denial of service on the given node that is used for pod creation. The CVE for the this vulnerability is CVE-2022-1708 and Github advisory can be found here: https://github.com/cri-o/cri-o/security/advisories/GHSA-fcm2-6c3h-pg6j

Interestingly, the denial of service attack also occurred in other container runtime interface implementations, most notably Containerd. Specifically, the exact same attack that exhausts memory in CRI-O can be used to exhaust memory of Containerd. The CVE for this issue in containerd is CVE-2022-31030 and the Github security advisory can be found here: https://github.com/containerd/containerd/security/advisories/GHSA-5ffw-gxpp-mxpf 

Furthermore, an extensive fuzzing suite targeting the CRI-O infrastructure was integrated as a result of this engagement, providing long-lasting improvements to the security posture of the project.

### Methodology

OSTIF undergoes an intensive scoping and RfP process to find the best-suited teams and individuals capable of performing high quality audit reviews.

### External References

Full synopsis and access to the published audit report can be found here: https://ostif.org/our-audit-of-cri-o-is-complete-high-severity-issues-found-and-fixed/

### Disclaimer

All security reviews are conducted on a "best-effort" basis against a software
component at a point in time. We make no guarantee as to the quality or completeness
of any review. If you believe any content is inaccurate, we encourage you to open
an issue or submit a pull request with a correction or improvement.

### License

This text is released under at least the
[Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt).
Externally-referenced content may be licensed differently.
