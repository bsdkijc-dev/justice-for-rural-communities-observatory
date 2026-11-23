# Contributing to the Justice for Rural Communities Observatory

Thank you for your interest in contributing to the JRC Observatory.

## Core Principles
1. **Evidence & Provenance First:** Every external fact, statistic, regulation, or institutional claim must include a verified primary source URL, retrieval date, and observation period.
2. **No Fabrication or Silent Imputation:** Never invent data, interviews, citations, or estimates. Leave missing official values empty and document missingness explicitly.
3. **Privacy & Ethics:** Never commit personally identifiable information (PII), unredacted case files, or unapproved survey/interview data.
4. **Publication Gates:** All datasets must be tagged with a publication classification (`P1`–`P5`). Only `P1` and reviewed `P5` (synthetic) files may be proposed for public release, subject to human approval.

## Development Workflow
1. Ensure all JSON schemas in `schemas/` validate cleanly.
2. Run `python3 -m unittest discover -s tests -p "test_*.py" -v` before committing.
3. Document changes in `CHANGELOG.md`.
