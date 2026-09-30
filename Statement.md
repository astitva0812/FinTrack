# FinTrack - Project Statement

## Problem Statement

Managing personal finances manually can make it difficult to keep track of income, expenses, spending categories, and the overall balance. A simple system is needed to record financial transactions and perform basic calculations on the stored data.

FinTrack is a Python-based command-line application designed to help users record and analyse their personal financial transactions. The project applies fundamental programming and problem-solving concepts from CSE1021, including algorithms, conditional statements, loops, lists, dictionaries, sets, and JSON-based data storage.

The application allows users to add transactions, view stored transactions, analyse expenses, calculate income and balance, remove duplicate transactions, separate income and expenses, and find the Kth smallest expense.

---

## Objectives

The main objectives of FinTrack are:

1. To develop a simple command-line application for recording and managing personal income and expense transactions.

2. To apply fundamental problem-solving techniques such as algorithms, logical decision-making, iteration, searching, counting, summation, reversal, duplicate removal, partitioning, and sorting.

3. To use Python data structures such as lists, dictionaries, and sets to store and process transaction data.

4. To provide basic financial analysis such as total income, total expenses, net balance, highest expense, unique categories, and the Kth smallest expense.

5. To store transaction data persistently using a local JSON file so that information can be retained between program executions.

6. To demonstrate the application of concepts covered in the CSE1021 Introduction to Problem Solving and Programming syllabus through a practical real-world problem.

---

## Scope of the Project

FinTrack focuses on basic personal financial transaction management through a command-line interface.

The project includes:

* Adding income and expense transactions.
* Viewing all stored transactions.
* Finding the highest expense.
* Viewing transactions in reverse order.
* Removing duplicate transactions.
* Separating income and expense transactions.
* Calculating total income, total expenses, and balance.
* Counting the number of transactions and unique categories.
* Finding the Kth smallest expense.
* Saving and loading transaction data using a JSON file.

The project is intended as an educational application demonstrating fundamental programming and algorithmic concepts rather than as a complete professional financial management system.

---

## Target Users

The primary target users are:

* Students who want to keep track of basic personal income and expenses.
* Individuals who want a simple command-line method for recording transactions.
* Students learning basic Python programming and problem-solving techniques.

---

## High-Level Features

FinTrack provides the following major features:

1. **Add Transaction**
   Allows the user to enter a transaction category, amount, and transaction type.

2. **View Transactions**
   Displays the transactions stored in the application.

3. **Highest Expense**
   Finds the transaction with the highest expense amount.

4. **Reverse Transactions**
   Displays transactions in reverse order.

5. **Duplicate Removal**
   Identifies and removes duplicate transactions.

6. **Income and Expense Separation**
   Partitions transactions into income and expense groups.

7. **Financial Summary**
   Calculates total income, total expenses, and the resulting balance.

8. **Transaction and Category Counting**
   Counts the total number of transactions and unique transaction categories.

9. **Kth Smallest Expense**
   Processes expense values to determine the Kth smallest expense.

10. **JSON Data Storage**
    Saves transaction information to a local JSON file and loads it when the program starts.

---

## Functional Requirements

### FR1 - Transaction Management

The system shall allow the user to:

* Enter a transaction category.
* Enter a transaction amount.
* Specify whether the transaction is an income or an expense.
* Add the transaction to the stored transaction list.
* Save the transaction data to the local JSON file.

### FR2 - Transaction Viewing and Processing

The system shall allow the user to:

* View all recorded transactions.
* Display transactions in reverse order.
* Remove duplicate transactions.
* Separate transactions into income and expense groups.
* Count the total number of transactions.
* Count the number of unique transaction categories.

### FR3 - Financial Analysis

The system shall calculate and display:

* The highest expense.
* Total income.
* Total expenses.
* Net balance.
* The Kth smallest expense.

### FR4 - Persistent Data Storage

The system shall:

* Load previously stored transaction data from `data.json`.
* Save new or modified transaction data to `data.json`.
* Retain transaction information between program executions.
* Handle a missing or invalid JSON data file without terminating unexpectedly.

---

## Non-Functional Requirements

### NFR1 - Usability

The program should provide a simple command-line menu so that users can select operations using numbered choices and receive understandable messages.

### NFR2 - Reliability

The program should continue operating when the user enters an invalid menu option or invalid transaction type instead of terminating unexpectedly.

### NFR3 - Data Persistence

Transaction information should remain available between program executions by storing the data in a local JSON file.

### NFR4 - Error Handling

The program should handle situations such as a missing data file, invalid JSON data, invalid transaction amounts, invalid transaction types, and invalid K values without causing the program to crash.

### NFR5 - Resource Efficiency

The program should use Python's built-in data structures and standard library functionality without requiring external packages, keeping the application lightweight and easy to run.

### NFR6 - Maintainability

The program should use understandable variable names, simple control structures, and logically separated operations so that the source code can be modified and extended by a student familiar with basic Python programming.

---

## CSE1021 Syllabus Mapping

FinTrack applies concepts from the CSE1021 Introduction to Problem Solving and Programming syllabus.

| CSE1021 Concept                      | Application in FinTrack                                                           |
| ------------------------------------ | --------------------------------------------------------------------------------- |
| Problem solving and algorithm design | The program follows a menu-driven workflow for processing financial transactions. |
| Python data types and expressions    | Strings, integers, floating-point values, lists, dictionaries, and sets are used. |
| Conditional statements               | `if`, `elif`, and `else` are used to process menu choices and input.              |
| Loops                                | `while` and `for` loops are used for menu repetition and transaction processing.  |
| Lists                                | Transactions are stored and processed using lists.                                |
| Dictionaries                         | Individual transactions and user data are represented using dictionaries.         |
| Sets                                 | Sets are used to determine unique transaction categories.                         |
| Maximum finding                      | The highest expense is found by processing expense transactions.                  |
| Reversal                             | Transactions can be displayed in reverse order.                                   |
| Duplicate removal                    | Duplicate transactions are identified and removed.                                |
| Partitioning                         | Transactions are separated into income and expense groups.                        |
| Summation                            | Total income and total expenses are calculated by processing transactions.        |
| Sorting / Kth smallest               | Expense values are processed to find the Kth smallest expense.                    |
| JSON data storage                    | Python's `json` module is used to save and load transaction data.                 |

The project therefore demonstrates the application of Python programming, control flow, data structures, and fundamental algorithms covered in the CSE1021 syllabus.
