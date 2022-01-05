---
Publication-State: Active
Access: Public
Reviewers:
  Organization: Open Source Technology Improvement Fund
  Associated-With-Project: false
  Compensation-Source: External
Domain: Security
Methodology:
- External-Review
- Manual Code Review
Issues-Identified: Severe
Package-URLs:
- pkg:github/NLnetLabs/unbound
Review-Date: 2019-12-19
Scope: Implementation/Full
Schema-Version: 1.0
SPDX-License-Identifier: CC-BY-4.0

---
  
### Summary

The audit of UnboundDNS, facilitated by Open Source Technology Improvement Fund, Inc (ostif.org) resulted in a total of 48 changes that either improve security or fix minor issues that could lead to future security problems as the application grows and evolves over time. The consensus is that Unbound has greatly benefited from the work and that the users and applications that depend on it are now safer than they were prior to the audit. A patch was released and all other outstanding issues were corrected in versions 1.9.4 and 1.9.5.

### Details

One Critical, Five High, and Five Medium severity issues were found, with an additional 39 issues that were rated as low or informational severity.

CVE-2019-18934 – CRITICAL – Shell Injection in IPSECMOD
FIXED in commit 09845779d5f2c96e3064ff398cad65c08357cfbf

When using the IPSECMOD module, a malicious DNS response from a client can inject commands into the host machine.

CVE-2019-16866 – HIGH – Uninitialized Memory in worker_handle_request()
FIXED in commit b60c4a472c856f0a98120b7259e991b3a6507eb5

A use-after-free issue in worker_handle_request() can lead to remote code execution or denial of service.

HIGH – Config Injection in create_unbound_ad_servers.sh
FIXED in commit f887552763477a606a9608b0f6b498685e0f6587

The bash script in contrib/create_unbound_ad_servers.sh does not properly sanitize the retrieved data before it is outputted into a configuration file. This allows to modify the configuration by having several statements on a single line. Since the input is retrieved via unencrypted, unauthenticated HTTP an attacker on the wire might be able to abuse this issue.

HIGH – Integer Overflow in Regional Allocator
FIXED in commit 226298bbd36f1f0fd9608e98c2ae85988b7bbdb8

When the regional allocator in util/regional.c is used to allocate memory via regional_alloc() integer overflows can happen. If size is big enough the first call to malloc() will have a parameter that is
smaller than expected. Furthermore the macro ALIGN_UP could overflow causing r->available to point at a bad memory location.

HIGH – Integer Overflow in sldns_str2wire_dname_buf_origin()
FIXED in commit a3545867fcdec50307c776ce0af28d07046a52dd

The function sldns_str2wire_dname_buf_origin() in sldns/str2wire.c converts a string to dname wireformat, concatenating with origin when the domain name is relative. Several checks are performed to avoid a buffer overflow when writing the result into buf. Nevertheless, when dlen + origin_len is bigger than sizeof(size_t), the calculation will wrap around, resulting in the value of the addition being smaller than the operands. When this happens, the checks might be bypassed and could lead to memmove() writing out of bounds. An out of bounds write produces unexpected results and can usually be abused by an attacker to gain remote code execution.

HIGH – Out of Bounds Write in sldns_bget_token_par()
FIXED in commit fa23ee8f31ba9a018c720ea822faaee639dc7a9c

The function sldns_bget_token_par() in sldns/parse.c returns a token from a buffer. While parsing the input buffer, char by char, certain inputs will result in a write and increment to the token buffer without checking boundary limits. A specially crafted input could repeatedly trigger this unbounded write and eventually perform a write outside of token ’s bounds. An out of bounds write produces unexpected results and can usually be abused by an attacker to gain remote code execution.

MEDIUM – Assert Causing DoS in synth_cname()
FIXED in commit f5e06689d193619c57c33270c83f5e40781a261d

It is possible to trigger an log_assert() in synth_cname() by sending invalid packets to the server. This issue should not be fixed by disabling asserts, as this raises an additional possible integer underflow issue. If asserts are disabled during compilation, this might lead to an out of bounds write in dname_pkt_copy() since the computation alias+(qnamelen-dname_rrset->dname_len) might become negative due to an underflow.

MEDIUM – Assert Causing DoS in dname_pkt_copy()
FIXED in commit d2eb78e871153f22332d30c6647f3815148f21e5

It is possible to trigger an assert() in dname_pkt_copy() by sending invalid packets to the server.

MEDIUM – Integer Overflows in Size Calculations
FIXED in commit 02080f6b180232f43b77f403d0c038e9360a460f

In different files and functions sizes are calculated that are later passed on to different allocation functions such as malloc(). Several of these cases are not protected against integer overflows.

MEDIUM – Insufficient Handling of Compressed Names in dname_pkt_copy()
FIXED in commit 2d444a5037acff6024630b88092d9188f2f5d8fe

In dname_pkt_copy() an infinite loop can be caused by the input data \xC0\x00. This will cause the LABEL_IS_PTR macro to return true and set lablen to 0, causing the checking to start at the beginning of the input again. Additionally, the log_assert() can be triggered quite easily, leading to another DoS.

MEDIUM – Out of Bound Write Compressed Names in rdata_copy()
FIXED in commit 6c3a0b54ed8ace93d5b5ca7b8078dc87e75cd640

In rdata_copy(), if the len parameter becomes bigger than the size of the packet (pkt_len ), the memmove() is performed before the check in log_assert(). It seems that, due to the fact that packets are first parsed by other functions that check for
unbounded pointers, this might not be exploitable.

### Methodology

A combination of manual code auditing, dynamic analysis using a custom fuzzing harness, and
static analysis was used to perform the audit.


### External References

A link to the full report is available for free at: https://ostif.org/our-audit-of-unbound-dns-by-x41-d-sec-full-results/

### Disclaimer

All security reviews are conducted on a "best-effort" basis against a software
component at a point in time. We make no guarantee as to the quality or completeness
of any review. If you believe any content is inaccurate, we encourage you to open
an issue or submit a pull request with a correction or improvement.

### License

This text is released under at least the
[Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt).
Externally-referenced content may be licensed differently.
