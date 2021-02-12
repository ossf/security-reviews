<!--
publication-state: draft
access: public
author: Dilan Bhalla
domain: security
methodology-summary: static-analysis;web-search
opinion: insecure
package-urls:
- "pkg:npm/atom-node-module-installer@0.9.0"
review-date: 2021-02-12
scope: implementation/full
schema-version: 1.0
severity: critical
SPDX-License-Identifier: CC-BY-4.0
-->

### Summary

Known critical vulnerability. Do not use this package if possible, as there is no existing patch. If necessary, ensure you are on a private, trusted network during installation.

### Details

This package installs node modules over an insecure protocol (HTTP) and is thus susceptible to MITM attacks. Remote code can be executed by an attacker if they are on the same network, or if the user is using a public network.

### Methodology

• Static Analysis - CodeQL
    • Converted CoffeScript to JavaScript using decaffeinate, an npm package
    • Ran all security queries on package
• Additional Research

### External References

• https://nvd.nist.gov/vuln/detail/CVE-2016-10620.   
• https://www.npmjs.com/advisories/216

### License

This text is released under at least the
[Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt).
External references are under their own licenses, which may be different.

### Disclaimer

All security reviews are conducted on a "best-effort" basis against a software
component at a point in time. We make no guarantees that any review will be accurate
or complete. If you dispute any content within a review, feel free to open an issue
or submit a pull request with a correction or improvement.

