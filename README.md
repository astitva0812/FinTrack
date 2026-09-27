# Personal Finance Tracker

A command-line Python program to log income and expenses and get simple analytics — built for the CSE1021 (Introduction to Problem Solving and Programming) evaluated course project.

## Features
1. Add a transaction (category, amount, income/expense)
2. View all transactions
3. Find the highest expense
4. View transactions newest-first (reversed order)
5. Remove duplicate transactions
6. Split transactions into income vs. expense
7. Show total income, total expense, and net balance
8. Data is saved to `data.json` and reloaded automatically next time you run it

## Technologies Used
- Python 3
- Standard library only (`json`) — no external packages needed

## How to Run
1. Make sure Python 3 is installed. Check with:python --version
2. Clone this repository:https://github.com/0812/finance-tracker.git
cd finance-tracker
3. Run the program: python main.py
4. Use the on-screen menu (type a number 1–8 and press Enter) to interact with it.

## Notes
-`main_backup.py` is an identical backup copy of `main.py`, provided in case there are any issues opening the primary file.
- Transaction data is stored in `data.json` in the same folder. This file is created automatically the first time you add a transaction.
- No installation of extra packages is required.