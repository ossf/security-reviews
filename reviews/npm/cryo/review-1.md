---
Publication-State: Draft
Access: Public
Reviewers:
- Name: Dilan Bhalla
  Associated-With-Project: false
  Compensation-Source: none
Domain: Security
Methodology:
- Static-Analysis
- Web-Search
Issues-Identified: Severe
Package-URLs:
- pkg:npm/cryo@0.0.6
Review-Date: 2021-02-13
Scope: Implementation/Full
Schema-Version: 1.0
SPDX-License-Identifier: CC-BY-4.0
---

### Summary

Known, high-severity code injection in latest version of cryo (0.0.6) allows arbitrary code to be executed by malicious actors.

### Details

This package deserializes JSON into objects using an insecure method. As a result, an attacker can inject arbitrary code that may later be called by the user's application and run on the their system. This is a high severity vulnerability without a patch currently available, so it is advisable to avoid using this library.

### Methodology

1. Static analysis (CodeQL)
2. Multiple credible sources referenced, attached in external references below.

### External References

1. https://nvd.nist.gov/vuln/detail/CVE-2018-3784
2. https://hackerone.com/reports/350418

### Disclaimer

All security reviews are conducted on a "best-effort" basis against a software
component at a point in time. We make no guarantee as to the quality or completeness
of any review. If you believe any content is inaccurate, we encourage you to open
an issue or submit a pull request with a correction or improvement.

### License

This text is released under at least the
[Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt).
Externally-referenced content may be licensed differently.
