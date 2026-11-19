# SE Lab 5 – Static Code Analysis
## Apartment Society Maintenance Dues Ledger

**Student Name:** Nakshathira B  
**SRN:** PES2UG24AM096  
**Course:** Software Engineering  
**Lab Number:** 5

## 1. Project Overview

This project focuses on analyzing and improving a Python-based apartment society maintenance dues ledger using static code analysis tools.

The application supports:
- Adding monthly maintenance dues.
- Collecting payments.
- Calculating late fees.
- Listing flats with pending payments.

## 2. Tools Used

- Python 3
- Pylint
- Flake8
- Bandit
- SQLite

## 3. Issues Identified

- SQL injection vulnerability.
- Unsafe use of eval().
- Mutable default arguments.
- Broad exception handling.
- Hardcoded credentials.
- PEP 8 formatting violations.
- Missing documentation and inconsistent return statements.

## 4. Improvements Implemented

- Replaced SQL string interpolation with parameterized queries.
- Implemented safe arithmetic expression evaluation using Python AST.
- Replaced mutable default arguments with None.
- Added specific exception handling.
- Replaced hardcoded password with environment-variable configuration.
- Improved naming conventions and formatting.
- Added function and module documentation.
- Added explicit return values.

## 5. Static Analysis Results

| Tool | Before | After |
|---|---:|---:|
| Pylint | 5.81/10 | 10.00/10 |
| Flake8 | 5 violations | 0 violations |
| Bandit | 3 findings | 0 findings |

## 6. Functionality and Security Testing

The corrected application was tested for:
1. Independent history lists.
2. SQL injection protection.
3. Arithmetic evaluation.
4. Rejection of malicious expressions.
5. Payment collection.
6. Pending dues identification.

All six tests passed.

## 7. Program Output

The original demonstration output was preserved:

```text
2500
100
['A-102']
```

## 8. Deliverables

- society_dues.py
- issues.md
- original_output.txt
- final_output.txt
- pylint_before.txt and pylint_after.txt
- flake8_before.txt and flake8_after.txt
- bandit_before.txt and bandit_after.txt

## 9. Conclusion

Static code analysis helped identify security vulnerabilities, programming errors and style violations.

After implementing the improvements, the application achieved a Pylint score of 10.00/10, zero Flake8 violations and zero Bandit findings while preserving its original demonstration functionality.
