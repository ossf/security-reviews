# Security Reviews

This repository contains a collection of security reviews performed
against open source components. It is intended to be a public resource,
consumable by anyone under a permissive license, and one that anyone
can contribute to.

It is **not** intended to be a vulnerability reporting process; if you
discover a vulnerability in an open source software component, we
strongly encourage you to disclose it privately to the author so as
to protect the community.

It is **not** intended to be a vulnerability disclosure mechanism
(i.e. it isn't an alternative to a CVE). If you are the author of a
component, we encourage you to publicly disclose the vulnerability,
either through the
[GitHub Security Advisory](https://docs.github.com/en/free-pro-team@latest/github/managing-security-vulnerabilities/about-github-security-advisories)
process, requesting a formal CVE yourself, or another appropriate
mechanism.

To be clear:

**Do not disclose "new" or "unknown" vulnerabilities to this project or to this repository.**

## Motivation

There are two main motivations that led to this project.

First, we weren't aware of any public resources that gave **positive indicators**
about the security quality of open source components. If three
organizations were all using the same component, they would consider
reviewing the component in some way, wasting effort that could
be better directed at other components.

Second, the safety of a component is more than a simple "lack of
vulnerabilities". Consider the case of a GUID generator that uses a
strong cryptographic function and the current time as part of its
algorithm. It's debatable whether this type of design should
be considered a vulnerability (as randomness isn't essential when
generating GUIDs), but in many cases, developers implicitly
assume that an attacker cannot guess what GUID will be generated.
In this regard, a security review could state that the 
GUID generator is specifically not resistent to prediction, and
would be of help to a developer trying to identify the best tool
for the job.

## Objective

The primary objective of this project is to collect and curate
security reviews performed against open source software components,
and to make these freely available to stakeholders.

## Scope

The scope of this project includes any software that is distributed
under an [open source](https://opensource.org/licenses) license.

## Prior Work

There are many tangentially-related projects (the NIST CVE database,
GitHub Security Advisories, commercial vulnerability databases), and
many security researchers make available their own security assessments,
but to the best of our knowledge, this project is somewhat unique
in its purpose and approach.

## Get Involved

### Adding/Updating a Security Review

- [ ] Watch the [video introduction](#) to the project for more information
      and to learn more about what is expected in a security review.
- [ ] Review the [review template](template.md) file for information on
      which sections can (and must) be included and suggestions for the
      level of detail expected. You can also use the [QuickStart](quickstart.html)
      page to generate a markdown file using a simple HTML form.
- [ ] Choose an open source component and conduct the security review.
- [ ] Clone this repository and add your security review to the relevant path.
- [ ] Submit a pull request.

### Naming a Security Review

The name of a security review should be readable, using hyphen-separated lowercase
letters, and should be placed in the most relevant path. For example, a security
review of Zlib could be placed in the `github/madler/zlib` path, and a review of
Django could be placed in the `pypi/django` path.

If a review reflects multiple projects across different package managers (e.g.
Django exists on both GitHub and PyPI), please file the project in location
users are most likely to look for it (in this case, PyPI). If you get stuck,
feel free to ask in an Issue or Pull Request.

### Removing a Security Review

If you believe that a security review is inappropriate, either because
it is giving objectively poor advice, contains an undisclosed security
vulnerability, or similar, please open an Issue or contact [TBD](#).

We reserve the right to remove (or not remove) any content submitted
to this repository.

## Licenses

All reviews here are under a permissive license.
Unless stated otherwise, documentation is released under the
[Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt),
while code is released under the Apache license 2.0 (Apache-2.0).
The documentation may link to other materials; those other materials retain
their licenses.

## More Information

For more information on this project and the Open Source Security
Foundation, please visit https://openssf.org.
