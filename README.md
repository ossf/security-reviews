# Open Source Security Reviews

This repository contains a collection of security reviews of open source software. It is a public resource that anyone can contribute to, and is consumable by anyone under a permissive license.

***Note: Do not disclose "new" or "unknown" vulnerabilities to this project or to this repository.***

## How Can I Submit a Security Review?

- [ ] Choose an open source component and complete the form on the [QuickStart](https://ossf.github.io/security-reviews/quickstart.html) page to generate your review (it will be a markdown file).
- [ ] Clone this repository and add your security review to the relevant path in the [reviews](https://github.com/ossf/security-reviews/tree/main/reviews) directory (see [Naming Reviews](#naming-reviews)).
- [ ] Submit a pull request!

## Naming Reviews

The name of a security review should be readable, using hyphen-separated lowercase
letters, and should be placed in the most relevant path in the [reviews](https://github.com/ossf/security-reviews/tree/main/reviews) directory. For example, a security review of Django could be placed in the `pypi/django` path, and a review of Zlib could be placed in the `github/madler/zlib` path. It is likely the relevant path for your security review has not yet been created, as this repository is still a work in progress. If that is the case, please create the relevant path for your review.

If a review reflects multiple projects across different package managers (e.g.
Django exists on both GitHub and PyPI), please file the project in location
users are most likely to look for it (in this case, PyPI). If you get stuck,
feel free to ask in an Issue or Pull Request.

## Removing Reviews

If you believe that a security review is inappropriate, either because
it is giving objectively poor advice, contains an undisclosed security
vulnerability, or similar, please open an Issue or contact [TBD](#).

We reserve the right to remove (or not remove) any content submitted
to this repository.

## Tips

- [ ] Read the [Review Template](template.md) for information on which sections can (and must) be included and suggestions for the level of detail expected.
- [ ] We are working on including a [Video Introduction](#) (may not be uploaded yet) to the project for more information and to learn more about what is expected in a security review.

## Disclosure Policy

This platform is **not** intended to be a vulnerability reporting process, but rather a forum for sharing general security reviews of open source components; if you
discover a vulnerability in an open source software component, we
strongly encourage you to disclose it privately to the author so as
to protect the community.

It is also **not** intended to be a vulnerability disclosure mechanism
(i.e. it isn't an alternative to a CVE). If you are the author of a
component, we encourage you to publicly disclose the vulnerability,
either through the
[GitHub Security Advisory](https://docs.github.com/en/free-pro-team@latest/github/managing-security-vulnerabilities/about-github-security-advisories)
process, requesting a formal CVE yourself, or another appropriate
mechanism.

***For reviews that describe or reference vulnerabilities:***

 * Vulnerabilities must already be disclosed publicly (preferably via a CVE) AND either (a) it must be fixed OR (b) at least 90 days must have passed since it was publicly disclosed.
For reviews that don't describe or reference vulnerabilities, all content should be acceptable.

### Examples

The following examples attempt to illustrate the policy above:

***Acceptable Submissions***

 * Reviewer found no security vulnerabilities in a project.
 * Reviewer found a new vulnerability, reported it to the author, and it was fixed. Note that since it was fixed, it meets the "publicly disclosed" part of the policy above, even though we'd prefer CVEs or another disclosure mechanism to be used and referenced.
 * A vulnerability was reported on Twitter 91 days ago, but the project has not been updated. Note that we'd strongly encourage the submitter to disclose that vulnerability to the project maintainer.
 * Reviewer describes that if a particular configuration setting is used incorrectly, it could open up the user to attack. For example, "Web Server X, by default, provides an index page at /index. You should turn it off by setting NO_INDEX=1 in your server.conf file".
 * Vulnerabilities in transitive dependencies. For example, "Project Foo depends on Project Bar, and Project Bar is vulnerable to CVE-2021-123456."

***Unacceptable Submissions***

 * Reviewer found a vulnerability but did not disclose it to the maintainer.
 * A vulnerability was reported on Twitter 30 days ago and the project has not released a fix yet.

This page cannot account for all possible scenarios; therefore we encourage you to seek guidance by opening an issue (please do not provide specifics), and a maintainer will advise on the most appropriate course.

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
GUID generator is specifically not resistent to prediction, which
could be of help to a developer trying to identify the best tool
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
