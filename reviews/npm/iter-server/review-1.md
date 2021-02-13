<!--
publication-state: draft
access: public
author: Dilan Bhalla
domain: security
methodology-summary: web-search
opinion: insecure
package-urls:
- "pkg:npm/iter-server@1.0.0"
review-date: 2021-02-12
scope: implementation/full
schema-version: 1.0
severity: critical
SPDX-License-Identifier: CC-BY-4.0
-->

### Summary

Directory traversal vulnerability in package. No patches available, it is best to avoid using this package in a production environment.

### Details

The latest version of this package (and only version, 1.0.0) accepts relative file paths, leaving it susceptible to a directory traversal exploit. This can allow others access to private files outside of the desired root directory.  

Potential exploit from https://www.npmjs.com/advisories/349:  

```
GET /../../../../../../../../../../etc/passwd HTTP/1.1  
host:foo
```

### Methodology

In-depth research and analysis from multiple sources, listed in the external references section below.

### External References

1. https://nvd.nist.gov/vuln/detail/CVE-2017-16183
2. https://www.npmjs.com/advisories/454
3. https://github.com/JacksonGL/NPM-Vuln-PoC/tree/master/directory-traversal/iter-server
4. https://www.npmjs.com/package/iter-server (npm website, to ensure no patches have been released)

### License

This text is released under at least the
[Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt).
External references are under their own licenses, which may be different.

### Disclaimer

All security reviews are conducted on a "best-effort" basis against a software
component at a point in time. We make no guarantees that any review will be accurate
or complete. If you dispute any content within a review, feel free to open an issue
or submit a pull request with a correction or improvement.
