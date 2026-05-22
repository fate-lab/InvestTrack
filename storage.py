import json
def save_db(data):
        with open("database.json", "w") as f:
            return json.dump(data, f)
def load_db():
    try:
        with open("database.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        default = {
            "balance": 0.0,
            "transactions": [],
            "investments": []
        }
        save_db(default)
        return default      