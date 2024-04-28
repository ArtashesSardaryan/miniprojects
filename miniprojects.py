import requests
import json
import time

def fetch_cryptocurrency_data():
    try:
        url = "https://api.coingecko.com/api/v3/coins/markets"
        params = {
            "vs_currency": "usd",
            "order": "market_cap_desc",
            "per_page": "10",
            "page": "1",
            "sparkline": "false",
            "price_change_percentage": "24h"
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            print("Failed to fetch data. Status code:", response.status_code)
            return None
    except Exception as e:
        print("An error occurred:", e)
        return None

def display_statistics(data, filter_name=None, filter_value=None):
    print("---------------------------------------------------------------------------")
    print("Name\t\tSymbol\tPrice (USD)\tMarket Cap\tVolume (24h)\tPrice Change (24h)")
    print("---------------------------------------------------------------------------")
    for crypto in data:
        if filter_name and filter_name.lower() not in crypto['name'].lower():
            continue
        if filter_value and float(crypto['current_price']) < filter_value:
            continue
        print(f"{crypto['name']}\t{crypto['symbol']}\t${crypto['current_price']}\t{crypto['market_cap']}\t{crypto['total_volume']}\t{crypto['price_change_percentage_24h']}%")
    print("---------------------------------------------------------------------------")

def main():
    while True:
        data = fetch_cryptocurrency_data()
        if data:
            display_statistics(data)
        time.sleep(5)

if __name__ == "__main__":
    main()
