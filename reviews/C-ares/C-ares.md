---
Publication-State: Active
Access: Public
Reviewers:
  Organization: X41 D-Sec
  Associated-With-Project: False
  Compensation-Source: External
Domain: Security
Methodology:
- Static-Analysis
- Dynamic-Analysis
- Code-Review
- External-Review
- Fuzzing
Issues-Identified: Non-Severe
Package-URL(s):
- pkg:c-ares/c-ares
Review-Date: 2023-05-30
Scope: Implementation (Full)
Schema-Version: 1.0
SPDX-License-Identifier: CC-BY-4.0
---

### Summary

Open Source Technology Improvement Fund organized a security audit of c-ares, funded by Amazon Web Services and carried out by X41 D-Sec.

### Details

C-ares is a library written in C for asynchronous DNS requests, which runs on such applications as Microsoft Windows, Netware, and Android. It was developed at MIT, when a group expanded upon the capabilities of the ares library and licensed c-ares in 1998. 

Overall, X41 found the c-ares library to be well designed and implemented. The audit found six inconsistencies during the process. Three vulnerabilities were rated as medium, three others as informational. Alongside performing static manual code review, the X41 team implemented and customized AFL++ fuzzers during this audit. Recently, AFL++ fuzzers have been made to support command-line interface (CLI) fuzzing, which was important to this audit as c-ares is made up of multiple CLI tooling components in its code base. While the audit particularly focused on memory corruption vulnerabilities which are common in C libraries, two of the medium vulnerabilities were categorized as CWE 330 – Use of Insufficiently Random Values.

### Methodology

No methodology was provided.

### External References

https://ostif.org/our-audit-of-c-ares-is-complete/

### Disclaimer

All security reviews are conducted on a "best-effort" basis against a software
component at a point in time. We make no guarantee as to the quality or completeness
of any review. If you believe any content is inaccurate, we encourage you to open
an issue or submit a pull request with a correction or improvement.

### License

This text is released under at least the
[Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt).
Externally-referenced content may be licensed differently.
