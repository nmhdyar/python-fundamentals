# Chapter 06 — Object-Oriented Programming

> Status: Paired draft  
> Persian edition: [فصل 06 — برنامه‌نویسی شی‌گرا](../../../persian/chapters/06-object-oriented-programming/README.md)

## 1. Overview
Model related data and behavior with classes, then compose objects into maintainable programs.

## 2. Learning objectives
By the end of this chapter, you can:
- Explain the concepts below and identify when they are useful.
- Implement the patterns in small, executable Python programs.
- Choose a clear solution and explain its trade-offs.
- Test normal, boundary, and invalid cases.

## 3. Prerequisites
Chapters 01–05; functions, dictionaries, and basic modules.

## 4. Lessons
1. OOP mental model: state and behavior
2. Classes and instances
3. Instance attributes and methods
4. `__init__` and `self`
5. Encapsulation by convention and properties
6. Inheritance and method overriding
7. Polymorphism and duck typing
8. Composition versus inheritance
9. Useful magic methods: `__str__` and `__repr__`

### Runnable lesson files
| File | Focus |
|---|---|
| [01_classes_and_objects.py](01_classes_and_objects.py) | Create a Product class with validated price and a readable string representation. |
| [02_composition_and_polymorphism.py](02_composition_and_polymorphism.py) | Use composition and a shared interface to calculate different notification costs. |

## 5. Worked examples
The lesson scripts are executable worked examples. Trace each statement, predict its output before running it, then change one input or design choice and compare the result.

## 6. Common mistakes
- Putting every behavior in one class; confusing a class with an instance; forgetting `self`; using inheritance where composition is simpler.
- Copying a pattern without understanding its contract or side effects.
- Skipping validation and boundary cases.

## 7. Practice exercises
Complete CH06-EX01, CH06-EX02, CH06-EX03, CH06-EX04, CH06-EX05 in [PRACTICE.md](../../PRACTICE.md).

**Chapter project:** Build a library system with Book, Member, and Library objects; keep responsibilities small and explicit.

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
| Object-Oriented | The central topic of this chapter. |
| Implementation | A concrete way of expressing an idea in code. |
| Edge case | An unusual but valid or important input condition. |
| Trade-off | A design choice that improves one quality while affecting another. |
