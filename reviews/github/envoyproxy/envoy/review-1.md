---
Publication-State: Active
Access: Public
Reviewers:
-  Organization: Cloud Native Computing Foundation
   Associated-With-Project: false
   Compensation-Source: External
-  Organization: Linux Foundation
   Associated-With-Project: false
   Compensation-Source: External
-  Organization: Cure53
   Associated-With-Project: false
   Compensation-Source: External
Domain: Security
Methodology:
- External-Review
Issues-Identified: Non-Severe
Package-URLs:
- pkg:github/envoyproxy/envoy@c31077b28e4f8a7db17895d5d2570e806e9e2a3e
Review-Date: 2018-02-01
Scope: Implementation/Full
Schema-Version: 1.0
SPDX-License-Identifier: CC-BY-4.0
---

### Summary

This security audit determined that Envoy maintains a modern, well-written, and secure codebase. Four vulnerabilities and four smaller security issues were detected, however. The vulnerability of highest severity, an insecure Admin-Interface, was not considered a large threat as it was later deemed to be outside of the relevant attack surface. The report does not state whether these security issues have been fixed, but instead emphasized the importance that no threats of critical risk level were identified.

### Details

The Cloud Native Computing Foundation asked Cure53 to conduct an in-depth security assessment of Envoy, which has since been made publicly available. This report was sponsored by the Linux Foundation and includes the scope, test coverage, identified vulnerabilities, and conclusions reached from the assessment, all of which are outlined in further detail in the [report](https://github.com/envoyproxy/envoy/blob/main/docs/SECURITY_AUDIT.pdf).

The analysis was conducted by a team of eight (six from Cure53 and two experts from Secfault Security GmbH) analyzing targeted areas of the codebase. A brief summary of each of the vulnerabilities detected and their relative threat levels are outlined below.

***Vulnerability 1: Lacking Admin-Interface Security allows CSRF and DOS (High)***

This was documented as the only vulnerability of notable concern, as the Admin Interface was insecure. The interface lacks HTTP security headers and does not utilize CSRF tokens. As a result, if an administrator were tricked into clicking a malicious link elsewhere with specified code injection, an external actor would be given full administrative rights. Two examples of such links have been copied from the report below (note the Admin Interface is located at ht<span>tp://</span>localhost:9901):

*Disable Logging:*
`<img src="http://localhost:9901/logging?admin=off">`

*Shutdown the Server:*
`<img src="http://localhost:9901/quitquitquit">`

***Vulnerability 2: Potential BoF with HeaderStrings and Inline Buffers (Medium)***

A potential buffer overflow was found in which the length of the input is not checked prior to a `memcpy` command within the constructor of the `HeaderString` class.

***Vulnerability 3: Potential UaF with HeaderStrings and Ref. Buffers (Medium)***

A potential use-after-free vulnerability was discovered in the Envoy's `HeaderMap` implementation, in which a function returning a reference is assigned to a particular variable that may later be invalidated/deleted. Importantly, in other locations of the codebase, the return value of the reference was assigned instead, protecting against this type of vulnerability in those areas.

***Vulnerability 4: Potential Integer Overflow during Header Encoding (Medium)***

A potential integer overflow was detected where the header encoding is handled, in which two 32-bit unsigned integers are included in an addition operation that is then assigned to a 64-bit unsigned integer, which is used for memory allocation. Using particularly large values would cause this operation to overflow, resulting far less memory allocated, and creates possibilities for buffer overflows later on.

***Smaller Issues***

There were four other issues detected during this security audit, all of which are listed below. It is important to note that these were not labeled vulnerabilities as the vulnerable code was not found to be very accessible/exploitable. For the full details on these additional security issues, see the [report](https://github.com/envoyproxy/envoy/blob/main/docs/SECURITY_AUDIT.pdf).

1. `strlcpy` does not check for zero-sized parameters (Low)
2. User-Controlled Allocation leads to DOS (Medium)
3. Stack Exhaustion via unbounded Recursion (Medium)
4. Lax Parsing when processing malformed Messages (Low)

### Methodology

Cure53 carried out a source code audit and penetration test in order to discover the above vulnerabilities/issues. The scope of this analysis, however, was very targeted due to the sheer size of the project. Thus, attention was focused on areas that posed a high threat such as the HTTP parser and header sanitizer, as well as areas requested by Envoy maintainers such as the TLS configuration, XFF, and DoS attacks.

### External References

* [Full Report](https://github.com/envoyproxy/envoy/blob/main/docs/SECURITY_AUDIT.pdf)
* [GitHub Repository](https://github.com/envoyproxy/envoy/tree/main)

### Disclaimer

All security reviews are conducted on a "best-effort" basis against a software
component at a point in time. We make no guarantee as to the quality or completeness
of any review. If you believe any content is inaccurate, we encourage you to open
an issue or submit a pull request with a correction or improvement.

### License

This text is released under at least the
[Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt).
Externally-referenced content may be licensed differently.
