from transactions import load_transactions, save_transactions, add_transaction
from analysis import calculate_summary
from visualization import visualize_data

def main():
    transactions = load_transactions()

    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Summary")
        print("4. Visualize Data")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            amount = float(input("Enter income amount: "))
            category = input("Enter income category: ")
            add_transaction(transactions, amount, category, 'Income')
            save_transactions(transactions)
        elif choice == '2':
            amount = float(input("Enter expense amount: "))
            category = input("Enter expense category: ")
            add_transaction(transactions, amount, category, 'Expense')
            save_transactions(transactions)
        elif choice == '3':
            total_income, total_expenses, net_savings = calculate_summary(transactions)
            print(f"Total Income: ${total_income}")
            print(f"Total Expenses: ${total_expenses}")
            print(f"Net Savings: ${net_savings}")
        elif choice == '4':
            visualize_data(transactions)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()