# Personal Finance Tracker
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
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        cat = input("Category (e.g. Food, Rent, Salary): ")
        amt = input("Amount: ")

        if not amt.replace(".", "", 1).isdigit():
            print("Amount must be a number. Transaction not added.")
        else:
            typ = input("Type (income/expense): ")
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
                if t["category"] == c["category"] and t["amount"] == c["amount"]:
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
        print("Goodbye!")
        break

    else:
        print("That's not a valid choice.")