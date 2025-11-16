# expense_tracker.py
# main menu for expense tracker
# options: add expense, view all, view totals, quit

# while True:
#     show menu
#     get user choice
#     if 1: add expense
#     if 2: list expenses
#     if 3: totals
#     if 4: quit

# import csv # lets you save/read data
from datetime import datetime # datetime fills in today's date
from operator import truediv


def add_expense():
    # function for adding expense to CSV file
    # strip removes spaces from start and end of string
    date = input("Enter date (YYYY-MM-DD) or leave blank to fill for today: ").strip()
    if not date: # is date empty or false-y?
        # convert today's date/time to a particular string format
        date = datetime.now().strftime("%-%m-%d")

    category = input("Enter category (e.g., Food, Bills, Shopping): ").strip()
    description = input("Enter description: ").strip()

    # get amount of expense
    while True:
        try:
            amount = float(input("Enter amount ($): ").strip())
            break
        except ValueError:
            print("Please enter a valid number!")

def view_expenses():
    """Read all expenses from CSV and print them nicely."""
    print("\n--- All Expenses ---")
    try:
        with open("expenses.csv", "r") as file:
            # turn file into rows you can loop through
            reader = csv.reader(file)
            next(reader) # skip header row
            empty = True
            for row in reader:
                empty = False
                date, category, description, amount = row
                print(f'{date} | {category} | {description} ${amount}')
            if empty:
                print("No expenses found.")
    except FileNotFoundError:
        print("Expenses file not found.")
while True: # show user menu option using while loop
    print("--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Totals")
    print("4. Quit")

    choice = input("Choose and option: (1-4)") # get user input of choice

    if choice == "1":
        print("Add Expense")
        add_expense()
    elif choice == "2":
        print("View All Expenses")
        view_expenses()
    elif choice == "3":
        print("View totals")
    elif choice == "4":
        print("Goodbye!")
        break #exit out of program
    else:
        print("Invalid option. Please select (1-4)")




