---
Publication-State: Active
Access: Public
Reviewers:
  Organization: Trail of Bits
  Associated-With-Project: False
  Compensation-Source: External
Domain: Security
Methodology:
- External-Review
Issues-Identified: Severe
Package-URL(s):
- pkg:github.com/westerndigitalcorporation
Review-Date: 2020-01-24
Scope: Implementation (Partial)
Schema-Version: 1.0
SPDX-License-Identifier: CC-BY-4.0
---

### Summary

From April 8th to April 26th 2019 Trail of Bits conducted an analysis of the SanDisk X600 SED drive firmware source code to determine if Western Digital’s proposed modifications resolved the set of cryptographic key management issues disclosed by Radboud University researchers. Radboud University contacted Western Digital in December 2018 to disclose multiple vulnerabilities discovered during their research. Western Digital developed a set of fixes and engaged Trail of Bits to validate their remediation for the protection of data at rest on the drive.

### Details

Trail of Bits has determined that the changes resolve the following documented issues:
* When an unlocked range was present on disk the key hierarchy contained a linkage between a KEK encrypted under an empty password and an intermediate encrypting key that allowed locked range decryption without the correct user password.
* TCG Activated and ATA security mode used the same raw PIN_KEK when initialized. When combined with the empty password-encrypted KEK from the previous vulnerability, this allowed decryption of a drive in ATA security mode if the drive was switched from TCG to ATA mode.
* With ATA security enabled the Master password remained linked to the data encryption key (DEK) when the drive was switched into Maximum capability mode.

For each of the issues Trail of Bits reviewed the original design, documentation of the proposed fix, and the concrete implementation of that fix to confirm that the vulnerability in question had been resolved. All three vulnerabilities listed above have been resolved by the changes that Western Digital has made to their design and firmware implementation.

### Methodology

No methodology was provided.

### External References

Report: https://github.com/trailofbits/publications/blob/master/reviews/sandiskx600.pdf

### Disclaimer

All security reviews are conducted on a "best-effort" basis against a software
component at a point in time. We make no guarantee as to the quality or completeness
of any review. If you believe any content is inaccurate, we encourage you to open
an issue or submit a pull request with a correction or improvement.

### License

This text is released under at least the
[Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt).
Externally-referenced content may be licensed differently.
