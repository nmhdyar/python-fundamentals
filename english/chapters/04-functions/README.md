# Chapter 04 — Functions

> Status: Draft — paired English/Persian editions
> Persian edition: [فصل ۰۴ — توابع](../../../persian/chapters/04-functions/README.md)

## 1. Overview
Functions package reusable behavior behind a clear interface. This chapter moves from simple functions to flexible arguments, scope, lambda expressions, and recursion.

## 2. Learning objectives
- Define and call functions.
- Distinguish parameters from arguments.
- Return values and avoid confusing `print()` with `return`.
- Use default and keyword arguments.
- Accept variable numbers of positional and keyword arguments.
- Explain local and global scope.
- Write small lambda expressions and understand basic recursion.
- Add useful docstrings and type hints.

## 3. Prerequisites
Chapters 01–03: variables, conditions, loops, strings, and data structures.

## 4. Lessons
| File | Topics |
|---|---|
| [01 — Defining Functions](01_defining_functions.py) | `def`, calling, reusable blocks, `pass` |
| [02 — Parameters and Return](02_parameters_and_return.py) | Parameters, arguments, return, early return |
| [03 — Default and Keyword Arguments](03_default_and_keyword_arguments.py) | Defaults, keyword calls, safe defaults |
| [04 — `*args` and `**kwargs`](04_args_and_kwargs.py) | Variable positional and keyword arguments, unpacking |
| [05 — Scope and Lambda](05_scope_and_lambda.py) | Local/global scope, lambda, sorting keys |
| [06 — Recursion and Docstrings](06_recursion_and_docstrings.py) | Base cases, recursive calls, documentation, annotations |

## 5. Worked examples
Examples include reusable greetings, price calculations, configurable messages, flexible summaries, sorting records, and recursive countdown/factorial functions.

## 6. Common mistakes
- Forgetting to call a function with parentheses.
- Expecting `print()` to provide a reusable return value.
- Using a mutable object as a default argument.
- Changing global state when a local variable is enough.
- Writing recursion without a base case.
- Adding too many parameters instead of designing a clear interface.

## 7. Practice
Complete `CH04-EX01` through `CH04-EX05` in the repository practice file.

## 8. Recap
A function has a name, optional parameters, a body, and optionally a return value. Prefer small functions with clear inputs and outputs. Use flexible arguments only when they improve the interface.

## 9. Self-check
- [ ] I can write a function that returns a value.
- [ ] I can explain the difference between a parameter and an argument.
- [ ] I can choose a safe default value.
- [ ] I understand local scope and recursion's base case.

## 10. Glossary
| Term | Meaning |
|---|---|
| Function | Reusable block of code |
| Parameter | Name in a function definition |
| Argument | Value supplied when calling a function |
| Return value | Result sent back to the caller |
| Scope | Region where a name can be accessed |
| Recursion | A function calling itself |
