# Chapter 08 — Testing & Code Quality

> Status: Paired draft  
> Persian edition: [فصل 08 — تست و کیفیت کد](../../../persian/chapters/08-testing-and-code-quality/README.md)

## 1. Overview
Design repeatable tests, cover edge cases, and improve code without changing its behavior.

## 2. Learning objectives
By the end of this chapter, you can:
- Explain the concepts below and identify when they are useful.
- Implement the patterns in small, executable Python programs.
- Choose a clear solution and explain its trade-offs.
- Test normal, boundary, and invalid cases.

## 3. Prerequisites
Chapters 01–07; functions, exceptions, modules, and basic project structure.

## 4. Lessons
1. Why automated tests matter
2. Assertions and expected behavior
3. Unit tests and test cases
4. Arrange–Act–Assert pattern
5. `unittest` and test discovery
6. Introduction to `pytest` and fixtures
7. Edge cases and invalid input
8. Test doubles and isolation basics
9. Test-driven development cycle
10. Refactoring and readable code

### Runnable lesson files
| File | Focus |
|---|---|
| [01_unittest_basics.py](01_unittest_basics.py) | Run a small unittest suite covering normal and invalid cases. |
| [02_testable_design.py](02_testable_design.py) | Separate pure calculation logic from side effects and test edge cases. |

## 5. Worked examples
The lesson scripts are executable worked examples. Trace each statement, predict its output before running it, then change one input or design choice and compare the result.

## 6. Common mistakes
- Testing only the happy path; tests that depend on execution order; assertions that merely repeat implementation details; changing behavior during refactoring.
- Copying a pattern without understanding its contract or side effects.
- Skipping validation and boundary cases.

## 7. Practice exercises
Complete CH08-EX01, CH08-EX02, CH08-EX03, CH08-EX04, CH08-EX05 in [PRACTICE.md](../../PRACTICE.md).

**Chapter project:** Write a tested expense calculator with normal, boundary, and invalid-input cases; keep business logic separate from input/output.

## 8. Recap
Review the lesson list and explain the key idea of each lesson in your own words. Re-run the examples after changing their data or assumptions.

## 9. Self-check
- [ ] I can explain the chapter's core vocabulary.
- [ ] I can write a small example without copying the lesson.
- [ ] I can identify at least two common failure cases.
- [ ] I can explain why my solution is appropriate.

## 10. Glossary
| English term | Definition |
|---|---|
| Testing | The central topic of this chapter. |
| Implementation | A concrete way of expressing an idea in code. |
| Edge case | An unusual but valid or important input condition. |
| Trade-off | A design choice that improves one quality while affecting another. |
