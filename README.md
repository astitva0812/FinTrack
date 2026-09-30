# FinTrack - Personal Finance Tracker

## Overview

FinTrack is a simple command-line personal finance tracker developed using Python.

The program allows users to record income and expenses, view stored transactions, perform financial calculations, and apply different algorithms to organize and analyze transaction data.

The project was developed as part of the CSE1021 - Introduction to Problem Solving and Programming course.

---

## Problem

Managing small personal transactions manually can make it difficult to keep track of income, expenses, and the overall financial balance.

FinTrack provides a simple way to store transactions and perform basic financial analysis using Python data structures and algorithms.

---

## Objectives

The main objectives of FinTrack are:

1. Store income and expense transactions.
2. Allow users to view their stored transactions.
3. Calculate total income, total expenses, and net balance.
4. Analyze transaction data using basic algorithms.
5. Store data persistently using a JSON file.
6. Apply Python programming concepts learned in CSE1021.

---

## Features

FinTrack currently provides the following features:

1. **Add Transaction**
   - Add an income or expense.
   - Enter a category and amount.
   - Data is saved to `data.json`.

2. **View Transactions**
   - Display all transactions stored for the current user.

3. **Find Highest Expense**
   - Finds the transaction with the highest expense amount.

4. **Reverse Transactions**
   - Displays transactions in reverse order.

5. **Remove Duplicate Transactions**
   - Identifies and removes duplicate transaction entries.

6. **Separate Income and Expenses**
   - Separates transactions into income and expense groups.

7. **Financial Summary**
   - Calculates:
     - Total income
     - Total expenses
     - Net balance

8. **Transaction Statistics**
   - Counts total transactions.
   - Counts income and expense transactions.
   - Finds unique transaction categories.

9. **Kth Smallest Expense**
   - Finds the Kth smallest expense using an ordering algorithm.

10. **Exit**
   - Exits the program.

---

## Technologies Used

- Python 3
- JSON
- Python Standard Library

### Python Concepts Used

The project applies concepts from the CSE1021 syllabus, including:

- Variables and data types
- Input and output
- Conditional statements
- `while` and `for` loops
- Lists
- Dictionaries
- Sets
- String operations
- File handling
- JSON data storage
- Basic algorithms
- Searching and counting
- Maximum and minimum-style operations
- Array/list manipulation

---

## CSE1021 Algorithmic Techniques

Several operations in FinTrack are based on fundamental algorithms covered in CSE1021.

### Summation

The program uses loops to calculate total income and total expenses.

```text
Total = 0

For each transaction:
    add transaction amount to Total
