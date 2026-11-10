# Python Fundamentals 🐍

A structured, hands-on journey through Python fundamentals, software development, and practical programming.

## Learning chapters

| Chapter | Focus |
|---|---|
| [01 — Python Foundations](chapters/01-python-foundations/) | Variables, data types, input/output, conversion, operators, strings |
| [02 — Conditions and Loops](chapters/02-conditions-and-loops/) | Conditions, loops, counters, accumulators, nested loops |
| 03 — Data Structures | Lists, tuples, sets, dictionaries |
| 04 — Functions | Functions, parameters, return values |
| 05 — Modules and Debugging | Imports, standard library, debugging |
| 06 — Object-Oriented Programming | Classes, objects, methods, object state |

Use [PRACTICE.md](PRACTICE.md) for five problem statements per available chapter. See [PROGRESS.md](PROGRESS.md) for the current learning checkpoint.

## Type hints

Python is dynamically typed. **Type hints** document the type a variable, parameter, or return value is expected to have.

### Variables

```python
name: str = "Nima"
age: int = 20
height: float = 1.82
is_learning: bool = True
middle_name: str | None = None
scores: list[int] = [18, 20, 16]
prices: dict[str, float] = {"coffee": 2.5}
```

### Functions

```python
def calculate_total(price: float, quantity: int) -> float:
    return price * quantity

def show_message(message: str) -> None:
    print(message)
```

Parameter annotations describe expected argument types; `->` describes the return type. Use `None` when a function does not return a meaningful value.

### Important rules

1. Type hints do not convert values. `input()` still returns `str`; use `int()` or `float()` when needed.
2. Python does not enforce ordinary annotations at runtime. They help readers, editors, and static type checkers.
3. An annotation does not replace input validation or tests.
4. Keep annotations accurate when a variable is reassigned.
5. Annotate a loop's iterable; Python can infer the loop variable's type.
6. The `X | None` syntax requires Python 3.10 or newer.

## Study workflow

1. Read each chapter README.
2. Read the concept notes in each Python file.
3. Run both examples and inspect their output.
4. Modify values and predict the result.
5. Complete the practice problems independently.
6. Update progress only after the material has been taught and practiced.

## Archived exercises

Original early exercises are preserved in [archive/early-exercises](archive/early-exercises/). They document learning history and are not the primary lesson sequence.

> Learn by building. Improve by practicing.
