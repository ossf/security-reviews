# Security Reviews

This repository contains a collection of security reviews performed
against open source components. It is intended to be a public resource,
consumable by anyone under a permissive license, and one that anyone
can contribute to.

It is **not** intended to be a vulnerability reporting process; if you
discover a vulnerability in an open source software component, we
strongly encourage you to disclose it privately to the author.

It is also **not** intended to be a vulnerability disclosure mechanism
(i.e. it isn't an alternative to a CVE). If you are the author of a
component, we encourage you to publicly dislcosure, either through the
[GitHub Security Advisory](https://docs.github.com/en/free-pro-team@latest/github/managing-security-vulnerabilities/about-github-security-advisories)
process or something similar.

To be clear:

**Please do not disclose "new" vulnerabilities on this repository.**

## Motivation

There are two main motivations that led to this project.

First, we weren't aware of any public resources that gave positive
indicators about the security of open source components. If three
organizations were all using the same component, they would each be
led to review the component in some way, wasting effort that could
be better directed at other components.

Second, the safefty of a component is more than just "lack of
vulnerability". Consider the case of a UUID generator that uses a
strong cryptographic function and the current time as part of its
algorithm. It's debatable whether this type of design should
be considered a vulnerability (as randomness isn't essential when
generating UUIDs), but in many cases, developers implicitly
assume that an attacker cannot guess what UUID was or will be
generated. In this regard, a security review could state that the 
UUID generator is specifically not resistent to prediction, and
would be of help to a developer trying to identify the best tool
for the job.

## Objective

The primary objective of this project is to collect and curate
security reviews performed against open source software components,
and to make these freely available to stakeholders.

## Scope

Any sofware component distributed under and open source license.

## Prior Work

There are many tangentially-related projects (the NIST CVE database,
GitHub Security Advisories, commercial vulnerability databases), but
to the best of our knowledge, nothing that quite overlaps with the
purpose of this project.

## Get Involved

### Adding/Updating a Security Review

- [ ] Review the [review template](template.md) file for information on
      which sections to include and the type of information required for
      a review to be accepted.
- [ ] Conduct the security review.    
- [ ] Clone this repository and add your security review in the relevant
      path.
- [ ] Submit a pull request.

### Removing a Security Review

If you believe that a security review is inappropriate, either because
it is giving objectively poor advice, contains an undisclosed security
vulnerability, or similar, please open an issue.

We reserve the right to remove (or not remove) any content submitted
to this repository.

## More Information

For more information on this project and the Open Source Security
Foundation, please visit https://openssf.org.