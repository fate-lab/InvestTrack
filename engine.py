from datetime import datetime
def add_transaction(data, trans_type, amount, category):
    transactions = data["transactions"]
    data["transactions"].append({
        "id": max(t["id"] for t in transactions) + 1 if transactions else 1,
        "type": trans_type,
        "amount": amount,
        "category": category,
        "date": datetime.now().isoformat()})
    data["balance"] += amount if trans_type == "income" else -amount
    return data
def add_investment(data, asset, ticker, shares, buy_price, yearly_yield):
    investments = data["investments"]
    data["investments"].append({
        "id": max(i["id"] for i in investments) + 1 if investments else 1,
        "asset": asset,
        "ticker": ticker,
        "shares": shares,
        "buy_price": buy_price,
        "yearly_yield": yearly_yield,
        "date": datetime.now().isoformat()})
    return data 
def get_stats(data):
    income = sum(t["amount"] for t in data["transactions"] if t["type"] == "income")
    expenses = sum(t["amount"] for t in data["transactions"] if t["type"] == "expense")
    return {
        "total_profit": income - expenses,
        "total_income": income,
        "total_expenses": expenses
    }
def compound_interest(amount, rate, years, periods_per_year=1):
    ## rate in %
    if periods_per_year <= 0:
        raise ValueError("periods_per_year must be a positive integer")
    period_rate = rate / 100.0 / periods_per_year
    periods = int(years * periods_per_year)
    return amount * (1 + period_rate) ** periods
def get_invest_forecast(data, years):
    forecast = []
    for inv in data["investments"]:
        future_value = compound_interest(
            inv["buy_price"] * inv["shares"],
            inv["yearly_yield"],
            years
        )
        forecast.append({
            "asset": inv["asset"],
            "ticker": inv["ticker"],
            "future_value": round(future_value, 2)
        })
    return forecast
def get_diversification(data):
    category_totals = {}
    for t in data["transactions"]:
        if t["type"] == "expense":
            category_totals[t["category"]] = category_totals.get(t["category"], 0) + t["amount"]
    total_expenses = sum(category_totals.values())
    if total_expenses == 0:
        return {}
    return {cat: round((amt / total_expenses) * 100, 2) for cat, amt in category_totals.items()}
def get_real_profit(investment, current_price):
    return (current_price - investment["buy_price"]) * investment["shares"]