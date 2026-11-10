# Chapter 02 — Conditions and Loops

This chapter teaches how a program makes decisions and repeats work. These ideas are the foundation of almost every useful program.

## Learning objectives

By the end of this chapter, you should be able to:

- Control program flow with `if`, `elif`, and `else`.
- Compare values and combine conditions with `and`, `or`, and `not`.
- Iterate over sequences and numeric ranges with `for`.
- Repeat work with `while` and explain its stopping condition.
- Use counters, accumulators, and the modulo operator.
- Build nested loops to produce simple text patterns.

## Lessons

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

## Important concepts

### Conditions
A condition evaluates to `True` or `False`. Python checks branches from top to bottom and runs the first matching branch.

### for vs. while
- Use `for` when iterating over a known sequence or range.
- Use `while` when repetition depends on a condition that may change during execution.

### range()
`range(start, stop, step)` generates integers. The `stop` value is excluded.

### Counters and accumulators
A **counter** tracks occurrences. An **accumulator** collects a result, such as a running sum. Initialize both before the loop.

### Nested loops
The inner loop completes all its iterations for each single iteration of the outer loop.

## Common mistakes

- Using `=` instead of `==` in a comparison.
- Forgetting to update a `while` loop counter, causing an infinite loop.
- Expecting `range()` to include its stop value.
- Incorrect indentation around branches or nested loops.
- Confusing row indexes with column indexes.

## Study workflow

1. Read the explanation at the top of each Python file.
2. Predict the output before running the examples.
3. Run the file, then change values and predict again.
4. Trace at least one loop manually.
5. Complete the five Chapter 02 problems in the repository's [practice file](../../PRACTICE.md) without copying lesson code.

> Do not memorize loop syntax only. Learn to trace the state of each variable as the program runs.
