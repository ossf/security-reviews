## Front Metadata

```
{
	"Publication-State": "active",
	"Reviewers": [
		{
			"Name": "Michael Scovetta" (Optional, Pseudonym/Handle OK)
			"Email": "michael.scovetta@microsoft.com", (Optional)
			"Organization": "Microsoft", (Optional)
			"Associated-With-Project": [true | false],
			"Compensation-Source": ["project" | "non-project" | "external" | "undisclosed" | "none"]
		}
	],
	"Domain": "Security",
	"Methodology": [  (Choose all that apply))
		"Static-Analysis",
		"Code-Review",
		"Threat-Model",
		"Web-Search",
		"Fuzzing"
		"External-Review"
	],
	"Issues-Identified": [ (Choose one)
		"Severe",
		"Non-Severe",
		"None",
		"Not-Examined"
	]
	"Package-URLs": [ (Multiple OK, but no wildcards)
		"<PACKAGE URL>"
	],
	"Date-Reviewed": "<YYYY-MM-DD>",
	"Scope": "[Implementation/Full | Implementation/Partial | Non-Implementation]" (Choose one)
	"Schema-Version": "1.0",
	"SPDX-License-Identifier": "CC-BY-4.0"
}
```

### Summary

<!-- [Required]
	Add a summary of the review. It can be as simple as,
	"There were no notable findings." This section should be
	no more than one short paragraph.
-->

### Details

<!-- [Optional]
	Use this section to describe any findings and to provide
	additional information. It can be as long as you'd like.
	If a threat model or assumed context is relevant, feel free
	to include it here.
-->

### Methodology

<!-- [Required]
	This section describes what was actually done when performing
	the review.
-->

### External References

<!-- [Optional]
	If the security review was conducted by a third-party or published
	at an external location, include a reference to that assessment. You
	can also reference external URLs for any other purpose.
-->

### Disclaimer

All security reviews are conducted on a "best-effort" basis against a software
component at a point in time. We make no guarantee as to the quality or completeness
of any review. If you believe any content is inaccurate, we encourage you to open
an issue or submit a pull request with a correction or improvement.

### License

This text is released under at least the
[Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt).
Externally-referenced content may be licensed differently.
