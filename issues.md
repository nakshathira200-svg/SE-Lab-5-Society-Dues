# Lab 5 – Static Code Analysis Issues

**Student:** Nakshathira B  
**SRN:** PES2UG24AM096  
**Assignment:** Software Engineering Lab 5 – Society Maintenance Dues Ledger

## 1. Original Analysis

- Pylint score: 5.81/10
- Tools used: Pylint, Flake8 and Bandit

## 2. Identified Issues and Fixes

| Issue | Type | Description | Fix Implemented |
|---|---|---|---|
| SQL Injection | Security - Medium | User-controlled values were inserted into SQL queries using string interpolation. | Replaced interpolation with parameterized SQL queries. |
| Unsafe eval() | Security - Medium | eval() could execute arbitrary Python expressions. | Implemented safe arithmetic evaluation using Python AST. |
| Mutable Default Argument | Code Quality - Medium | A shared history=[] default could retain values across function calls. | Used None and initialized a new list inside the function. |
| Broad Exception Handling | Code Quality - Medium | Catching Exception could hide unexpected errors. | Replaced it with specific exception handling. |
| Hardcoded Password | Security - Low | An unused password-like constant was stored in the source code. | Removed the unused constant. |
| Incorrect None Comparison | Code Quality - Low | fetchall() returns a list, so comparing its result with None was unnecessary. | Removed the redundant comparison. |
| Formatting Violations | Style - Low | Blank-line and formatting violations did not follow PEP 8. | Corrected formatting and verified with Flake8. |

## 3. Improvements Implemented

1. Secured database operations using parameterized SQL.
2. Replaced unsafe dynamic expression evaluation with AST-based arithmetic evaluation.
3. Eliminated mutable default arguments.
4. Improved exception handling.
5. Removed the unused hardcoded password constant.
6. Corrected formatting and naming conventions.
7. Added documentation and explicit return values.

## 4. Final Static Analysis Results

| Tool | Original Result | Final Result |
|---|---:|---:|
| Pylint | 5.81/10 | 10.00/10 |
| Flake8 | 5 violations | 0 violations |
| Bandit | 3 findings | 0 findings |

## 5. Functionality and Security Testing

Six unit tests were executed successfully:

1. Independent history lists.
2. SQL injection protection.
3. Valid arithmetic evaluation.
4. Rejection of malicious expressions.
5. Payment collection.
6. Pending dues identification.

**Result: 6 tests passed.**

## 6. Program Output

The original demonstration output was preserved:

```text
2500
100
['A-102']




## 7. Conclusion

Static code analysis identified security vulnerabilities, code quality problems and formatting violations in the original program.

The issues were addressed using parameterized SQL queries, safe arithmetic expression evaluation, proper default argument handling, specific exception handling and PEP 8 formatting.

The final program achieved a Pylint score of 10.00/10, zero Flake8 violations and zero Bandit findings. All six unit tests passed, and the original demonstration output was preserved.
