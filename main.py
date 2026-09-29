# Personal Finance Tracker - FinTrack
# CSE1021 - Introduction to Problem Solving and Programming
# Name: Astitva Srivastava
# Reg No: 26BAS10101

import json
import os

folder = os.path.dirname(os.path.abspath(__file__))
data_file = os.path.join(folder, "data.json")

all_data = {}

try:
    f = open(data_file, "r")
    all_data = json.load(f)
    f.close()
    if not isinstance(all_data, dict):
        all_data = {}
except (FileNotFoundError, json.decoder.JSONDecodeError):
    all_data = {}

user_name = input("Enter your name: ")
print("Welcome,", user_name, "- let's track your finances!")

if user_name in all_data:
    tx = all_data[user_name]
else:
    tx = []

while True:
    print()
    print("1. Add a transaction")
    print("2. View all transactions")
    print("3. Find highest expense")
    print("4. View transactions (newest first)")
    print("5. Remove duplicate transactions")
    print("6. Split into income vs. expense")
    print("7. Show total income, expense, and balance")
    print("8. Count transactions and unique categories")
    print("9. Find Kth smallest expense")
    print("10. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        cat = input("Category (e.g. Food, Rent, Salary): ")
        amt = input("Amount: ")

        if not amt.replace(".", "", 1).isdigit():
            print("Amount must be a number. Transaction not added.")
        else:
            typ = input("Type (income/expense): ")
            if typ not in ["income", "expense"]:
                print("Type must be exactly 'income' or 'expense'. Transaction not added.")
            else:
                tx.append({"category": cat, "amount": amt, "type": typ})
                all_data[user_name] = tx
                f = open(data_file, "w")
                json.dump(all_data, f)
                f.close()
                print("Added and saved!")

    elif choice == "2":
        for t in tx:
            print(t["category"], "-", t["amount"], "-", t["type"])

    elif choice == "3":
        exp_only = []
        for t in tx:
            if t["type"] == "expense":
                exp_only.append(t)

        if len(exp_only) == 0:
            print("No expenses yet.")
        else:
            high = exp_only[0]
            for t in exp_only:
                if float(t["amount"]) > float(high["amount"]):
                    high = t
            print("Highest expense:", high["category"], "-", high["amount"])

    elif choice == "4":
        rev = []
        for t in tx:
            rev.insert(0, t)
        for t in rev:
            print(t["category"], "-", t["amount"], "-", t["type"])

    elif choice == "5":
        clean = []
        for t in tx:
            dup = False
            for c in clean:
                if t["category"] == c["category"] and t["amount"] == c["amount"] and t["type"] == c["type"]:
                    dup = True
            if not dup:
                clean.append(t)
        tx = clean
        all_data[user_name] = tx
        f = open(data_file, "w")
        json.dump(all_data, f)
        f.close()
        print("Duplicates removed. Remaining transactions:", len(tx))

    elif choice == "6":
        inc = []
        exp = []
        for t in tx:
            if t["type"] == "income":
                inc.append(t)
            else:
                exp.append(t)
        print()
        print("--- INCOME ---")
        for t in inc:
            print(t["category"], "-", t["amount"])
        print()
        print("--- EXPENSE ---")
        for t in exp:
            print(t["category"], "-", t["amount"])

    elif choice == "7":
        ti = 0
        te = 0
        for t in tx:
            if t["type"] == "income":
                ti = ti + float(t["amount"])
            else:
                te = te + float(t["amount"])
        bal = ti - te
        print()
        print("Total income:", ti)
        print("Total expense:", te)
        print("Net balance:", bal)

    elif choice == "8":
        total_cnt = 0
        inc_cnt = 0
        exp_cnt = 0
        categories = set()

        for t in tx:
            total_cnt = total_cnt + 1
            if t["type"] == "income":
                inc_cnt = inc_cnt + 1
            else:
                exp_cnt = exp_cnt + 1
            categories.add(t["category"])

        print()
        print("Total transactions:", total_cnt)
        print("Income transactions:", inc_cnt)
        print("Expense transactions:", exp_cnt)
        print("Unique categories:", len(categories))

    elif choice == "9":
        exp_only = []
        for t in tx:
            if t["type"] == "expense":
                exp_only.append(t)

        if len(exp_only) == 0:
            print("No expenses yet.")
        else:
            k_input = input("Enter K (1 to " + str(len(exp_only)) + "): ")
            if not k_input.isdigit():
                print("K must be a positive number.")
            else:
                k = int(k_input)
                if k < 1 or k > len(exp_only):
                    print("Invalid K value.")
                else:
                    for i in range(len(exp_only)):
                        min_idx = i
                        for j in range(i + 1, len(exp_only)):
                            if float(exp_only[j]["amount"]) < float(exp_only[min_idx]["amount"]):
                                min_idx = j
                        temp = exp_only[i]
                        exp_only[i] = exp_only[min_idx]
                        exp_only[min_idx] = temp

                    res = exp_only[k - 1]
                    print("Rank", k, "smallest expense:", res["category"], "-", res["amount"])

    elif choice == "10":
        print("Goodbye!")
        break

    else:
        print("That's not a valid choice.")