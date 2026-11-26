# Chapter 10 — Advanced Python Concepts

> Status: Paired draft  
> Persian edition: [فصل 10 — مفاهیم پیشرفته پایتون](../../../persian/chapters/10-advanced-python-concepts/README.md)

## 1. Overview
Use advanced language features deliberately to reduce repetition and express clear object behavior.

## 2. Learning objectives
By the end of this chapter, you can:
- Explain the concepts below and identify when they are useful.
- Implement the patterns in small, executable Python programs.
- Choose a clear solution and explain its trade-offs.
- Test normal, boundary, and invalid cases.

## 3. Prerequisites
Chapters 01–09; functions, OOP, iterators, exceptions, and modules.

## 4. Lessons
1. Closures and enclosing scope
2. Decorators and wrapper functions
3. Preserving metadata with `functools.wraps`
4. Parameterized decorators
5. Context manager protocol
6. `contextlib.contextmanager`
7. Properties and controlled attributes
8. Dataclasses and generated methods
9. Choosing simple alternatives over clever abstractions

### Runnable lesson files
| File | Focus |
|---|---|
| [01_closures_and_decorators.py](01_closures_and_decorators.py) | Create a reusable decorator that measures calls while preserving function metadata. |
| [02_context_managers_and_dataclasses.py](02_context_managers_and_dataclasses.py) | Use a dataclass and a context manager to model temporary configuration. |

## 5. Worked examples
The lesson scripts are executable worked examples. Trace each statement, predict its output before running it, then change one input or design choice and compare the result.

## 6. Common mistakes
- Forgetting to return the wrapped function's result; losing metadata; hiding side effects in decorators; using dataclasses when custom invariants need explicit logic.
- Copying a pattern without understanding its contract or side effects.
- Skipping validation and boundary cases.

## 7. Practice exercises
Complete CH10-EX01, CH10-EX02, CH10-EX03, CH10-EX04, CH10-EX05 in [PRACTICE.md](../../PRACTICE.md).

**Chapter project:** Build a small timing decorator, a safe temporary setting context manager, and a dataclass model.

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
| Advanced | The central topic of this chapter. |
| Implementation | A concrete way of expressing an idea in code. |
| Edge case | An unusual but valid or important input condition. |
| Trade-off | A design choice that improves one quality while affecting another. |
