# Chapter 11 — Project Structure & Packaging

> Status: Paired draft  
> Persian edition: [فصل 11 — ساختار پروژه و بسته‌بندی](../../../persian/chapters/11-project-structure-and-packaging/README.md)

## 1. Overview
Organize multi-module applications, manage dependencies, and prepare projects for reliable reuse.

## 2. Learning objectives
By the end of this chapter, you can:
- Explain the concepts below and identify when they are useful.
- Implement the patterns in small, executable Python programs.
- Choose a clear solution and explain its trade-offs.
- Test normal, boundary, and invalid cases.

## 3. Prerequisites
Chapters 01–10; imports, virtual environments, OOP, testing, and file handling.

## 4. Lessons
1. Project layout and separation of concerns
2. Packages and `__init__.py`
3. Absolute and relative imports
4. Virtual environments and dependency isolation
5. `requirements.txt` and pinned versions
6. `pyproject.toml` overview
7. Logging levels and handlers
8. Configuration and environment variables
9. Entry points and command-line basics
10. Packaging and distribution concepts

### Runnable lesson files
| File | Focus |
|---|---|
| [01_logging_and_configuration.py](01_logging_and_configuration.py) | Configure logging and read an optional setting from the environment with a safe default. |
| [02_package_layout_demo.py](02_package_layout_demo.py) | Inspect a recommended src/tests project layout and explain each responsibility. |

## 5. Worked examples
The lesson scripts are executable worked examples. Trace each statement, predict its output before running it, then change one input or design choice and compare the result.

## 6. Common mistakes
- Using one giant module; committing secrets; installing packages globally; logging secrets or swallowing exceptions; confusing source layout with distribution metadata.
- Copying a pattern without understanding its contract or side effects.
- Skipping validation and boundary cases.

## 7. Practice exercises
Complete CH11-EX01, CH11-EX02, CH11-EX03, CH11-EX04, CH11-EX05 in [PRACTICE.md](../../PRACTICE.md).

**Chapter project:** Refactor a single-file inventory script into a package with configuration, logging, tests, and a documented entry point.

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
| Project | The central topic of this chapter. |
| Implementation | A concrete way of expressing an idea in code. |
| Edge case | An unusual but valid or important input condition. |
| Trade-off | A design choice that improves one quality while affecting another. |
