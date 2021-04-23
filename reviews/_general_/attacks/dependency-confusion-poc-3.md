---
Publication-State: Active
Access: Public
Reviewers:
- Organization: Microsoft (OSS Security Team)
  Associated-With-Project: false
  Compensation-Source: none
Domain: Security
Methodology:
- Static-Analysis
- Code-Review
Issues-Identified: Severe
Package-URLs:
- pkg:npm/add-tw@91.0.0
- pkg:npm/dep-b@1.0.0
- pkg:npm/dep-c@1.0.0
- pkg:npm/dep-e@2.0.0
- pkg:npm/ember-addon-with-dependencies@1.0.0
- pkg:npm/ember-after-blueprint-addon@1.0.0
- pkg:npm/ember-before-blueprint-addon@1.0.0
- pkg:npm/ember-cli-nested@1.0.0
- pkg:npm/ember-foo-env-addon@1.0.0
- pkg:npm/ember-generated-with-export-addon@1.0.0
- pkg:npm/ember-non-root-addon@1.0.0
- pkg:npm/ember-random-addon@1.0.0
- pkg:npm/ember-views@0.9.9-zendesk
- pkg:npm/ember-yagni@1.0.0
- pkg:npm/eslint-plugin-workday-custom-rules@1.0.0
- pkg:npm/eslint-plugin-workday-custom-rules@1.0.1
- pkg:npm/eslint-plugin-workday-custom-rules@1.0.2
- pkg:npm/fake-dependency@1.0.1
- pkg:npm/fake-yarn-dependency@1.0.1
- pkg:npm/kfcss@0.5.5
- pkg:npm/native-component-list@1.0.0
- pkg:npm/node-scoped-http-client@1.0.0
- pkg:npm/node-token@1.0.2
- pkg:npm/non-ember-thingy@1.0.0
- pkg:npm/plywood-clickhouse-requester@1.0.0
- pkg:npm/polaris-charts@1.0.0
- pkg:npm/rnpm-plugin-test@10.0.1
- pkg:npm/string_decoder-browserify@1.0.0
- pkg:npm/worksp@91.0.0
- pkg:npm/workspace-hoist-all@91.0.0
Review-Date: 2021-02-16
Scope: Implementation/Partial
Schema-Version: 1.0
SPDX-License-Identifier: CC-BY-4.0
---

### Summary

This package contains a proof-of-concept for the "[dependency confusion](https://medium.com/@alex.birsan/dependency-confusion-4a5d60fec610)"
vulnerability. Upon installation, it exfiltrates basic information (IP address, hostname, username, local path) to a remote server using DNS.

These packages were removed from the NPM registry on February 17, 2021.

### Details

This package contains a proof-of-concept for the "[dependency confusion](https://medium.com/@alex.birsan/dependency-confusion-4a5d60fec610)"
vulnerability. Upon installation, it exfiltrates basic information (IP address, hostname, username, local path) to a remote server using DNS.

The affected packages appear to target specific organizations as well as more general names like "dep-e" or "fake-d".

### Methodology

We built custom tooling to discover these packages and after manual triage, we reported them to the NPM security team.

### External References

* [Dependency Confusion: How I Hacked Into Apple, Microsoft and Dozens of Other Companies](https://medium.com/@alex.birsan/dependency-confusion-4a5d60fec610)
* [Avoiding npm substitution attacks](https://github.blog/2021-02-12-avoiding-npm-substitution-attacks/)
* [3 Way to Mitigate Risk When Using Private Package Feeds](https://azure.microsoft.com/en-us/resources/3-ways-to-mitigate-risk-using-private-package-feeds/)

### Disclaimer

All security reviews are conducted on a "best-effort" basis against a software
component at a point in time. We make no guarantee as to the quality or completeness
of any review. If you believe any content is inaccurate, we encourage you to open
an issue or submit a pull request with a correction or improvement.

### License

This text is released under at least the
[Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt).
Externally-referenced content may be licensed differently.
