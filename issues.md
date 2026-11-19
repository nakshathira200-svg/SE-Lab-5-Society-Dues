# Lab 6 – Static Code Analysis Issues

**Student:** Nakshathira B  
**SRN:** PES2UG24AM096  
**Assignment:** Software Engineering Lab 6 – Society Maintenance Dues Ledger

## Original Analysis

- Pylint score: 5.81/10
- Tools used: Pylint, Flake8 and Bandit

## Identified Issues

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| SQL Injection | Security - Medium | 9 | User-controlled values are inserted directly into an SQL query using an f-string. | Replace string interpolation with parameterized SQL queries. |
| Unsafe eval() | Security - Medium | 21 | eval() executes arbitrary Python expressions and may allow malicious code execution. | Replace eval() with a safe arithmetic expression parser. |
| Mutable Default Argument | Code Quality - Medium | 8 | Using history=[] causes the same list to be shared across function calls. | Use None as the default and initialize a new list inside the function. |
| Broad Exception Handling | Code Quality - Medium | 22 | Catching Exception hides unexpected errors and makes debugging difficult. | Catch specific exceptions and handle invalid input explicitly. |
| Hardcoded Password | Security - Low | 5 | The treasurer password is stored directly in the source code. | Read the password from an environment variable. |
| Incorrect None Comparison | Code Quality - Low | 29 | Comparing the result of fetchall() with None is unnecessary because fetchall() returns a list. | Remove the redundant condition. |
| Formatting Violations | Style - Low | 4, 12, 13, 15 | Long lines and missing blank lines violate Python style conventions. | Apply PEP 8 formatting. |

## Planned Improvements

1. Secure database operations using parameterized SQL.
2. Remove unsafe dynamic expression evaluation.
3. Eliminate mutable default arguments.
4. Improve exception handling.
5. Remove hardcoded credentials.
6. Correct logical and formatting issues.

## Validation

All three static analysis tools will be executed again after fixing the code. Their final results will be compared with the original reports.

## Final Analysis Results

| Tool | Original Result | Final Result |
|---|---|---|
| Pylint | 5.81/10 | 10.00/10 |
| Flake8 | 5 violations | 0 violations |
| Bandit | 3 findings | 0 findings |

## Conclusion

The original program contained security vulnerabilities,
code quality problems and formatting violations.

The issues were addressed using parameterized SQL queries,
safe arithmetic expression evaluation, immutable default
argument handling, specific exception handling and
environment-based credential configuration.

The final program achieved a Pylint score of 10.00/10.
Flake8 reported no violations and Bandit identified no
security issues.

The original program's demonstration output was preserved.
