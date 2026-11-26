# Chapter 02 — Conditions and Loops

> Status: Paired draft
> Persian edition: [فصل ۰۲ — شرط‌ها و حلقه‌ها](../../../persian/chapters/02-conditions-and-loops/README.md)

## 1. Overview
This chapter explains how programs choose between alternatives and repeat actions. Conditions and loops let a program respond to data instead of following only a fixed sequence.

## 2. Learning objectives
- Control branches with `if`, `elif`, and `else`.
- Combine conditions with `and`, `or`, and `not`.
- Iterate with `for` and `range()`.
- Use `while` with a clear stopping condition.
- Build counters, accumulators, and filters.
- Use nested loops for simple patterns and grids.

## 3. Prerequisites
Chapter 01: variables, data types, input/output, conversion, operators, and strings.

## 4. Lessons
| File | Topics |
|---|---|
| [01 — Conditional Statements](01_conditional_statements.py) | `if`, `elif`, `else`, comparison, validation |
| [02 — For Loop Iteration](02_for_loop_iteration.py) | Iterables, lists, `range()` |
| [03 — While Loop Counter](03_while_loop_counter.py) | Conditions, counters, termination |
| [04 — Filtering Even Numbers](04_filter_even_numbers.py) | Modulo, filtering, `range()` |
| [05 — Combining Conditions](05_combining_conditions.py) | `and`, `or`, compound conditions |
| [06 — Accumulating a Sum](06_accumulating_a_sum.py) | Accumulators and running totals |
| [07 — Nested Loop Rectangle](07_nested_loop_rectangle.py) | Nested loops, rows, columns |
| [08 — Checkerboard Pattern](08_checkerboard_pattern.py) | Nested loops, indexes, conditional output |

## 5. Worked examples
Examples cover age-based decisions, iterating over values, retry counters, filtering even numbers, running totals, and printing rectangular patterns.

## 6. Common mistakes
- Using `=` instead of `==` in a condition.
- Forgetting to update a `while` loop variable.
- Expecting `range()` to include its stop value.
- Misplacing indentation inside branches or nested loops.
- Confusing a counter with an accumulator.

## 7. Practice exercises
Complete `CH02-EX01` through `CH02-EX05` in [PRACTICE.md](../../PRACTICE.md).

## 8. Chapter recap
A condition selects a branch. A loop repeats a block. `for` is useful for iterating over an iterable, while `while` repeats as long as its condition remains true. Counters track occurrences; accumulators combine values.

## 9. Self-check
- [ ] I can trace which branch will execute.
- [ ] I can choose between `for` and `while`.
- [ ] I can explain why a loop stops.
- [ ] I can trace a counter and an accumulator through a loop.

## 10. Glossary
| Term | Meaning |
|---|---|
| Condition | An expression evaluated as true or false |
| Iteration | One repetition of a loop |
| Iterable | An object that can provide its elements one by one |
| Counter | A variable that tracks a number of occurrences |
| Accumulator | A variable that collects a running result |
| Nested loop | A loop placed inside another loop |
