---
Publication-State: Active
Access: Public
Reviewers:
- Organization: Microsoft (OSS Security Team)
  Associated-With-Project: false
  Compensation-Source: None
Domain: Security
Methodology:
- Static-Analysis
- Code-Review
- Web-Search
Package-URLs:
- pkg:nuget/redis-64@2.6.8.2
- pkg:nuget/redis-64@2.6.12.1
- pkg:nuget/redis-64@2.6.14
- pkg:nuget/redis-64@2.8.4
- pkg:nuget/redis-64@2.8.9
- pkg:nuget/redis-64@2.8.12
- pkg:nuget/redis-64@2.8.17
- pkg:nuget/redis-64@2.8.19
- pkg:nuget/redis-64@2.8.21
- pkg:nuget/redis-64@2.8.2101
- pkg:nuget/redis-64@2.8.2104
- pkg:nuget/redis-64@2.8.2400
- pkg:nuget/redis-64@2.8.2402
- pkg:nuget/redis-64@3.0.500
- pkg:nuget/redis-64@3.0.501
- pkg:nuget/redis-64@3.0.503
Issues-Identified: Severe
Review-Date: 2019-06-15
Scope: Implementation/Partial
Schema-Version: 1.0
SPDX-License-Identifier: CC-BY-4.0
---

### Summary

This package is based on a fork from the Redis 3.x branch, which contains
multiple vulnerabilities. It is also abandoned, and should not be used in
any capacity.

### Details

This package is based on a fork from the Redis 3.x branch, which contains
multiple vulnerabilities. It is also abandoned, and should not be used in
any capacity.

Specifically, the latest version of Redis-64 appears to be based on Redis 3.0.5,
released in October 2015, and has
[eight known CVEs](https://www.cvedetails.com/vulnerability-list/vendor_id-18560/product_id-47087/version_id-250998/Redislabs-Redis-3.0.5.html).

### Methodology

This review was conducted by the Microsoft Open Source Security Team using of automated
tools (including static analysis), custom tools, a targeted code review, and some
effort to identify already-known security defects.

### External References

* [nuget.org/packages/redis-64](https://www.nuget.org/packages/redis-64/)
* [CVE Listing for Redis](https://www.cvedetails.com/version-list/18560/47087/1/Redislabs-Redis.html)

### Disclaimer

All security reviews are conducted on a "best-effort" basis against a software
component at a point in time. We make no guarantee as to the quality or completeness
of any review. If you believe any content is inaccurate, we encourage you to open
an issue or submit a pull request with a correction or improvement.

### License

This text is released under at least the
[Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt).
Externally-referenced content may be licensed differently.