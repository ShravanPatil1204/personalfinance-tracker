from transactions import add_income, add_expense
from reports import view_transactions, show_balance
from storage import load_data, save_data

def menu():
    data = load_data()

    while True:
        print("\n1. Add Income")
        print("2. Add Expense")
        print("3. View Transactions")
        print("4. Show Balance")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_income(data)
            save_data(data)

        elif choice == "2":
            add_expense(data)
            save_data(data)

        elif choice == "3":
            view_transactions(data)

        elif choice == "4":
            show_balance(data)

        elif choice == "5":
            break

        else:
            print("Invalid choice")

menu()