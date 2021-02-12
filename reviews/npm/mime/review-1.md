<!--
publication-state: published
access: public
author: Dilan Bhalla
domain: security
methodology-summary: static-analysis;web-search
opinion: secure
package-urls:
- "pkg:npm/mime@1.3.6"
review-date: 2021-02-12
scope: implementation/full
schema-version: 1.0
severity: low
SPDX-License-Identifier: CC-BY-4.0
-->

### Summary

Older versions of this package are susceptible to a low severity vulnerability.

### Details

Versions before 1.4.1, as well as versions 2.0.1 and 2.0.2 of this package are susceptible to a Regular Expression Denial of Service attack, that can allow an attacker to slow down the user's system. It is recommended to upgrade to a more recent version of this package where the vulnerability is patched.

### Methodology

1. Static Analysis (CodeQL)
2. Additional research

### External References

1. https://snyk.io/test/npm/mime/1.3.6
2. https://www.cvedetails.com/vulnerability-list/vendor_id-20879/Mime-Project.html
3. https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=mime

### License

This text is released under at least the
[Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt).
External references are under their own licenses, which may be different.

### Disclaimer

All security reviews are conducted on a "best-effort" basis against a software
component at a point in time. We make no guarantees that any review will be accurate
or complete. If you dispute any content within a review, feel free to open an issue
or submit a pull request with a correction or improvement.
