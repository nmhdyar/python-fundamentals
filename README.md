# Python Fundamentals 🐍

A practical Python curriculum with synchronized English and Persian editions.

> **Release status: Verified** — chapters 01–11 are complete in both languages. Chapters 02–11 pass automated compilation, execution, filename-pairing, and exercise-ID checks (`tools/verify_curriculum.py`).

## Choose your language
- [English curriculum](english/README.md)
- [مسیر آموزشی فارسی](persian/README.md)

## Curriculum map
| Chapter | Topic | Main concepts |
|---|---|---|
| [01](english/chapters/01-python-foundations/) | Python Foundations | Variables, types, input/output, conversion, operators, strings |
| [02](english/chapters/02-conditions-and-loops/) | Conditions and Loops | Branching, iteration, counters, accumulators, nested loops |
| [03](english/chapters/03-data-structures/) | Data Structures | Lists, tuples, sets, dictionaries, comprehensions |
| [04](english/chapters/04-functions/) | Functions | Parameters, return values, flexible arguments, scope, recursion |
| [05](english/chapters/05-modules-and-debugging/) | Modules, Exceptions, and Debugging | Imports, standard library, exceptions, debugging, environments |
| [06](english/chapters/06-object-oriented-programming/) | Object-Oriented Programming | Classes, objects, composition, polymorphism |
| [07](english/chapters/07-file-handling-and-data-persistence/) | File Handling and Data Persistence | Text files, paths, JSON, CSV, data persistence |
| [08](english/chapters/08-testing-and-code-quality/) | Testing and Code Quality | unittest, testable design, code quality |
| [09](english/chapters/09-iterators-and-generators/) | Iterators and Generators | Iteration protocol, generators, lazy streams |
| [10](english/chapters/10-advanced-python-concepts/) | Advanced Python Concepts | Closures, decorators, context managers, dataclasses |
| [11](english/chapters/11-project-structure-and-packaging/) | Project Structure and Packaging | Logging, configuration, package layout |

## Repository layout
```text
.
├── docs/                 # Bilingual teaching standard and chapter templates
├── english/
│   ├── chapters/         # English lessons, chapter 01 through 11
│   ├── archive/          # Historical early exercises; not part of the main path
│   ├── PRACTICE.md       # Exercises CH01-EX01 through CH11-EX05
│   ├── PROGRESS.md       # Learner-maintained checkpoint
│   └── README.md         # English navigation
├── persian/              # Same structure and content coverage in Persian
└── README.md             # Project entry point
```

## How to use this repository
1. Choose English or Persian.
2. Follow chapters 01 to 11 in order; each chapter links to its paired translation.
3. Read a chapter README before opening its numbered Python lessons.
4. Run each lesson, change the examples, and predict the output.
5. Solve the matching exercise IDs in `PRACTICE.md`.
6. Update `PROGRESS.md` only after personally studying and practising a topic.

## Bilingual quality rule
Both editions must share chapter order, learning objectives, code logic, filenames, exercise IDs, and difficulty. Explanations and comments may be localized. See the [English teaching standard](docs/TEACHING_STANDARD.md) and [استاندارد فارسی](docs/TEACHING_STANDARD.fa.md).
