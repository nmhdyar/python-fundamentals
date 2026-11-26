# Chapter 02 — Conditions and Loops

> Status: Paired draft  
> Persian edition: [فصل ۰۲ — شرط‌ها و حلقه‌ها](../../../persian/chapters/02-conditions-and-loops/README.md)

## 1. Overview
Learn how programs make decisions, repeat actions, and control the flow inside loops.

## 2. Learning objectives
- Use `if`, `elif`, `else` and Boolean operators.
- Iterate with `for`, `while`, and `range()`.
- Build counters, accumulators, filters, and nested loops.
- Control loop execution with `break` and `continue`.

## 3. Prerequisites
Chapter 01: variables, types, input/output, conversion, operators, and strings.

## 4. Lessons
| File | Topics |
|---|---|
| 01–08 existing lesson files | Conditions, iteration, counters, filters, accumulators, nested loops, patterns |
| [09 — break](09_break_statement.py) | Exit the nearest loop immediately |
| [10 — continue](10_continue_statement.py) | Skip the rest of the current iteration |

## 5. Worked examples
`break` stops the nearest enclosing loop. `continue` skips the remaining statements in the current iteration and proceeds to the next one. Both work in `for` and `while` loops.

## 6. Common mistakes
- Using `break` when only the current iteration should be skipped.
- Using `continue` before updating a `while` loop counter, causing an infinite loop.
- Assuming `break` exits every nested loop; it exits only the nearest loop.

## 7. Practice exercises
Complete `CH02-EX01` through `CH02-EX05` in [PRACTICE.md](../../PRACTICE.md).

## 8. Recap
Conditions select branches; loops repeat work; `break` ends a loop and `continue` skips one iteration.

## 9. Self-check
- [ ] I can choose between `for` and `while`.
- [ ] I can predict the effect of `break` and `continue`.
- [ ] I can trace nested loops and avoid infinite loops.

## 10. Glossary
| Term | Definition |
|---|---|
| Loop control | Statements that change the normal loop flow |
| `break` | Immediately terminates the nearest enclosing loop |
| `continue` | Skips to the next iteration of the nearest enclosing loop |
| Nested loop | A loop inside another loop |
