# Testing - FinTrack

## 1. Testing Approach

FinTrack was tested by running the program with different users, transaction values, and menu options.

The testing focused on checking whether the main input, storage, viewing, and financial calculation operations produced the expected results.

---

## 2. Test Cases

| Test ID | Feature Tested | Input / Action | Expected Result | Result |
|---|---|---|---|---|
| T01 | Add Expense | Food, 300, expense | Transaction is added and saved | Passed |
| T02 | Add Income | Salary, 20000, income | Transaction is added and saved | Passed |
| T03 | View Transactions | Select option 2 | Previously stored transactions are displayed | Passed |
| T04 | Different User | User `Aryan`, Food, 200, expense | Transaction is saved for the selected user | Passed |
| T05 | Financial Summary | Select option 7 | Total income, expense and net balance are calculated | Passed |

---

## 3. Test Evidence

### T01 - Add Expense

The program was tested by adding:

```text
Category: Food
Amount: 300
Type: expense
