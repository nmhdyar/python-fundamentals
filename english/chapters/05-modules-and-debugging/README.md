# Chapter 05 — Modules, Exceptions, and Debugging

> Status: Draft — paired English/Persian editions
> Persian edition: [فصل ۰۵ — ماژول‌ها، استثناها و اشکال‌زدایی](../../../persian/chapters/05-modules-and-debugging/README.md)

## 1. Overview
As programs grow, code should be split into focused modules. This chapter also introduces Python's standard library, exception handling, and a repeatable debugging workflow.

## 2. Learning objectives
- Explain what a module is and import it in common ways.
- Protect script entry points with `if __name__ == "__main__":`.
- Use selected standard-library modules.
- Recognize syntax errors and runtime exceptions.
- Handle expected failures with specific exception types.
- Raise exceptions when a function receives invalid input.
- Describe a basic package and virtual environment workflow.
- Debug by reproducing, isolating, inspecting, and verifying a problem.

## 3. Prerequisites
Chapters 01–04: core syntax, collections, functions, and basic file/path familiarity.

## 4. Lessons
| File | Topics |
|---|---|
| [01 — Modules and Imports](01_modules_and_imports.py) | Imports, aliases, module namespace, main guard |
| [02 — Standard Library](02_standard_library.py) | `math`, `random`, `datetime`, `pathlib` |
| [03 — Understanding Exceptions](03_exceptions_basics.py) | Syntax errors, runtime exceptions, common exception types |
| [04 — Handling Exceptions](04_exception_handling.py) | `try`, specific `except`, `else`, `finally` |
| [05 — Raising Exceptions](05_raising_custom_exceptions.py) | `raise`, validation, custom exception classes |
| [06 — Debugging and Environments](06_debugging_and_environments.py) | Tracebacks, debugging workflow, `pip`, `venv` |

## 5. Worked examples
Examples show importing a module, using standard-library helpers, handling conversion errors, validating a quantity, and creating an isolated project environment.

## 6. Common mistakes
- Naming a file after a standard-library module such as `random.py`.
- Using `except:` without an exception type.
- Catching an exception and silently ignoring it.
- Using exceptions for ordinary control flow.
- Forgetting that `finally` runs whether or not an exception occurred.
- Installing packages globally when a project environment should be used.

## 7. Practice
Complete `CH05-EX01` through `CH05-EX05` in the repository practice file.

## 8. Recap
Modules organize code; the standard library provides reusable tools; exceptions report errors; handlers let a program respond to expected failures. Debugging is a disciplined process, not random code editing.

## 9. Self-check
- [ ] I can import a module and explain the main guard.
- [ ] I can handle a specific exception without hiding unrelated bugs.
- [ ] I can validate input and raise a meaningful exception.
- [ ] I can create and activate a virtual environment.

## 10. Glossary
| Term | Meaning |
|---|---|
| Module | A Python file that can be imported |
| Package | A way to organize related modules |
| Exception | An object representing an error during execution |
| Traceback | The call history shown when an exception is unhandled |
| Debugging | Finding and correcting the cause of a problem |
| Virtual environment | An isolated Python environment for a project |
