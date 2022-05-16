#!env python

import os
import datetime
import re
import sys
from typing import List

import yaml
from better_profanity import profanity

IS_PUBLIC_REPOSITORY = True

class SecurityReviewValidator:
    results = None
    warn_results = None

    def __init__(self):
        profanity.load_censor_words(whitelist_words=['strip'])

    def validate_path(self, path: str) -> List[str]:
        results = []
        warn_results = []
        for root, _, files in os.walk(path, topdown=False):
            for name in files:
                filename  = os.path.join(root, name)
                if 'reviews/README.md' in filename:
                    continue   # Ignore this one
                (_results, _warn_results) = self.validate_file(filename)
                for result in _results:
                    results.append(f"{filename}: {result}")
                for result in _warn_results:
                    warn_results.append(f"{filename}: {result}")

        return (results, warn_results)

    def validate_file(self, filename: str) -> List[str]:
        self.results = []
        self.warn_results = []

        if not os.path.isfile(filename):
            self.results.append('File does not exist.')
            return self.results

        with open(filename, 'r', encoding='utf-8') as f:
            if not f.readable():
                self.results.append('Unable to read from file.')
                return self.results
            content = f.read()
            lines = content.splitlines()

        self.__check_profanity(content)
        self.__check_required_headers(lines)
        self.__check_metadata(lines)

        return (self.results, self.warn_results)

    def __check_profanity(self, content):
        profanity.load_censor_words(whitelist_words=['len'])
        if profanity.contains_profanity(content):
            censored_lines = profanity.censor(content).splitlines()
            content_lines = content.splitlines()
            if len(censored_lines) != len(content_lines):
                self.warn_results.append("Contains profanity.")
            else:
                for idx in range(0, len(content_lines)):
                    if content_lines[idx] != censored_lines[idx]:
                        if content_lines[idx].startswith('- "pkg:'):
                            continue
                        self.warn_results.append(f"Contains profanity in line #{idx}: [{censored_lines[idx]}]")
        return

    def __check_required_headers(self, lines):
        sections = list(map(str.strip, filter(lambda s: s.startswith('### '), lines)))

        for header in ['Summary', 'Details',
                       'External References', 'Methodology', 'License', 'Disclaimer']:
            if f'### {header}' not in sections:
                self.results.append(f'Missing header: {header}')

    def __check_metadata(self, lines):
        metadata_content = []
        section = 0
        for line in lines:
            lstrip = line.strip()
            if section == 0 and lstrip == '---':
                section = 1
            elif section == 1 and lstrip == '---':
                break
            elif section == 1:
                metadata_content.append(line)

        metadata = yaml.safe_load('\n'.join(metadata_content))

        if 'Package-URLs' not in metadata or not len(metadata['Package-URLs']):
            self.results.append("Missing Package URL.")

        access = metadata.get('Access')
        if not access:
            self.results.append("Missing access.")
        if access != 'Public' and not access.startswith("Private/"):
            self.results.append("Invalid access, must be either 'Public' or 'Private/<name>'")

        # For GitHub
        if IS_PUBLIC_REPOSITORY:
            if access.startswith("Private/"):
                self.results.append("Invalid access, all reviews must be Public.")

        for reviewer in metadata.get('Reviewers'):
            for key, value in reviewer.items():
                if key not in ['Name', 'Email', 'Organization', 'Associated-With-Project', 'Compensation-Source']:
                    self.results.append(f"Unexpected reviewer property ({key}).")
                #if not isinstance(value, str):
                #    self.results.append(f"Unexpected reviewer value ({value}), string expected.")

        if 'Domain' not in metadata:
            self.results.append("Missing domain.")
        if metadata['Domain'] != 'Security':
            self.results.append("Invalid domain.")

        methodology_parts = metadata.get('Methodology')
        if not methodology_parts or not isinstance(methodology_parts, list):
            self.results.append("Missing Methodology.")
        else:
            for methodology_part in methodology_parts:
                if methodology_part not in ['Static-Analysis', 'Dynamic-Analysis', 'Fuzzing', 'Code-Review', 'Web-Search', 'External-Review']:
                    self.results.append("Invalid methodology element.")

        review_date = metadata.get('Review-Date')
        if not review_date:
            self.results.append("Missing review date.")
        if not isinstance(review_date, datetime.date):
            self.results.append("Invalid review date.")
        if isinstance(review_date, datetime.date) and review_date > datetime.date.today():
            self.results.append("Invalid review date (in the future).")

        publication_state = metadata.get('Publication-State')
        if not publication_state:
            self.results.append("Missing Publication-State.")
        if publication_state not in ['Active', 'Draft', 'Removed']:
            self.results.append("Invalid Publication-State.")

        issues = metadata.get('Issues-Identified')
        if not issues:
            self.results.append("Missing Issues-Identified.")
        if issues not in ['Severe', 'Non-Severe', 'None', 'Not-Examined']:
            self.results.append("Invalid Issues-Identified value.")

        scope = metadata.get('Scope')
        if not scope:
            self.results.append("Missing Scope.")
        if scope not in ['Implementation/Full', 'Implementation/Partial', 'Non-Implementation']:
            self.results.append("Invalid scope.")

        schema_version = metadata.get('Schema-Version')
        if not schema_version:
            self.results.append("Missing Schema-Version.")
        if str(schema_version) != "1.0":
            self.results.append("Invalid Schema-Version.")

        spdx = metadata.get("SPDX-License-Identifier")
        if not spdx or spdx not in ["CC-BY-4.0"]:
            self.results.append(f"SPDX-License-Identifier is not CC-BY-4.0")

if __name__ == '__main__':
    validator = SecurityReviewValidator()
    if len(sys.argv) == 2:
        path = sys.argv[1]
        if os.path.isdir(path):
            (results, warn_results) = validator.validate_path(path)
        else:
            (results, warn_results) = validator.validate_file(path)
    else:
        (results, warn_results) = validator.validate_path('reviews')

    errcode = 0
    if results:
        for result in results:
            print(f'Error: {result}', flush=True)
        errcode = 1

    if warn_results:
        for result in warn_results:
            print(f' Warn: {result}', flush=True)

    if not results and not warn_results:
        print("OK", flush=True)
    sys.exit(errcode)
