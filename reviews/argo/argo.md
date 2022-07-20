---
Publication-State: Active
Access: Public
Reviewers:
- Organization: Open Source Technology Improvement Fund, Ada Logics
  Associated-With-Project: false
  Compensation-Source: External
Domain: Security
Methodology: 
- Code-Review
Issues-Identified: Severe
Package-URLs:
- pkg:github/argoproj/argoproj
Review-Date: 2022-04-19
Scope: Implementation/Partial
Schema-Version: 1.0
SPDX-License-Identifier: CC-BY-4.0

---

### Summary

The audit was facilitated by OSTIF and sponsored by CNCF and carried out by Ada Logics’ team of researchers. We found several high-severity CVEs which the Argo teams have worked hard to fix since mid May. With the release of the report, all CVEs have been fixed.

### Details

The research findings resulted in 26 security issues including 1 critical and 4 high severity bugs that were fixed. The most significant finding is an XSS injection in ArgoCD https://github.com/argoproj/argo-cd/security/advisories/GHSA-h4w9-6×78-8vrj that allows an attacker to execute javascript code in the UI, which could allow an attacker to take admin control of the kubernetes cluster.

Additionally, the Ada Logics team built 7 new fuzzers to integrate into the ossfuzz testing suite for Argo that focus on security relevant functions. The Argo team and community demonstrated a strong commitment to improving the project’s security posture. See the full report and Argo team’s synopsis below for detailed information.

### Conclusion

26 security issues including 1 critical and 4 high severity bugs that were fixed.


### Methodology

Ada Logics found 26 issues across ArgoCD, Argo Workflows and Argo Events

### External References

• [Full Report](https://ostif.org/our-audit-of-argo-is-complete-critical-and-high-severity-security-issues-found-and-fixed/)


### Disclaimer

All security reviews are conducted on a "best-effort" basis against a software
component at a point in time. We make no guarantee as to the quality or completeness
of any review. If you believe any content is inaccurate, we encourage you to open
an issue or submit a pull request with a correction or improvement.

### License

This text is released under at least the
[Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt).
Externally-referenced content may be licensed differently.
