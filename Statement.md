# Project Statement

## Problem Statement
Individuals often lose track of their personal spending because manual tracking methods (pen-and-paper, memory, or unused spreadsheets) are tedious and rarely reviewed consistently. There is a need for a simple, no-setup tool that lets a user quickly log transactions and immediately see where their money is going, without requiring any installation beyond Python itself.

## Scope of the Project
This project is a command-line Personal Finance Tracker built in Python. It allows a user to:
- Record income and expense transactions
- View and analyze recorded transactions using fundamental algorithms (finding maximum, reversing order, removing duplicates, partitioning, and summation)
- Persist data between runs using a local JSON file

The scope is intentionally limited to single-user, local, command-line use — it does not include multi-user accounts, a graphical interface, or cloud storage, keeping it aligned with the tools and concepts covered in the CSE1021 syllabus (Units 2, 3, 4, and 5).

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
8. Persist all data automatically to `data.json` between sessionsx`