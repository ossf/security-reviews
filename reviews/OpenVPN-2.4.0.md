---
Publication-State: Active
Access: Public
Reviewers:
- Organization: Open Source Technology Improvement Fund, Quarkslab
  Associated-With-Project: false
  Compensation-Source: External
Domain: Security
Methodology: 
- Source-Code Audit
Issues-Identified: Critical
Package-URLs:
- pkg:github/OpenVPN
Review-Date: 2017-05-11
Scope: Implementation/Full
Schema-Version: 2.4.0
SPDX-License-Identifier: CC-BY-4.0

---

### Summary

The Open Source Technology Improvement Fund, Inc (ostif.org) organized a coalition of organizations to conduct an in-depth security assessment of OpenVPN 2.4.0, The report is publicly available at the link below. The report includes the scope, test coverage, identified vulnerabilities, and conclusions reached from the assessment. Seven vulnerabilities were detected: one critical, one medium, and five low/informational. The critical vulnerability addressed a pre-authentication Denial of Service attack vector, along with other related issues. The initial public disclosure of these vulnerabilities coincided with the release of OpenVPN 2.4.2 which fixes all of the high priority concerns. 

### Details

OpenVPN 2.4.0, the NDIS6 TAP Driver for Windows, the Windows GUI, and Linux versions were evaluated. This release included a number of new features including control channel encryption.

QuarksLab found:
1 Critical/High Vulnerability (CVE-2017-7478)
1 Medium Vulnerability (CVE-2017-7479)
5 Low or Informational Vulnerabilities / Concerns

Because of this audit, the OpenVPN development team has issued a number of fixes in OpenVPN 2.4.2.

### The fixes include:

#### - Correction of a pre-authentication Denial of Service attack. An attacker can crash any OpenVPN client or server without any credentials or keys.
#### - Correction of an authenticated user Denial of Service attack. An attacker can crash an OpenVPN client or server using an AEAD mode cipher by sending crafted data to exhaust the packet counter. Requires authentication.
#### - Correction of issues in mbedtls (PolarSSL) X509 certificate handling. Verify return values of mbedtls_x509_dn_gets and mbedtls_x509_serial_gets correctly.
#### - Correction of usernames and passwords not being properly erased. for the new bootloader. (keystrokes not erased after authentication)
#### - Correction of null pointer dereferences. Because this issue is low-severity and not exploitable, this fix is reserved for a future release.
#### - Correction of service handling for OpenVPN GUI. The OpenVPN GUI did not properly terminate the service when closed.
#### - Improvements to documentation of the OpenVPN protocol. Improving transparency of functionality for developers working with the OpenVPN protocol.
#### - Updates to user documentation for other vulnerabilities that can be closed by user practices. Such as selecting more secure options, and deprecating antiquated options that are unsafe.

### Furthermore the following was affirmed:

#### - When using OpenSSL, OpenVPN uses the RAND_bytes function for entropy exclusively. It appears to utilize it correctly with proper error handling.
#### - When using mbedTLS, OpenVPN uses the mbedtls_ctr_drbg_random function for entropy exclusively. It appears to utilize it correctly with proper error handling.
#### - When generating “non critical” random values, OpenVPN uses a custom algorithm that is non-standard but cryptographically sound.
#### - OpenVPN contains some legacy code related to end-of-life versions of OpenSSL that are no longer supported.



### Methodology

An in-depth source code audit.  Main focus was on the source code of OpenVPN 2.4.0, on OpenVPN GUI 11.4.0.0 and on
the TAP driver used by OpenVPN for Windows. The scope of the audit includes Linux and Windows versions of OpenVPN.

### External References

• [Full Report](https://ostif.org/wp-content/uploads/2017/05/OpenVPN1.2final.pdf)  


### Disclaimer

All security reviews are conducted on a "best-effort" basis against a software
component at a point in time. We make no guarantee as to the quality or completeness
of any review. If you believe any content is inaccurate, we encourage you to open
an issue or submit a pull request with a correction or improvement.

### License

This text is released under at least the
[Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt).
Externally-referenced content may be licensed differently.
