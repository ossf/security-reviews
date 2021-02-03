#!env python

import os
import datetime
import re
import sys
from typing import List

import yaml
from better_profanity import profanity


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
                if'reviews/README.md' in filename:
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

        with open(filename, 'r') as f:
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
                       'External References', 'Methodology', 'Disclaimer']:
            if f'### {header}' not in sections:
                self.results.append(f'Missing header: {header}')

    def __check_metadata(self, lines):
        metadata_content = []
        in_metadata = False

        for line in lines:
            lstrip = line.strip()
            if lstrip == '<!--':
                in_metadata = True
            elif lstrip == '-->':
                in_metadata = False
                break
            elif in_metadata:
                metadata_content.append(line)
        metadata = yaml.safe_load('\n'.join(metadata_content))

        if 'package-urls' not in metadata or not len(metadata['package-urls']):
            self.results.append("Missing Package URL.")

        access = metadata.get('access')
        if not access:
            self.results.append("Missing access.")
        if access != 'public' and not access.startswith("private/"):
            self.results.append("Invalid access, must be either 'public' or 'private/<name>'")

        if 'author' not in metadata:
            self.results.append("Missing author.")
        
        if 'domain' not in metadata:
            self.results.append("Missing domain.")
        
        methodology_summary = metadata.get('methodology-summary')
        if not methodology_summary:
            self.results.append("Missing methodology-summary.")
        methodology_parts = methodology_summary.split(';')
        for part in methodology_parts:
            if part not in ['static-analysis', 'dynamic-analysis', 'fuzzing', 'code-review', 'web-search', 'project-health']:
                self.result.append("Invalid methodology summary, must be one or more (semicolon-separated) of 'static-analysis', 'dynamic-analysis', 'fuzzing', 'code-review', 'web-search', or 'project-health'.")

        review_date = metadata.get('review-date')
        if not review_date:
            self.results.append("Missing review date.")
        if not isinstance(review_date, datetime.date):
            self.results.append("Invalid review date.")

        if 'opinion' not in metadata:
            self.results.append("Missing opinion.")
        
        publication_state = metadata.get('publication-state')
        if not publication_state:
            self.results.append("Missing publication-state.")
        if publication_state not in ['draft', 'published', 'revoked']:
            self.results.append("Invalid publication-state, must be either 'draft', 'published', or 'revoked'.")

        opinion = metadata.get('opinion')
        if not opinion:
            self.results.append("Missing opinion.")
        if opinion not in ['secure', 'insecure', 'partially-secure', 'no-opinion']:
            self.results.append("Invalid opinion, must be either 'secure', 'insecure', 'partially-secure', or 'no-opinion'.")

        scope = metadata.get('scope')
        if not scope:
            self.results.append("Missing scope.")
        if scope not in ['implementation/full', 'implementation/partial', 'non-implementation']:
            self.results.append("Invalid scope, must be either 'implementation/full', 'implementation/partial', or 'non-implementation'.")

        schema_version = metadata.get('schema-version')
        if not schema_version:
            self.results.append("Missing schema-version.")
        if str(schema_version) != "1.0":
            self.results.append("Invalid schema version.")
        
        severity = metadata.get('severity')
        if not severity:
            self.results.append("Missing severity.")
        if severity not in ['critical', 'important', 'moderate', 'low', 'defense-in-depth', 'not-applicable', 'informational']:
            self.results.append("Invalid severity, must be either 'critical', 'important', 'moderate', 'low', 'defense-in-depth', 'not-applicable', or 'informational'.")
        
        if opinion == 'secure' and severity in ['critical', 'important', 'moderate']:
            self.results.append(f"Opinion is {opinion} but severity is {severity}.")
        if opinion == 'insecure' and severity in ['informational']:
            self.results.append(f"Opinion is {opinion} but severity is {severity}.")

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
