---
Publication-State: Draft
Access: Public
Reviewers:
- Organization: OpenSSF / Omega
  Associated-With-Project: false
  Compensation-Source: none
Domain: Security
Methodology:
- Static-Analysis
Issues-Identified: None
Package-URLs:
- pkg:npm/destroy@1.0.4
Review-Date: 2022-05-08
Scope: Implementation/Full
Schema-Version: 1.0
SPDX-License-Identifier: CC-BY-4.0
Private/OpenSSF:
- Omega-Analyzer-Version: 0.7.1
- Omega-Tag: POC;2022-05-05;HC2-ACEG-T100
---

### Summary

This package was analyzed using the Omega analysis toolchain. No significant issues were
discovered, and as of 2022-05-08, no publicly-known security
vulnerabilities are known to affect this version of the package.

**IMPORTANT:** This review is 'draft' and experimental at this stage. Do not rely on its 
correctness for anything.

### Details

This package was analyzed using the Omega analysis toolchain. No significant issues were
discovered, and as of 2022-05-08, no publicly-known security
vulnerabilities are known to affect this version of the package.

Analyses may be reproduced using the Omega
[analysis toolchain](https://github.com/alpha-omega/blob/main/omega/analysis/), version
0.7.1).

Summarized Results:

✔ CodeQL Analysis - PASS

✔ Detect-Secrets - PASS

✔ NodeJSScan - PASS

✔ Semgrep - PASS

✔ Rebuildable - PASS

✔ No Public Vulnerabilities - PASS

### Methodology

This automated review was executed by the Omega Analysis toolchain, version '0.7.1'
on 2022-05-08. Only a subset of results were taken into account
when creating this review. For more information, view the toolchain referenced in the
`External References` section below.

The [Open Source Insights](https://deps.dev) website was used to identify publicly-known
vulnerabilities.

The [OSS Gadget](https://github.com/Microsoft/OSSGadget) reproducibility checker was used to
ensure the deployed package could be recreated from source code.

### External References

* [Home Page](https://github.com/stream-utils/destroy)
* [Project Issue Tracker](https://github.com/stream-utils/destroy/issues)
* [Project Repository](https://github.com/stream-utils/destroy)
* [Package on deps.dev](https://deps.dev/npm/destroy/1.0.4)
* [Omega Analysis Toolchain](https://github.com/alpha-omega/blob/main/omega/analysis)

### Disclaimer

This security review was conducted against the specific version included in the 
`Package-URLs` section of this review, at a point in time, using a set of imperfect tools.
This review does not in any way guarantee the quality, completeness of analysis, or lack of
vulnerability. 

### License

This text is released under at least the
[Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt).
Externally-referenced content may be licensed differently.