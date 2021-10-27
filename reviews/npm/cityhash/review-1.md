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
- pkg:npm/cityhash@0.0.5
Issues-Identified: Non-Severe
Review-Date: 2019-10-30
Scope: Implementation/Full
Schema-Version: 1.0
SPDX-License-Identifier: CC-BY-4.0
---

### Summary

CityHash is not a cryptographic hash function, and was designed for speed rather
than collision resistence or other security properties.

### Details

CityHash is not a cryptographic hash function, and was designed for speed rather
than collision resistence or other security properties. If you use CityHash, you
should assume an attacker is able to both "invert" (given a hash output, easily
find input that would map to that hash output) and collide (quickly create many
inputs that map to the same output value. This could lead to O(n) hash tables,
caching issues, etc. Ensure that you do not rely on CityHash for security.

### Methodology

This review was conducted by the Microsoft Open Source Security Team using of automated
tools (including static analysis), custom tools, a targeted code review, and some
effort to identify already-known security defects.

### External References

No external references exist for this review.

### Disclaimer

All security reviews are conducted on a "best-effort" basis against a software
component at a point in time. We make no guarantee as to the quality or completeness
of any review. If you believe any content is inaccurate, we encourage you to open
an issue or submit a pull request with a correction or improvement.

### License

This text is released under at least the
[Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt).
Externally-referenced content may be licensed differently.