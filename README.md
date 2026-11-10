# Python Fundamentals 🐍

A structured, hands-on journey through Python fundamentals, software development, and practical programming.

## Repository structure

```text
python-fundamentals/
├── chapters/
│   ├── 01-python-foundations/
│   └── 02-conditions-and-loops/
├── archive/
│   └── early-exercises/
├── PRACTICE.md
├── PROGRESS.md
└── README.md
```

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

## Type hints

Python is dynamically typed: types belong to values, and a variable name can be assigned values of different types. **Type hints** (type annotations) document the type a variable, function parameter, or return value is expected to have.

### Variable annotations

```python
name: str = "Nima"
age: int = 20
height: float = 1.82
is_learning: bool = True
middle_name: str | None = None
scores: list[int] = [18, 20, 16]
prices: dict[str, float] = {"coffee": 2.5}
```

The part after the colon is the annotation. Assignment still works normally.

### Function annotations

```python
def calculate_total(price: float, quantity: int) -> float:
    return price * quantity

def show_message(message: str) -> None:
    print(message)
```

Parameter annotations describe expected argument types. The annotation after `->` describes the return type. Use `-> None` when a function does not return a meaningful value.

### Common types

| Hint | Meaning |
|---|---|
| `int` | Integer |
| `float` | Floating-point number |
| `str` | Text |
| `bool` | True or False |
| `None` | No value |
| `str \| None` | A string or None |
| `list[int]` | A list of integers |
| `dict[str, float]` | String keys and float values |

### Important rules

1. Type hints do **not** convert values. `input()` still returns `str`; use `int()` or `float()` when numeric values are needed.
2. Python does not enforce ordinary annotations at runtime. They primarily help readers, editors, and static type checkers.
3. An annotation does not replace input validation.
4. Keep annotations accurate when a variable is reassigned.
5. In a `for` loop, annotate the collection; Python infers the loop variable's type. Do not annotate the loop target itself.
6. The `X | None` syntax requires Python 3.10 or newer.

Type hints improve clarity and tooling support; they are not a substitute for tests.

## Practice problems

[PRACTICE.md](PRACTICE.md) contains five independent English-language problem statements for Chapter 01 and five for Chapter 02. Solutions are intentionally not included.

## Archived exercises

The `archive/early-exercises/` directory preserves original exercises separately from the organized chapter material.

## Study approach

1. Read each chapter's README.
2. Run the examples and inspect their output.
3. Modify values and test different inputs.
4. Complete the exercises without copying the examples.
5. Update the progress tracker only after the material has been taught and practiced.

> Learn by building. Improve by practicing.
