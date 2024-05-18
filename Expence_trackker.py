
class Expense:
    def __init__(self, amount, category, description):
        self.amount = amount
        self.category = category
        self.description = description

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def calculate_total_expenses(self):
        return sum(expense.amount for expense in self.expenses)

    def view_expenses(self):
        for expense in self.expenses:
            print(f"Amount: ${expense.amount}, Category: {expense.category}, Description: {expense.description}")

def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Total Expenses")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter the amount: "))
            category = input("Enter the category: ")
            description = input("Enter the description: ")
            expense = Expense(amount, category, description)
            tracker.add_expense(expense)
            print("Expense added successfully!")
        elif choice == '2':
            if tracker.expenses:
                print("\nList of Expenses:")
                tracker.view_expenses()
            else:
                print("No expenses recorded yet.")
        elif choice == '3':
            total_expenses = tracker.calculate_total_expenses()
            print(f"\nTotal Expenses: ${total_expenses}")
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
