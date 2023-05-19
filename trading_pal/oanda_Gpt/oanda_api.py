# oanda_api.py

import requests

BASE_URL = "https://api-fxpractice.oanda.com"
ACCOUNT_ID = "your id here"

OANDA_API_KEY = "your api here"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {OANDA_API_KEY}",
    "Connection": "keep-alive"
}
ACCOUNT_ID = "101-001-25239678-001"
def get_account_details(account_id):
    url = f"{BASE_URL}/v3/accounts/{account_id}"
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to get account details. Status code: {response.status_code}")

def place_trade(account_id, trade_data):
    url = f"{BASE_URL}/v3/accounts/{account_id}/orders"
    response = requests.post(url, headers=headers, json=trade_data)
    
    if response.status_code == 201:
        return response.json()
    else:
        raise Exception(f"Failed to place trade. Status code: {response.status_code}")







import requests

def get_candlestick_data(instrument, bearer_token, granularity='S5', count=500):
    url = f"{BASE_URL}/v3/instruments/{instrument}/candles"
    headers = {"Authorization": f"Bearer {bearer_token}", "Accept-Datetime-Format": "UNIX"}
    params = {"granularity": granularity, "count": count}
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code != 200:
        raise Exception(f"Request failed with status {response.status_code}")
    
    return response.json()

def get_order_book(instrument, bearer_token):
    url = f"{BASE_URL}/v3/instruments/{instrument}/orderBook"
    headers = {"Authorization": f"Bearer {bearer_token}", "Accept-Datetime-Format": "UNIX"}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        raise Exception(f"Request failed with status {response.status_code}")
    
    return response.json()

def get_position_book(instrument, bearer_token):
    url = f"{BASE_URL}/v3/instruments/{instrument}/positionBook"
    headers = {"Authorization": f"Bearer {bearer_token}", "Accept-Datetime-Format": "UNIX"}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        raise Exception(f"Request failed with status {response.status_code}")
    
    return response.json()
