# Python Fundamentals — Practice Problems

Solve these problems independently after studying the matching chapter. The statements are in English to help you become comfortable reading technical requirements.

## Chapter 01 — Python Foundations

### Exercise 1 — Personal Profile Card

**Problem statement**

Write a program that asks the user for their full name, age, city, and height in meters. Clean the text input and display a neatly formatted profile card. Also calculate and display the user's age next year.

**Requirements**
- Use meaningful variables with `snake_case` names.
- Convert numeric input to the correct data type.
- Use at least two f-strings.
- Display the height with two decimal places.

### Exercise 2 — Temperature Converter

**Problem statement**

Write a program that asks the user for a temperature in Celsius and converts it to Fahrenheit and Kelvin.

**Requirements**
- Use `F = C * 9 / 5 + 32` and `K = C + 273.15`.
- Convert the input to a floating-point number.
- Display all three temperatures with two decimal places.
- Use clear labels and readable output.

### Exercise 3 — Simple Receipt Calculator

**Problem statement**

Create a receipt calculator. Ask for a product name, unit price, and quantity. Calculate the subtotal, a 9% tax amount, and the final total.

**Requirements**
- Convert price to `float` and quantity to `int`.
- Calculate tax from the subtotal.
- Display the product name, quantity, subtotal, tax, and final total.
- Format all monetary values to two decimal places.

### Exercise 4 — Number Analysis

**Problem statement**

Ask the user to enter two numbers. Display their sum, difference, product, quotient, floor division result, and remainder.

**Requirements**
- Convert both inputs to numbers.
- Use the appropriate arithmetic operators.
- Display each operation with a descriptive label.
- Do not perform division if the second number is zero; display a clear message instead.

### Exercise 5 — Username Generator

**Problem statement**

Ask the user for their full name. Generate a username by removing leading and trailing spaces, converting the name to lowercase, and replacing spaces with underscores.

**Requirements**
- Use `strip()`, `lower()`, and `replace()`.
- Display the cleaned full name and generated username.
- Display the number of characters in the final username.
- Store the generated value in a new variable.

---

## Chapter 02 — Conditions and Loops

### Exercise 1 — Ticket Price Calculator

**Problem statement**

Write a program that asks the user for their age and calculates the ticket price based on these rules:

- Under 6 years old: free.
- From 6 to 17: 50% of the regular price.
- From 18 to 64: regular price.
- 65 or older: 30% discount.
- Negative ages must be rejected as invalid.

**Requirements**
- Use `if`, `elif`, and `else`.
- Store the regular ticket price in a variable.
- Display the final price with two decimal places.

### Exercise 2 — Multiplication Table

**Problem statement**

Ask the user for an integer and print its multiplication table from 1 to 10.

**Requirements**
- Use a `for` loop and `range()`.
- Display each calculation as `number x multiplier = result`.
- Print exactly ten rows.

### Exercise 3 — Password Attempts

**Problem statement**

Create a simple password checker. Repeatedly ask the user to enter a password until the correct password is entered or the user has used all three attempts.

**Requirements**
- Use a `while` loop.
- Track attempts with a counter.
- Display the remaining attempts after each incorrect entry.
- Stop immediately when the correct password is entered.
- Display an appropriate message when all attempts are used.

### Exercise 4 — Number Statistics

**Problem statement**

Ask the user to enter a positive integer N. Examine all integers from 1 through N and calculate how many are even, how many are odd, and the sum of all integers in that range.

**Requirements**
- Use a `for` loop and an `if/else` statement.
- Use modulo to identify even and odd numbers.
- Use counters for even and odd numbers.
- Use an accumulator for the total sum.
- Reject N if it is less than 1.

### Exercise 5 — Multiplication Grid

**Problem statement**

Ask the user for the number of rows and columns. Print a multiplication grid in which each cell contains the product of its row number and column number.

**Requirements**
- Use nested `for` loops.
- Number rows and columns starting from 1.
- Align the output so the grid is easy to read.
- Reject row or column values less than 1.

---

## Submission checklist

Before considering an exercise complete:

- [ ] The program runs without syntax errors.
- [ ] Variable names are descriptive.
- [ ] The output is readable.
- [ ] You tested normal and boundary inputs.
- [ ] You can explain every line without copying it from the lesson.

**Rule:** Make a serious attempt before looking for help. If you get stuck, write down what you expected, what actually happened, and the exact error message.
