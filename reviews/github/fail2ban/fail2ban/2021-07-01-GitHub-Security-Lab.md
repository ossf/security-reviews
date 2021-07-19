---
Publication-State: Active
Access: Public
Reviewers:
- Name: Kevin Backhouse
  Email: kevinbackhouse@github.com
  Organization: GitHub
  Associated-With-Project: False
  Compensation-Source: Non-Project
Domain: Security
Methodology:
- Code-Review
- External-Review
Issues-Identified: Non-Severe
Package-URLs:
- pkg:github/fail2ban/fail2ban@0.11.2
Review-Date: 2021-07-01
Scope: Implementation/Full
Schema-Version: 1.0
SPDX-License-Identifier: CC-BY-4.0
---

### Summary

I audited Fail2Ban for vulnerabilities that could be triggered by either a remote or local attacker. I did not find any exploitable issues.

### Details

Fail2ban protects against brute force password-guessing attacks. In its default configuration, it protects OpenSSH, but it includes configurations for other applications such as asterisk, dropbear, and mysql, that are very easy to enable. I have tested and audited the source code of Fail2ban for security vulnerabilities and did not find any serious issues. Fail2ban has a [known problem](https://www.fail2ban.org/wiki/index.php/MANUAL_0_8#Possibility_of_DOS_attack_by_a_local_user) that an unprivileged local user can lock other users out of the system, which may make Fail2ban unsuitable for use on some shared servers. I also found that Fail2ban’s defenses against command injection attacks from a local attacker are not as good as they could be, because they rely on regexes in config files rather than validation in the source code, but I did not find anything that is exploitable in practice.

### Methodology

* Attack surface analysis
* Manual testing of attack surface
* Manual audit of security-sensitive areas of the source code

### External References

https://securitylab.github.com/research/Fail2exploit/

### Disclaimer

All security reviews are conducted on a "best-effort" basis against a software
component at a point in time. We make no guarantee as to the quality or completeness
of any review. If you believe any content is inaccurate, we encourage you to open
an issue or submit a pull request with a correction or improvement.

### License

This text is released under at least the
[Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt).
Externally-referenced content may be licensed differently.
