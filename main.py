import json
import os
from datetime import datetime

class ExpenseTracker:
    def __init__(self, filename='expenses.json'):
        self.filename = filename
        self.expenses = self.load_expenses()

    def load_expenses(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        else:
            return []

    def save_expenses(self):
        with open(self.filename, 'w') as file:
            json.dump(self.expenses, file, indent=4)

    def add_expense(self, amount, description, category):
        expense = {
            'amount': amount,
            'description': description,
            'category': category,
            'date': datetime.now().strftime('%Y-%m-%d')
        }
        self.expenses.append(expense)
        self.save_expenses()

    def view_summary(self, month, year):
        monthly_expenses = [e for e in self.expenses if datetime.strptime(e['date'], '%Y-%m-%d').month == month and datetime.strptime(e['date'], '%Y-%m-%d').year == year]
        total = sum(e['amount'] for e in monthly_expenses)
        category_summary = {}
        for e in monthly_expenses:
            if e['category'] in category_summary:
                category_summary[e['category']] += e['amount']
            else:
                category_summary[e['category']] = e['amount']
        return total, category_summary

    def run(self):
        while True:
            print("\nExpense Tracker")
            print("1. Add Expense")
            print("2. View Summary")
            print("3. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                amount = float(input("Enter amount: "))
                description = input("Enter description: ")
                category = input("Enter category: ")
                self.add_expense(amount, description, category)
                print("Expense added successfully!")

            elif choice == '2':
                month = int(input("Enter month (1-12): "))
                year = int(input("Enter year (YYYY): "))
                total, category_summary = self.view_summary(month, year)
                print(f"\nSummary for {month}/{year}")
                print(f"Total Expenses: {total}")
                print("Category-wise breakdown:")
                for category, amount in category_summary.items():
                    print(f"{category}: {amount}")

            elif choice == '3':
                break

            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.run()
