from storage import load_db, save_db
from engine import add_transaction, get_stats, compound_interest, get_diversification, add_investment, get_invest_forecast
data = load_db()
while True:
    print("\n1. Add Transaction\n2. View Stats\n3. Calculate Compound Interest\n4. View Diversification\n5. Manage Investments\n6. Exit")
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
        print("1. Add Investment\n2. View Investment Forecast")
        inv_choice = input("Choose an option: ")
        if inv_choice == "1":
            asset = input("Asset Name: ")
            ticker = input("Ticker Symbol: ")
            try:
                shares = float(input("Number of Shares: "))
                buy_price = float(input("Buy Price per Share: "))
                yearly_yield = float(input("Expected Yearly Yield (%): "))
            except ValueError:
                print("Invalid input. Please enter numbers for shares, price, and yield.")
                continue
            data = add_investment(data, asset, ticker, shares, buy_price, yearly_yield)
            save_db(data)
            print("Investment added.")
        elif inv_choice == "2":
            years = float(input("Years to Forecast: "))
            forecast = get_invest_forecast(data, years)
            if not forecast:
                print("No investments to forecast.")
            else:
                print("Investment Forecast:")
                for f in forecast:
                    print(f"{f['asset']} ({f['ticker']}): Future Value = {f['future_value']}")
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid option. Please try again.")