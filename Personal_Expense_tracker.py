import json
import os
from datetime import datetime

# File to store the expenses
FILE_NAME = "expenses.json"

# Load existing data from the file
def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    return []

# Save expenses to the file
def save_expenses(expenses):
    with open(FILE_NAME, 'w') as file:
        json.dump(expenses, file, indent=4)

# Add a new expense
def add_expense(expenses):
    amount = float(input("Enter the amount: $"))
    category = input("Enter the category (e.g., Food, Transport, Entertainment): ")
    date_input = input("Enter the date (YYYY-MM-DD) or press Enter to use today's date: ")
    date = date_input if date_input else str(datetime.now().date())

    expense = {
        "amount": amount,
        "category": category,
        "date": date
    }

    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully!\n")

# View summary of expenses
def view_summary(expenses):
    if not expenses:
        print("No expenses to show.\n")
        return

    print("1. View total spending by category")
    print("2. View total overall spending")
    print("3. View spending over time")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        category = input("Enter the category: ")
        total = sum(expense['amount'] for expense in expenses if expense['category'].lower() == category.lower())
        print(f"Total spending on {category}: ${total:.2f}\n")

    elif choice == '2':
        total = sum(expense['amount'] for expense in expenses)
        print(f"Total overall spending: ${total:.2f}\n")

    elif choice == '3':
        view_spending_over_time(expenses)
    
    else:
        print("Invalid choice. Please try again.\n")

# View spending over time (daily, weekly, or monthly)
def view_spending_over_time(expenses):
    print("1. Daily summary")
    print("2. Weekly summary")
    print("3. Monthly summary")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        group_by_date(expenses, 'daily')
    elif choice == '2':
        group_by_date(expenses, 'weekly')
    elif choice == '3':
        group_by_date(expenses, 'monthly')
    else:
        print("Invalid choice. Please try again.\n")

# Group expenses by day, week, or month
def group_by_date(expenses, period):
    grouped = {}

    for expense in expenses:
        date = datetime.strptime(expense['date'], "%Y-%m-%d")
        key = date.date()

        if period == 'weekly':
            key = f"Week {date.isocalendar()[1]} of {date.year}"
        elif period == 'monthly':
            key = f"{date.strftime('%B %Y')}"

        if key not in grouped:
            grouped[key] = 0
        grouped[key] += expense['amount']

    print(f"\nSpending summary ({period}):")
    for k, v in grouped.items():
        print(f"{k}: ${v:.2f}")
    print()

# Main menu for the user
def main_menu():
    expenses = load_expenses()

    while True:
        print("=== Personal Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_summary(expenses)
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Run the program
if __name__ == "__main__":
    main_menu()
