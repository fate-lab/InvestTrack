import requests
import os
from dotenv import load_dotenv
load_dotenv()
def get_current_price(ticker):
    try:
        url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={ticker}&apikey={os.getenv('API_KEY')}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        price = data["Global Quote"]["05. price"]
        return float(price)
    except (requests.RequestException, KeyError):
        return None