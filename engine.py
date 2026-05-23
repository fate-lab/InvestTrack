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