---
Publication-State: Active
Access: Public
Reviewers:
  Organization: Cloud Native Computing Foundation, Cure53
  Associated-With-Project: false
  Compensation-Source: External
Domain: Security
Methodology:
- External-Review
Issues-Identified: Non-Severe
Package-URLs:
- pkg:github/coredns/coredns@1.0.6
Review-Date: 2018-02-03
Scope: Implementation/Full
Schema-Version: 1.0
SPDX-License-Identifier: CC-BY-4.0
---

### Summary

The Cloud Native Computing Foundation asked Cure53 to conduct an in-depth security assessment of CoreDNS, which has since been made publicly available. The report includes the scope, test coverage, identified vulnerabilities, and conclusions reached from the assessment, all of which are outlined in further detail in the [report](https://coredns.io/assets/DNS-01-report.pdf). Four vulnerabilities were detected, one critical and the rest minor. The critical vulnerability, DNS cache poisoning, can be used to inject harmful records into the server's cache. This issue was fixed in the CoreDNS 1.1.1 release. It is recommended to upgrade to this version.

### Details



### Methodology

Cure53 used dynamic penetration testing and probed input locations for undesired behavior. A series of common attacks such as DoS/SYN-floods were attempted, with one of these common attacks detecting a vulnerability (poisoning the DNS cache). Other checks were run as well, including non-terminating and data starving zone transfers, but in the end the software handled almost all attacks appropriately, and only very few minor issues were detected. Lastly, some manual static analysis was used to check for common vulnerabilities such as command injection, but nothing major was found.

### External References

• [Full Report](https://coredns.io/assets/DNS-01-report.pdf)
• [Repository](https://github.com/coredns/coredns)

### Disclaimer

All security reviews are conducted on a "best-effort" basis against a software
component at a point in time. We make no guarantee as to the quality or completeness
of any review. If you believe any content is inaccurate, we encourage you to open
an issue or submit a pull request with a correction or improvement.

### License

This text is released under at least the
[Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt).
Externally-referenced content may be licensed differently.
