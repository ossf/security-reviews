---
Publication-State: Active
Access: Public
Reviewers:
  Organization: Cloud Native Computing Foundation / Linux Foundation / Cure53
  Associated-With-Project: false
  Compensation-Source: External
Domain: Security
Methodology:
- External-Review
Issues-Identified: Non-Severe
Package-URLs:
- pkg:github/coredns/coredns@1.0.6
- pkg:github/miekg/dns@1.0.4
Review-Date: 2018-02-03
Scope: Implementation/Full
Schema-Version: 1.0
SPDX-License-Identifier: CC-BY-4.0
---

### Summary

Four vulnerabilities were detected, one critical and the rest minor. The critical vulnerability, DNS cache poisoning, can be used to inject harmful records into the server's cache. This issue was fixed in the CoreDNS 1.1.1 release. It is recommended to upgrade to this version.

### Details

The Cloud Native Computing Foundation asked Cure53 to conduct an in-depth security assessment of CoreDNS, which has since been made publicly available. This report was sponsored by the Linux Foundation and includes the scope, test coverage, identified vulnerabilities, and conclusions reached from the assessment, all of which are outlined in further detail in the [report](https://coredns.io/assets/DNS-01-report.pdf).

The analysis was conducted by a team of six targeting the CoreDNS DNS Server Software. A brief summary of each of the vulnerabilities detected are outlined below.

###### Vulnerability 1: DNS Cache Poisoning - Critical

In the cache plugin of CoreDNS, it is not checked whether the domain in a request matches the response. This allows an attacker to inject malicious records into the DNS server's cache, as each domain handled by CoreDNS uses a different cache. See the [report](https://coredns.io/assets/DNS-01-report.pdf) for more details, along with an example exploit.

###### Vulnerability 2: Overlong Domain Names Bypass Logging

While domain names are checked to ensure the maximum length of 253 characters is not exceeded, if a domain name is modified using the rewrite plugin to exceed this length, the result will produce undesired behavior by the DNS server and logs.

###### Vulnerability 3: Denial-of-Service via Endless Zone Transfer

Using the secondary plugin, CoreDNS can act as a secondary name server. In this case, another DNS server can continuously relay zone file information to the CoreDNS server, which can halt the application and prevent it from responding to other queries.

###### Vulnerability 4: Denial-of-Service through Large Queries

A malicious actor can spoof IP addresses and source ports, paired with additional queries that can disable the service from responding to other queries (CoreDNS does not crash, however). This attack vector is directed at the DNS protocol used by CoreDNS, not the application itself.

### Methodology

Cure53 used dynamic penetration testing and probed input locations for undesired behavior. A series of common attacks such as DoS/SYN-floods were attempted, with one of these common attacks detecting a vulnerability (poisoning the DNS cache). Other checks were run as well, including non-terminating and data starving zone transfers, but in the end CoreDNS handled almost all attacks appropriately, and only a few minor issues were detected. Lastly, some manual static analysis was used to check for common vulnerabilities such as command injection, but nothing major was found.

### External References

* [Full Report](https://coredns.io/assets/DNS-01-report.pdf)  
* GitHub Repositories:  
  *  [coredns/coredns](https://github.com/coredns/coredns)  
  * [miekg/dns]( https://github.com/miekg/dns)

### Disclaimer

All security reviews are conducted on a "best-effort" basis against a software
component at a point in time. We make no guarantee as to the quality or completeness
of any review. If you believe any content is inaccurate, we encourage you to open
an issue or submit a pull request with a correction or improvement.

### License

This text is released under at least the
[Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt).
Externally-referenced content may be licensed differently.
