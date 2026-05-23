from storage import load_db, save_db
from engine import add_transaction, get_stats, compound_interest, get_diversification
data = load_db()
while True:
    print("\n1. Add Transaction\n2. View Stats\n3. Calculate Compound Interest\n4. View Diversification\n5. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        t_type = input("Type (income/expense): ")
        if t_type not in ["income", "expense"]:
            print("Invalid type. Please enter 'income' or 'expense'.")
            continue
        try:
            amount = float(input("Amount: "))
        except ValueError:
            print("Invalid amount. Please enter a number.")
            continue
        category = input("Category: ")
        data = add_transaction(data, t_type, amount, category)
        save_db(data)
        print("Transaction added.")
    elif choice == "2":
        stats = get_stats(data)
        print(f"Total Profit: {stats['total_profit']}\nTotal Income: {stats['total_income']}\nTotal Expenses: {stats['total_expenses']}")
    elif choice == "3":
        amount = float(input("Principal Amount: "))
        rate = float(input("Annual Interest Rate (%): "))
        years = float(input("Years: "))
        periods = int(input("Compounding Periods per Year (default 1): ") or 1)
        result = compound_interest(amount, rate, years, periods)
        print(f"Future Value: {result:.2f}")
    elif choice == "4":
        diversification = get_diversification(data)
        if not diversification:
            print("No expenses to calculate diversification.")
        else:
            print("Diversification by Category:")
            for cat, perc in diversification.items():
                print(f"{cat}: {perc}%")
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid option. Please try again.")