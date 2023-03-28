---
Publication-State: Active
Access: Public
Reviewers:
- Name: Jonathan Leitschuh
  Email: Jonathan.Leitschuh@linuxfoundation.org
  Organization: OpenSSF
  Associated-With-Project: False
  Compensation-Source: External
Domain: Security
Methodology:
- Code-Review
Issues-Identified: None
Package-URL(s):
- pkg:maven/com.typesafe.play/play_2.13@2.8.19
- pkg:maven/com.typesafe.play/play-java_2.13@2.8.19
Review-Date: 2023-03-28
Scope: Implementation (Partial)
Schema-Version: 1.0
SPDX-License-Identifier: CC-BY-4.0
---

### Summary

Performed a cursory investigation looking for HTTP Response Splitting via CRLF injection in the header values returned via an HTTP response.

### Details

No CRLF injection was possible.

### Methodology

Source code audit and writing unit tests within the codebase itself to test the injection of CRLF.

```scala
Results.Ok("Ok").withHeaders("X-Test" -> "Value\r\nX-Malicious: Malicious")
```

### External References

No external references were provided.

### Disclaimer

All security reviews are conducted on a "best-effort" basis against a software
component at a point in time. We make no guarantee as to the quality or completeness
of any review. If you believe any content is inaccurate, we encourage you to open
an issue or submit a pull request with a correction or improvement.

### License

This text is released under at least the
[Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt).
Externally-referenced content may be licensed differently.
