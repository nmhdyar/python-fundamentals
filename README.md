# Python Fundamentals 🐍

A structured, hands-on journey through Python fundamentals, software development, and practical programming.

## Repository structure

```text
python-fundamentals/
├── chapters/
│   ├── 01-python-foundations/
│   └── 02-conditions-and-loops/
│       ├── README.md
│       ├── 01_variables_and_types.py
│       ├── 02_input_output.py
│       ├── 03_type_conversion.py
│       ├── 04_operators.py
│       ├── 05_strings.py
│       └── 06_foundations_exercises.py
├── archive/
│   └── early-exercises/
├── README.md
└── PROGRESS.md
```

## Type hints

Python is dynamically typed, which means variable types are determined while the program runs. **Type hints** let you document the type you expect a variable, function parameter, or return value to have.

### Variable annotations

```python
name: str = "Nima"
age: int = 20
height: float = 1.82
is_learning: bool = True
middle_name: str | None = None
languages: list[str] = ["Python", "JavaScript"]
```

### Function annotations

```python
def calculate_total(price: float, quantity: int) -> float:
    return price * quantity
```

The annotations before the parameter names describe expected argument types. The annotation after `->` describes the return type. Use `-> None` when a function does not return a meaningful value.

### Important points

- Type hints do **not** automatically convert values or enforce types at runtime.
- `input()` still returns a `str`; convert it with `int()` or `float()` when needed.
- Use `str | None` when a value may be a string or `None` (Python 3.10+).
- For collections, specify their item types, such as `list[int]` or `dict[str, float]`.
- Annotate the collection in a `for` loop; Python can infer the loop variable's type. Do not annotate the loop target directly.
- Keep annotations accurate when a variable is reassigned.

Type hints improve readability and editor/static-checker support. They are not a replacement for input validation or tests.

## Learning chapters

| Chapter | Focus | Status |
|---|---|---|
| [01 — Python Foundations](chapters/01-python-foundations/) | Variables, data types, input/output, conversion, operators, strings | Organized |
| [02 — Conditions and Loops](chapters/02-conditions-and-loops/) | Conditions, loops, nested loops | Organized |
| 03 — Data Structures | Lists, tuples, sets, dictionaries | Review and practice |
| 04 — Functions | Functions, parameters, return values | Consolidation |
| 05 — Modules and Debugging | Imports, standard library, debugging | Previously practiced |
| 06 — Object-Oriented Programming | Classes, objects, methods, object state | In progress |

Use [PRACTICE.md](PRACTICE.md) for five English-language exercises per chapter. See [PROGRESS.md](PROGRESS.md) for the actual learning checkpoint. A chapter's presence in the repository does not automatically mean it has been mastered.

## Practice problems

The root-level [PRACTICE.md](PRACTICE.md) contains five independent problem statements for Chapter 01 and five for Chapter 02. No solutions are included, so the file can be used for real practice.

## Archived exercises

The `archive/early-exercises/` directory preserves the original small exercises from the first stages of learning. They are kept as learning history, separate from the organized chapter material.

## Study approach

1. Read each chapter's README.
2. Run the examples and inspect their output.
3. Modify values and test different inputs.
4. Complete the exercises without copying the examples.
5. Update the progress tracker only after the material has been taught and practiced.

> Learn by building. Improve by practicing.
