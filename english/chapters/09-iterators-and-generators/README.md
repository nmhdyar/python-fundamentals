# Chapter 09 — Iterators & Generators

> Status: Paired draft  
> Persian edition: [فصل 09 — ایتراتورها و ژنراتورها](../../../persian/chapters/09-iterators-and-generators/README.md)

## 1. Overview
Understand Python's iteration protocol and produce values lazily when that is more efficient.

## 2. Learning objectives
By the end of this chapter, you can:
- Explain the concepts below and identify when they are useful.
- Implement the patterns in small, executable Python programs.
- Choose a clear solution and explain its trade-offs.
- Test normal, boundary, and invalid cases.

## 3. Prerequisites
Chapters 01–08; loops, functions, exceptions, and basic testing.

## 4. Lessons
1. Iterable, iterator, and iteration protocol
2. `iter()` and `next()`
3. StopIteration
4. Building a custom iterator
5. Generator functions and `yield`
6. Generator expressions
7. Lazy evaluation
8. Streaming large inputs
9. When a list is simpler than a generator

### Runnable lesson files
| File | Focus |
|---|---|
| [01_iterator_protocol.py](01_iterator_protocol.py) | Implement a small iterator and inspect how iter and next work. |
| [02_generators_and_streams.py](02_generators_and_streams.py) | Use a generator pipeline to transform values without building intermediate lists. |

## 5. Worked examples
The lesson scripts are executable worked examples. Trace each statement, predict its output before running it, then change one input or design choice and compare the result.

## 6. Common mistakes
- Expecting a generator to restart after exhaustion; confusing `return` with `yield`; materializing a huge stream unnecessarily.
- Copying a pattern without understanding its contract or side effects.
- Skipping validation and boundary cases.

## 7. Practice exercises
Complete CH09-EX01, CH09-EX02, CH09-EX03, CH09-EX04, CH09-EX05 in [PRACTICE.md](../../PRACTICE.md).

**Chapter project:** Build a generator that streams cleaned transaction records and yields only records matching a filter.

## 8. Chapter recap
Review the lesson list and explain the key idea of each lesson in your own words. Re-run the examples after changing their data or assumptions.

## 9. Self-check
- [ ] I can explain the chapter's core vocabulary.
- [ ] I can write a small example without copying the lesson.
- [ ] I can identify at least two common failure cases.
- [ ] I can explain why my solution is appropriate.

## 10. Glossary
| English term | Definition |
|---|---|
| Iterators | The central topic of this chapter. |
| Implementation | A concrete way of expressing an idea in code. |
| Edge case | An unusual but valid or important input condition. |
| Trade-off | A design choice that improves one quality while affecting another. |
