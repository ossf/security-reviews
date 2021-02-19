---
Publication-State: Active
Access: Public
Reviewers:
- Organization: Microsoft (OSS Security Team)
  Associated-With-Project: false
  Compensation-Source: none
Domain: Security
Methodology:
- Static-Analysis
- Code-Review
Issues-Identified: Severe
Package-URLs:
- pkg:npm/msft-wam@0.0.7
- pkg:npm/msft-wam@0.0.8
- pkg:npm/msft-wam@0.4.7
Review-Date: 2021-02-12
Scope: Implementation/Partial
Schema-Version: 1.0
SPDX-License-Identifier: CC-BY-4.0
---

### Summary

This package contains what appears to be a proof-of-concept for the "[dependency confusion](https://medium.com/@alex.birsan/dependency-confusion-4a5d60fec610)"
vulnerability. It exfiltrates basic information (hostname, username, local path) to a remote server using a "postinstall" script. 

Affected packages were removed from the NPM registry on February 12, 2021.

### Details

This package contains what appears to be a proof-of-concept for the "[dependency confusion](https://medium.com/@alex.birsan/dependency-confusion-4a5d60fec610)"
vulnerability. It exfiltrates basic information (hostname, username, local path) to a remote server using a "postinstall" script. While there was no text within
the package that explicitly stated it to be a proof of concept, the username suggested it was created by a security researcher.

### Methodology

We built custom tooling to discover these packages and after manual triage, we reported them to the NPM security team.

### External References

* [Dependency Confusion: How I Hacked Into Apple, Microsoft and Dozens of Other Companies](https://medium.com/@alex.birsan/dependency-confusion-4a5d60fec610)
* [Avoiding npm substitution attacks](https://github.blog/2021-02-12-avoiding-npm-substitution-attacks/)
* [3 Way to Mitigate Risk When Using Private Package Feeds](https://azure.microsoft.com/en-us/resources/3-ways-to-mitigate-risk-using-private-package-feeds/)

### Disclaimer

All security reviews are conducted on a "best-effort" basis against a software
component at a point in time. We make no guarantee as to the quality or completeness
of any review. If you believe any content is inaccurate, we encourage you to open
an issue or submit a pull request with a correction or improvement.

### License

This text is released under at least the
[Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt).
Externally-referenced content may be licensed differently.
