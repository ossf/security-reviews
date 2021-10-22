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
Issues-Identified: Not Examined
Package-URL(s):
- pkg:github.com/zerotier
Review-Date: 2020-03-23
Scope: Non-Implementation
Schema-Version: 1.0
SPDX-License-Identifier: CC-BY-4.0
---

### Summary

Trail of Bits performed an assessment of the cryptographic components of the ZeroTier protocol. ZeroTier provided some documentation of the protocol and communicated further details about the protocol to Trail of Bits.

### Details

Overall, the assessment resulted in a series of constructive conversations about various components of ZeroTier’s protocol. Trail of Bits has concluded the AES-GMAC-SIV construction satisfies its desired goals: It is a secure, nonce–misuse-resistant authenticated encryption scheme; it is FIPS compliant; and its security bounds fit within the system’s constraints. The public-key infrastructure is also FIPS compliant.

As the protocol continues to evolve, recommendations and concerns should be addressed. These concerns comprise theoretical attacks in which the attacker has some amount of control over the network infrastructure or sections of the code that could introduce serious vulnerabilities without careful consideration, but do not in themselves make ZeroTier an insecure protocol. 

ZeroTier should also consider the effect of nodes and network infrastructure controlled by a powerful attacker, and assume nation-states have the resources to mount these attacks. Further, Trail of Bits recommends stating explicitly the protocol’s security guarantees and assumptions. Code implementations should be checked for compliance against the specification; writing these guarantees and assumptions clearly will help ensure compliance. Overall, Trail of Bits find the protocol to be well designed, and ZeroTier will be protected against wide classes of network attacks if it is implemented in line with the protocol described to Trail of Bits.

### Methodology

No methodology was provided.

### External References

Report: https://github.com/trailofbits/publications/raw/master/reviews/ZeroTierProtocol.pdf

### Disclaimer

All security reviews are conducted on a "best-effort" basis against a software
component at a point in time. We make no guarantee as to the quality or completeness
of any review. If you believe any content is inaccurate, we encourage you to open
an issue or submit a pull request with a correction or improvement.

### License

This text is released under at least the
[Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt).
Externally-referenced content may be licensed differently.
