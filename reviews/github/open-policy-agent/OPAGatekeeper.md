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
- pkg:github.com/open-policy-agent/gatekeeper
- pkg:github.com/open-policy-agent/opa
- pkg:github.com/open-policy-agent/frameworks/tree/master/constraint
Review-Date: 2020-03-10
Scope: Implementation (Full)
Schema-Version: 1.0
SPDX-License-Identifier: CC-BY-4.0
---

### Summary

From February 18 through February 21, 2020, Cloud Native Computing Foundation (CNCF) engaged Trail of Bits to review the security of Gatekeeper. Trail of Bits conducted this assessment over the course of two person-weeks with two engineers working from commit hash 98edc61 of the Gatekeeper repository.

Gatekeeper allows enforcement of CRD-based policies over Kubernetes objects through a Kubernetes validation hook. It uses Open Policy Agent (“OPA”), a policy engine for Cloud Native environments where policies are written in the Rego policy language. It also periodically audits the existing Kubernetes objects against the specified constraints to ensure all objects continue to hold under the specified policies.

### Details

The assessment of Gatekeeper revealed a total of 10 findings ranging from High to Undetermined severity. Most notably, finding TOB-OPAGK-005 details an insecure configuration that allows Gatekeeper validation checks to be bypassed (e.g., by performing a denial of service attack).

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
