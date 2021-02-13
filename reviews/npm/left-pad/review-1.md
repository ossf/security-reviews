---
Publication-State: Active
Access: Public
Reviewers:
- Name: Microsoft OSS Security Team
  Email: oss-security-team@microsoft.com
  Organization: Microsoft
  Associated-With-Project: false
  Compensation-Source: none
Domain: Security
Methodology:
- Static-Analysis
- Web-Search
- Code-Review
Issues-Identified: None
Package-URLs:
- pkg:npm/left-pad@1.3.0
Review-Date: 2019-04-08
Scope: Implementation/Full
Schema-Version: 1.0
SPDX-License-Identifier: CC-BY-4.0
---

### Summary

This is a relatively simple module for padding strings. A review did not identify any security defects.

### Details

This is a relatively simple module for padding strings. A review did not identify any security defects, but the module itself has been deprecated; the module author suggests using `String.prototype.padStart()` instead. The associated GitHub [repository](https://github.com/left-pad/left-pad) has also been archived.

### Methodology

This review was conducted by the Microsoft Open Source Security Team using of automated
tools (including static analysis), custom tools, a targeted code review, and some
effort to identify already-known security defects.

### External References

* [npmjs.com/package/left-pad](https://www.npmjs.com/package/left-pad)
* [github.com/left-pad/left-pad](https://github.com/left-pad/left-pad)

### Disclaimer

All security reviews are conducted on a "best-effort" basis against a software
component at a point in time. We make no guarantee as to the quality or completeness
of any review. If you believe any content is inaccurate, we encourage you to open
an issue or submit a pull request with a correction or improvement.

### License

This text is released under at least the
[Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt).
Externally-referenced content may be licensed differently.
