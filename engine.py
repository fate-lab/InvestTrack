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
