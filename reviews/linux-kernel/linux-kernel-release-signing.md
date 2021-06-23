---
Publication-State: Active
Access: Public
Reviewers:
- Organization: Open Source Technology Improvement Fund
  Associated-With-Project: false
  Compensation-Source: External
- Organization: Trail of Bits
  Associated-With-Project: false
  Compensation-Source: External  
Domain: Security
Methodology:
- External-Review
Issues-Identified: Non-Severe
Package-URLs:
- pkg:generic/linux-kernel?download_url=https://kernel.org
- pkg:github/torvalds/linux
Review-Date: 2021-04-15
Scope: Non-Implementation
Schema-Version: 1.0
SPDX-License-Identifier: CC-BY-4.0

---
  
### Summary

The Linux Foundation sought a review of the kernel teams’ processes for release signing and for the policies and procedures for the handling of the signing keys. Working with OSTIF, Trail of Bits was selected to lead the project and a two person-week review was conducted.

### Details

This review resulted in seven recommendations that can help improve the robustness of the security and use of the signing keys for the Linux Kernel. Additionally, Trail of Bits suggested that more comprehensive and up to date documentation on the current procedures and policies are needed to help organizations around the world to best understand the current stratagem.

## Use of smart cards for GPG and SSH not enforced for key individuals

Individuals with commit rights on key Linux kernel repositories are not required to store private key material used for GPG or SSH on a separate smart card device, such as a Nitrokey or Yubikey.

# Recommended mitigation

Short term, require individuals with access to significant repositories or systems to use a smart card device to store sensitive key material. If that is not a viable option, consider using an alternative mechanism, such as a TPM, to protect sensitive cryptographic material.

## Recommended smartcard does not require touch activation

The Linux Foundation recommends that kernel developers use smart cards, specifically Nitrokeys, to secure their private key material. Linux Foundation-issued Nitrokeys do not require users to perform any physical actions when using smart card functions. Other devices can be configured to require the user to touch the device before the smart card operations occur. As a result, the Nitrokey is protected only by a passphrase while inserted into a workstation.

While touch activation does not prevent all classes of attacks, such as ones that replace binaries on disk (e.g., for GPG and SSH) or leverage session hijacking, it prevents entire classes of less sophisticated attacks and improves the security posture of a given end-user.

# Recommended mitigation

Consider mandating the use of smart card devices that require physical touch to validate each smart card operation. If that is not practical, add guidance recommending that a smart card be physically connected to a workstation only when it is required to complete an operation, which would help prevent an attacker from using an attached smart card device without its user’s knowledge.

# Response

The Linux Foundation Kernel Team members said that because the Yubikey with touch activation is not open source, it is not possible to use for critical infrastructure security. However, they would consider updating their policies to recommend that the current Nitrokeys be physically removed from the administrator’s computer when they are not in use. In the longer term we hope for more options for open source software in touch activated devices.

## Lack of documented key management policies and procedures

There is no centralized, authoritative documentation laying out policies and procedures for key revocation, generation, or rotation or other key management tasks. Without such documentation, users and administrators are more likely to make serious errors when engaging in routine and emergent key management tasks.

# Recommended mitigation

Short term, work with administrators and developers to document current procedures and policies and compile that information into a single set of documents that can be updated as necessary.

Long term, periodically review policies and procedures, assessing their applicability and appropriateness. Update the documentation as policies and procedures change.

# Response

The Linux Foundation Kernel Team members have affirmed that improved documentation is needed to reduce the chance of errors and improve incident response.

## Lack of public-key authentication resources

To verify the content of kernel updates, each commit in the git tree produces a signed tag, and each release is accompanied by a signature over the release’s tarball. Public keys for Linux developers, as well as the associated key signatures forming the web of trust, are managed from a single location. Compromise of the git.kernel.org server would allow an attacker to provide users with a web of public keys not controlled by kernel developers, enabling them to post malicious kernel “releases” that would validate against the attacker’s public keys.

Bootstrapping trust for public-key systems is a hard problem, and is certainly not unique to the Linux kernel. Any software that relies on digital signatures for verification must first “bootstrap” trust by ensuring that users have the correct public key. It creates a circular problem that is difficult to solve in the general case.

The Linux Foundation is uniquely equipped to alleviate this problem. Because of Linux’s community and commercial support, kernel developers have many ways to distribute PGP key fingerprints for important developers. Key fingerprints can be included in conference presentations, periodically published on news sites such as lwn.net, included in email signatures, or published on websites maintained by Linux Foundation partners like Red Hat or IBM. Key fingerprints hosted on the kernel.org infrastructure could then be validated against multiple public sources, reducing the likelihood of a malicious key being trusted.

# Recommended mitigation

Short term, identify effective ways to widely advertise developers’ key fingerprints. These could include adding key fingerprints to email signatures, periodically posting them in mailing lists, or referencing them in conference presentations. Long term, continue advertising keys through multiple channels, and work with partners to provide accessible sources of public-key corroboration.

# Response

The Linux Foundation Kernel Team members have expressed interest in both the short and long term recommendations.

## Use of older public-key algorithms and standards within web of trust

PGP keys used by kernel developers vary significantly in terms of algorithm and key size. RSA is the most commonly used algorithm, followed by DSA and elliptic curve algorithms. Work estimates for attacking algorithms based on integer factorization and integer discrete logarithms vary widely, and the algorithms are frequently subject to subtle new failure modes. Trail of Bits generally recommends moving away from RSA where possible in favor of elliptic curve algorithms.

Since these keys are used to verify code that is eventually incorporated into the kernel, modern primitives should be used. Using a single modern algorithm and key size will help reduce the attack surface for sophisticated attackers.

# Recommended mitigation

Short term, choose a single algorithm and key size for new keys incorporated into the kernel web of trust and the PGP key repository. The current kernel developer guidance suggests using ECDSA or Ed25519 keys. Requiring all new keys to conform to this guidance would be an effective step toward standardization.

Long term, work with developers to gradually replace older RSA and traditional DSA keys with new policy-compliant keys and integrate them into the kernel web of trust. Establish a “sunset date” by which all keys should be switched over.

## Lack of external integrity validation mechanisms

Kernel releases involve a series of steps such as merging changes in Git repositories, pushing tags, and generating a tarball for release. Currently, verification of the steps’ integrity largely depends on the wider community to notice incorrect or malicious behavior. Although this can be effective, additional integrity checks would greatly increase the robustness of the system and help reduce the implicit trust placed in the infrastructure.

# Recommended mitigation

Short term, consider releasing tooling that can compare release tarball content with the content of the tagged Git release, as well as tooling that can ensure that all commits to key repositories hosted on kernel.org are signed with an expected identity. Also consider running a verifier on kernel.org systems.

Long term, consider advocating for interested independent parties to run these verification tools to bolster the integrity verification mechanisms of the wider Linux kernel community.

## Lack of SSH key rotation

Currently, SSH keys used to access kernel.org infrastructure are static. Because SSH keys can often be leveraged to access additional systems, they are frequently targeted by attackers. Under the current setup, recovery of a single developer’s SSH key could allow indefinite access to kernel.org resources.

A key rotation schedule would mitigate the impact of an SSH key compromise on the kernel.org system. Moreover, with a system in place for rotating SSH keys, the Linux Foundation could respond to an attack that compromises these keys more quickly.

# Recommended mitigation

Short term, develop an appropriate key rotation schedule to limit the impact of a compromised SSH key.

Long term, ensure that key rotation policy is followed and that administrators are practiced in key rotation procedures. This will limit the threat posed by compromised keys and ensure that administrators are capable of quickly rotating keys when a compromise is discovered.

### Methodology

This project involved multiple one-on-one interviews with members of the kernel team as well as representatives from the stakeholders where opportunities to investigate were discussed. Additionally, the audit team looked at documentation, articles, public talks, and discussions that took place over the last few years to construct a best-possible picture of the current topology.

### External References

A link to the full report is available for free at: https://ostif.org/a-review-of-the-linux-kernels-release-signing-and-key-management-policies/

### Disclaimer

All security reviews are conducted on a "best-effort" basis against a software
component at a point in time. We make no guarantee as to the quality or completeness
of any review. If you believe any content is inaccurate, we encourage you to open
an issue or submit a pull request with a correction or improvement.

### License

This text is released under at least the
[Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt).
Externally-referenced content may be licensed differently.
