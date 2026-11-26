# Chapter 03 — Data Structures

> Status: Draft — paired English/Persian editions
> Persian edition: [فصل ۰۳ — ساختارهای داده](../../../persian/chapters/03-data-structures/README.md)

## 1. Overview
This chapter explains how to store, organize, access, and transform collections of values. Choose a data structure based on the operations and guarantees your program needs.

## 2. Learning objectives
By the end of this chapter, you should be able to:
- Create, access, update, and remove list items.
- Explain when tuples are useful and why they are immutable.
- Use sets for uniqueness and set operations.
- Store and retrieve key-value pairs in dictionaries.
- Work with nested collections safely.
- Build list and dictionary comprehensions.

## 3. Prerequisites
Chapters 01–02: variables, data types, strings, conditions, loops, and basic functions such as `len()` and `range()`.

## 4. Lessons
| File | Topics |
|---|---|
| [01 — Lists](01_lists.py) | Indexing, slicing, mutation, common methods |
| [02 — Tuples](02_tuples.py) | Immutability, packing, unpacking |
| [03 — Sets](03_sets.py) | Uniqueness, membership, union, intersection, difference |
| [04 — Dictionaries](04_dictionaries.py) | Keys, values, items, safe lookup, updates |
| [05 — Nested Structures](05_nested_structures.py) | Lists of dictionaries, nested access, safe updates |
| [06 — Comprehensions](06_comprehensions.py) | List and dictionary comprehensions, filtering |

## 5. Worked examples
The lesson files contain runnable examples for a shopping list, coordinates, unique tags, a product catalogue, student records, and filtered transformations.

## 6. Common mistakes
- Accessing an index or key that does not exist.
- Mutating a collection while iterating over it.
- Expecting a tuple to support item assignment.
- Using a mutable list or dictionary as a set element or dictionary key.
- Confusing `dict.get()` with direct indexing.
- Writing a comprehension that is harder to read than a normal loop.

## 7. Practice
Complete exercises `CH03-EX01` through `CH03-EX05` in the repository practice file. Exercise statements should be paired in English and Persian.

## 8. Recap
Lists are ordered and mutable; tuples are ordered and immutable; sets contain unique hashable values; dictionaries map unique hashable keys to values. Comprehensions create collections from iterables.

## 9. Self-check
- [ ] I can choose between a list, tuple, set, and dictionary.
- [ ] I can explain whether an operation mutates a collection.
- [ ] I can safely access nested data.
- [ ] I can rewrite a simple loop as a readable comprehension.

## 10. Glossary
| Term | Meaning |
|---|---|
| Mutable | Can be changed after creation |
| Immutable | Cannot be changed after creation |
| Iterable | An object that can be iterated over |
| Hashable | Has a stable hash and can be used as a set element or dictionary key |
| Comprehension | Compact syntax for constructing a collection |
