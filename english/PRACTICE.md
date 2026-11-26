# Python Fundamentals — Practice Bank

Solve each problem independently after studying its matching chapter. Exercise IDs are identical in the Persian edition.

## Chapter 01 — Python Foundations
- **CH01-EX01 — Personal Profile Card:** Ask for a name, age, city, and height. Convert numeric inputs, then display a formatted profile and the age next year. Use meaningful variables and at least two f-strings.
- **CH01-EX02 — Temperature Converter:** Convert Celsius to Fahrenheit and Kelvin using `F = C * 9 / 5 + 32` and `K = C + 273.15`. Display two decimal places.
- **CH01-EX03 — Simple Receipt:** Ask for a product, unit price, and quantity. Calculate subtotal, 9% tax, and final total. Convert price to float and quantity to int.
- **CH01-EX04 — Number Analysis:** Ask for two numbers and display sum, difference, product, quotient, floor division, and remainder. Handle division by zero.
- **CH01-EX05 — Username Generator:** Clean a full name and create a lowercase username with underscores. Use `strip()`, `lower()`, and `replace()`.

## Chapter 02 — Conditions and Loops
- **CH02-EX01 — Ticket Price Calculator:** Under 6 is free, ages 6–17 pay half, 18–64 pay full price, and 65+ receive 30% off. Reject negative ages. Use `if/elif/else`.
- **CH02-EX02 — Multiplication Table:** Print an integer's multiplication table from 1 through 10 using `for` and `range()`.
- **CH02-EX03 — Password Attempts:** Allow up to three password attempts. Stop on a correct password; use `while` and a counter.
- **CH02-EX04 — Number Statistics:** For positive N, count evens and odds from 1 through N and calculate the sum. Use modulo, counters, and an accumulator.
- **CH02-EX05 — Multiplication Grid:** Ask for row and column counts and print a neatly aligned grid using nested `for` loops.

## Chapter 03 — Data Structures
- **CH03-EX01 — Shopping List Manager:** Add, remove, and display items. Use list methods and handle a missing item gracefully.
- **CH03-EX02 — Coordinate Records:** Store coordinates in a tuple, unpack x and y, and calculate distance from the origin.
- **CH03-EX03 — Unique Tags:** Given two tag lists, display unique, shared, and first-list-only tags using set operations.
- **CH03-EX04 — Product Catalogue:** Store products in a dictionary keyed by product ID. Support safe lookup and stock updates using `get()` and `in`.
- **CH03-EX05 — Score Summary:** Store students and scores in nested dictionaries. Use a dictionary comprehension to keep students whose average is at least 15.

## Chapter 04 — Functions
- **CH04-EX01 — Reusable Greeting:** Write a function that accepts a name and returns a greeting string. Use a parameter and `return`.
- **CH04-EX02 — Order Total:** Write a function that accepts price, quantity, and an optional discount rate. Validate values and return the final amount.
- **CH04-EX03 — Flexible Statistics:** Accept any number of numeric positional arguments and return count, minimum, maximum, and average. Use `*args` and define behavior for no arguments.
- **CH04-EX04 — Student Report:** Accept a student name and keyword-based subject scores, then return a formatted summary. Use `**kwargs`.
- **CH04-EX05 — Recursive Sum:** Return the sum of integers from 1 through n using recursion. Include a base case and reject negative input.

## Chapter 05 — Modules, Exceptions, and Debugging
- **CH05-EX01 — Unit Converter Module:** Create a module with temperature conversion functions and a separate script that imports it. Use the main guard.
- **CH05-EX02 — Date Utility:** Use `datetime` to calculate days between two ISO-format dates. Handle invalid input.
- **CH05-EX03 — Safe Division:** Handle invalid numbers and division by zero separately with specific `except` clauses.
- **CH05-EX04 — Positive Quantity:** Raise `ValueError` for zero or negative quantities. Handle it at the call site.
- **CH05-EX05 — Debugging Report:** Reproduce and fix at least two bugs in a short program. Record the traceback, cause, fix, and verification.

## Submission checklist
- [ ] The program runs without syntax errors.
- [ ] Names are clear and follow `snake_case`.
- [ ] Normal and edge-case inputs have been tested.
- [ ] I can explain the code without copying it.
