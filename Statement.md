# Project Statement

## Problem Statement
Individuals often lose track of their personal spending because manual tracking methods (pen-and-paper, memory, or unused spreadsheets) are tedious and rarely reviewed consistently. There is a need for a simple, no-setup tool that lets a user quickly log transactions and immediately see where their money is going, without requiring any installation beyond Python itself.

## Functional Requirements

FinTrack provides the following major functional modules:

### FR1 — Transaction Management

The system shall allow the user to:

* Enter a transaction category.
* Enter a transaction amount.
* Specify whether the transaction is an income or an expense.
* Store the transaction in the application's transaction list.
* Save the transaction to the local JSON file.

### FR2 — Transaction Viewing and Processing

The system shall allow the user to:

* View all recorded transactions.
* Display transactions in reverse order.
* Remove duplicate transactions.
* Separate transactions into income and expense groups.
* Count the total number of transactions.
* Count the number of unique categories.

### FR3 — Financial Analysis

The system shall calculate and display:

* The highest expense.
* Total income.
* Total expenses.
* Net balance.
* The Kth smallest expense.

### FR4 — Persistent Data Storage

The system shall:

* Load previously stored transaction data from `data.json`.
* Save new or modified transaction data to `data.json`.
* Continue using previously stored data when the program is executed again.
* Handle a missing or invalid JSON file by starting with an empty data structure.

## Objectives
The main objectives of FinTrack are:

1. To develop a simple command-line application for recording and managing personal income and expense transactions.

2. To apply fundamental problem-solving techniques such as algorithms, logical decision-making, iteration, searching, counting, summation, reversal, duplicate removal, partitioning, and sorting.

3. To use Python data structures such as lists, dictionaries, and sets to store and process transaction data.

4. To provide basic financial analysis such as total income, total expenses, net balance, highest expense, unique categories, and the Kth smallest expense.

5. To store transaction data persistently using a local JSON file so that information can be retained between program executions.

6. To demonstrate the application of concepts covered in the CSE1021 Introduction to Problem Solving and Programming syllabus through a practical real-world problem.

## Scope of the Project
This project is a command-line Personal Finance Tracker built in Python. It allows a user to:
- Record income and expense transactions
- View and analyze recorded transactions using fundamental algorithms (finding maximum, reversing order, removing duplicates, partitioning, summation, set operations, and finding the Kth smallest element)
- Persist data between runs using a local JSON file

The scope is intentionally limited to single-user-per-name, local, command-line use — it does not include a graphical interface or cloud storage, keeping it aligned with the tools and concepts covered in the CSE1021 syllabus (Units 2, 3, 4, and 5).

## Target Users
Students or individuals who want a lightweight way to track personal income and expenses without learning spreadsheet software or installing a dedicated budgeting app.

## High-Level Features
1. Add a transaction (category, amount, type: income/expense)
2. View all transactions
3. Find the highest expense
4. View transactions in reverse (most recent first)
5. Remove duplicate transactions
6. Split transactions into income vs. expense
7. Calculate and display total income, total expense, and net balance
8. Count total transactions and unique categories used
9. Find the Kth smallest expense
10. Persist all data automatically to `data.json` between sessions

## Non-Functional Requirements

### NFR1 — Usability

The program should provide a simple command-line menu so that a user can select operations using numbered choices and receive understandable messages.

### NFR2 — Reliability

The program should continue operating when the user enters an invalid menu option or an invalid transaction type instead of terminating unexpectedly.

### NFR3 — Data Persistence

Transaction information should remain available between program executions by storing the data in a local JSON file.

### NFR4 — Error Handling

The program should handle situations such as a missing data file, invalid JSON data, invalid transaction amounts, invalid transaction types, and invalid K values without causing the program to crash.

### NFR5 — Resource Efficiency

The program should use Python's built-in data structures and standard library functionality without requiring external packages, keeping the application lightweight and easy to run.

### NFR6 — Maintainability

The program should use understandable variable names, simple control structures, and logically separated operations so that the source code can be modified and extended by a student familiar with basic Python programming.

## CSE1021 Syllabus Mapping

The implementation of FinTrack applies concepts from the CSE1021 Introduction to Problem Solving and Programming syllabus.

| CSE1021 Concept                      | Application in FinTrack                                                           |
| ------------------------------------ | --------------------------------------------------------------------------------- |
| Problem solving and algorithm design | The program follows a menu-driven workflow for processing financial transactions. |
| Python data types and expressions    | Strings, integers, floating-point values, lists, dictionaries, and sets are used. |
| Conditional statements               | `if`, `elif`, and `else` are used to process menu choices and validate input.     |
| Loops                                | `while` and `for` loops are used for menu repetition and transaction processing.  |
| Lists                                | Transactions are stored and processed using lists.                                |
| Dictionaries                         | Individual transactions and user data are represented using dictionaries.         |
| Sets                                 | Sets are used to determine unique transaction categories.                         |
| Maximum finding                      | The highest expense is found by iterating through expense transactions.           |
| Reversal                             | Transactions are displayed in reverse order using list insertion.                 |
| Duplicate removal                    | Duplicate transactions are identified and removed using comparison.               |
| Partitioning                         | Transactions are separated into income and expense groups.                        |
| Summation                            | Total income and total expense are calculated by iterating through transactions.  |
| Sorting / Kth smallest               | Selection-sort-style processing is used to find the Kth smallest expense.         |
| JSON data storage                    | The `json` module is used to save and reload transaction data.                    |
