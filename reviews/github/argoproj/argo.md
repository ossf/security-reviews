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
Issues-Identified: Severe
Package-URLs:
- pkg:github.com/argoproj/argo-cd
- pkg:github.com/argoproj/argo-events
- pkg:github.com/argoproj/argo-rollouts
- pkg:github.com/argoproj/argo-workflows
- pkg:github.com/argoproj/gitops-engine
- pkg:github.com/argoproj/pkg
Review-Date: 2021-03-12
Scope: Implementation/Full
Schema-Version: 1.0
SPDX-License-Identifier: CC-BY-4.0
---

### Summary

From March 1 to March 9, 2021, Trail of Bits conducted a code review of the Argo product suite, which includes Argo CD, Argo Workflows, Argo Rollouts, and Argo Events.

### Details

Manual review efforts included investigations into insufficient use of cryptography and data validation, improper handling or assignment of access controls, weak configurations, potential information disclosures, incorrect or dangerous use of auditing and logging, and resource exhaustion attacks. The primary targets of these manual review efforts included Argo CD and Argo Workflows. This review resulted in 23 findings ranging from undetermined to medium severity, as well as several untriaged concerns.
In addition to conducting a deeper review into the above mentioned classes of issues, Trail of Bits triaged remaining suspicions identified in the previous week. During the remainder of the audit, Trail of Bits placed increased emphasis on Argo Events and Argo Rollouts while generally reviewing concerns regarding insufficient use of authentication, file permissions, Kubernetes best practices, undefined behavior stemming from a lack of documentation or insufficient error handling, race conditions, and general data validation concerns. This resulted in 12 additional findings ranging from medium to informational severity.

### Methodology

No methodology was provided.

### External References

Report - Security Review: https://github.com/trailofbits/publications/blob/master/reviews/argo-securityreview.pdf
Report - Threat Model: https://github.com/trailofbits/publications/blob/master/reviews/argo-threatmodel.pdf

### Disclaimer

All security reviews are conducted on a "best-effort" basis against a software
component at a point in time. We make no guarantee as to the quality or completeness
of any review. If you believe any content is inaccurate, we encourage you to open
an issue or submit a pull request with a correction or improvement.

### License

This text is released under at least the
[Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt).
Externally-referenced content may be licensed differently.
