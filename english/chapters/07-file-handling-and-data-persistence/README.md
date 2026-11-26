# Chapter 07 — File Handling & Data Persistence

> Status: Paired draft  
> Persian edition: [فصل 07 — کار با فایل و ماندگاری داده](../../../persian/chapters/07-file-handling-and-data-persistence/README.md)

## 1. Overview
Read, write, and preserve structured data safely across program runs.

## 2. Learning objectives
By the end of this chapter, you can:
- Explain the concepts below and identify when they are useful.
- Implement the patterns in small, executable Python programs.
- Choose a clear solution and explain its trade-offs.
- Test normal, boundary, and invalid cases.

## 3. Prerequisites
Chapters 01–05; strings, dictionaries, exceptions, and pathlib basics.

## 4. Lessons
1. Text files and file modes
2. Reading: `read`, `readline`, and iteration
3. Writing and appending
4. Context managers and `with`
5. Paths with `pathlib`
6. JSON serialization and deserialization
7. CSV readers and writers
8. Encoding and newline considerations
9. File-related exceptions and safe updates

### Runnable lesson files
| File | Focus |
|---|---|
| [01_text_files_and_paths.py](01_text_files_and_paths.py) | Use pathlib and a temporary directory to write and read a UTF-8 text file safely. |
| [02_json_and_csv.py](02_json_and_csv.py) | Serialize structured records to JSON and export rows with the csv module. |

## 5. Worked examples
The lesson scripts are executable worked examples. Trace each statement, predict its output before running it, then change one input or design choice and compare the result.

## 6. Common mistakes
- Forgetting to close files; overwriting when append was intended; assuming JSON preserves custom Python objects; ignoring encoding and missing-file errors.
- Copying a pattern without understanding its contract or side effects.
- Skipping validation and boundary cases.

## 7. Practice exercises
Complete CH07-EX01, CH07-EX02, CH07-EX03, CH07-EX04, CH07-EX05 in [PRACTICE.md](../../PRACTICE.md).

**Chapter project:** Create a contact manager that loads and saves contacts as JSON, validates records, and exports a CSV report.

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
| File | The central topic of this chapter. |
| Implementation | A concrete way of expressing an idea in code. |
| Edge case | An unusual but valid or important input condition. |
| Trade-off | A design choice that improves one quality while affecting another. |
