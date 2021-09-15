---
Publication-State: Active
Access: Public
Reviewers:
- Organization: Open Source Technology Improvement Fund, Quarkslab
  Associated-With-Project: false
  Compensation-Source: External
Domain: Security
Methodology: 
- Code-Review
Issues-Identified: Severe
Package-URLs:
- pkg:github/veracrypt/veracrypt
Review-Date: 2016-08-16
Scope: Implementation/Partial
Schema-Version: 1.18
SPDX-License-Identifier: CC-BY-4.0

---

### Summary

Open Source Technology Improvement Fund, Inc facilitated the security assessment of VeraCrypt 1.18. Carried out by Quarkslab
between Aug. 16 and Sep. 14, 2016, two Quarkslab engineers worked a total of 32 person-days of study.

The audit resulted in the finding of: 

 • 8 Critical Vulnerabilities • 
 • 3 Medium Vulnerabilities • 
 • 15 Low or Informational Vulnerabilities / Concerns • 

This public disclosure of these vulnerabilities coincides with the release of VeraCrypt 1.19 which fixed the vast majority of these high priority concerns. Some of these issues have not been fixed due to high complexity for the proposed fixes, but workarounds have been presented in the documentation for VeraCrypt.

### Details

The audit followed two lines of work:

  • The analysis of the fixes introduced in VeraCrypt after the results of the Open Crypto
    Audit Project’s audit of TrueCrypt 7.1a have been published.
    
  • The assessment of VeraCrypt’s features that were not present in TrueCrypt

All the vulnerabilities that have been taken into account have been correctly fixed (except
a minor missing fix for one of them). In particular, the problem leading to a privilege
escalation discovered by James Forshaw in the TrueCrypt driver just after the OCAP
audit has been solved.

• Vulnerabilities which require substantial modifications of the code or the architecture of
the project have not been fixed. These include:

  – TC_IOCTL_OPEN_TEST multiple issues (need to change the application behavior),
  – EncryptDataUnits() lacks error handling (need to design a new logic to retrieve errors),
  – AES implementation susceptible to cache-timing attacks (need to fully rewrite the
    AES implementations).

• Vulnerabilities leading to incompatibilities with TrueCrypt, as the ones related to cryptographic mechanisms, have not been fixed. Most notable are:

  – Keyfile mixing is not cryptographically sound,
  – Unauthenticated ciphertext in volume headers.
    Ref.: 16-08-215-REP Quarkslab SAS 4

New Problems

Among the problems found during the audit, some must be corrected quickly:
  
  • The availability of GOST 28147-89, a symmetric block cipher with a 64-bit block size, is
    an issue. This algorithm must not be used in this context.
    
  • Compression libraries are outdated or poorly written. They must be updated or replaced.
  
  • If the system is encrypted, the boot password (in UEFI mode) or its length (in legacy
    mode) could be retrieved by an attacker.

Finally, the UEFI loader is not mature yet. However, its use has not been found to cause
security problems from a cryptographic point of view.

### Conclusion

This audit, funded by OSTIF, required 32 person-days of study. It shows that this follow-up of
TrueCrypt is very much alive and evolves with new functionalities like the support of UEFI.
The results shows that evaluations at regular intervals of such difficult security projects are not
an option. When well received by the project’s developers, they provide useful feedback to help
the project mature. The openess of the evaluation results help build confidence in the product
for the final users.


### Methodology

• The analysis of the fixes introduced in VeraCrypt after the results of the Open Crypto
  Audit Project’s audit of TrueCrypt 7.1a have been published.
  
• The assessment of VeraCrypt’s features that were not present in TrueCrypt.

### External References

• [Full Report](https://ostif.org/wp-content/uploads/2016/10/VeraCrypt-Audit-Final-for-Public-Release.pdf)  


### Disclaimer

All security reviews are conducted on a "best-effort" basis against a software
component at a point in time. We make no guarantee as to the quality or completeness
of any review. If you believe any content is inaccurate, we encourage you to open
an issue or submit a pull request with a correction or improvement.

### License

This text is released under at least the
[Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt).
Externally-referenced content may be licensed differently.

