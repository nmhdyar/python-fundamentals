# Chapter 01 — Python Foundations

> Status: Paired draft
> Persian edition: [فصل ۰۱ — مبانی پایتون](../../../persian/chapters/01-python-foundations/README.md)

## 1. Overview
This chapter introduces the syntax and core values used in everyday Python programs: variables, built-in types, input/output, conversion, operators, and strings.

## 2. Learning objectives
By the end of this chapter, you should be able to:
- Create variables using clear `snake_case` names.
- Recognize `int`, `float`, `str`, `bool`, and `None` values.
- Read input and format output with `print()` and f-strings.
- Convert input safely to numeric types.
- Use arithmetic, comparison, logical, and assignment operators.
- Index, slice, and use common string methods.

## 3. Prerequisites
No prior Python knowledge is required. Basic computer use and the ability to run a Python file are enough.

## 4. Lessons
| File | Topics |
|---|---|
| [01 — Variables and Data Types](01_variables_and_types.py) | Variables, naming, built-in types, `type()` |
| [02 — Input and Output](02_input_output.py) | `input()`, `print()`, f-strings, `sep`, `end` |
| [03 — Type Conversion](03_type_conversion.py) | `int()`, `float()`, `str()`, boolean conversion |
| [04 — Operators](04_operators.py) | Arithmetic, comparison, logical, assignment, precedence |
| [05 — Strings](05_strings.py) | Indexing, slicing, methods, immutability, formatting |
| [06 — Foundations Practice](06_foundations_exercises.py) | Integrated beginner exercises |

## 5. Worked examples
The lesson files demonstrate profile data, formatted messages, numeric conversion, arithmetic calculations, and string cleanup. Each file is executable on its own.

## 6. Common mistakes
- Treating `input()` as a number without converting it.
- Confusing `=` (assignment) with `==` (comparison).
- Expecting `int("3.5")` to work.
- Forgetting that string indexes start at zero.
- Expecting a string method to modify the original string in place.

## 7. Practice exercises
Complete `CH01-EX01` through `CH01-EX05` in [PRACTICE.md](../../PRACTICE.md).

## 8. Chapter recap
Variables refer to values. Built-in types describe those values. Input and output connect a program to a user. Conversion changes a value's type, operators perform calculations and comparisons, and strings provide tools for working with text.

## 9. Self-check
- [ ] I can explain the difference between a variable and a value.
- [ ] I can identify the main built-in data types.
- [ ] I can convert numeric input before calculating with it.
- [ ] I can format output and use basic string operations.

## 10. Glossary
| Term | Meaning |
|---|---|
| Variable | A name that refers to a value |
| Data type | A category that describes a value and its operations |
| Type conversion | Creating a value of another type |
| Expression | Code that evaluates to a value |
| String | A sequence of text characters |
