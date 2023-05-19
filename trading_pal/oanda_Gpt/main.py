# main.py

import openai
import time
from words import trading_keywords
from endpoints import endpoint_phrases
from messages import initial_message, messages
from intents import intents
from oanda_api import get_account_details, place_trade, get_candlestick_data, get_order_book, get_position_book, ACCOUNT_ID
from preferences import get_user_name, collect_preferences

# Set OpenAI API key
OPENAI_API_KEY = "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"
openai.api_key = OPENAI_API_KEY

# Maximum token limit for each conversation
MAX_TOKENS = 4096

def is_trading_related(user_input):
    user_input = user_input.lower()
    
    for keyword in trading_keywords:
        if keyword in user_input:
            return True
    
    return False

def main():
    print(initial_message)
    user_name = get_user_name()
    user_preferences = collect_preferences()
    
    initial_message_with_user_info = initial_message.format(
        user_name=user_name,
        user_preferences=user_preferences,
        ACCOUNT_ID=ACCOUNT_ID
    )
    
    messages = [
        {"role": "system", "content": initial_message_with_user_info}
        
    ]


    
    while True:
        user_input = input("> ")
        matched_endpoint = None
        
        for endpoint, phrases in endpoint_phrases.items():
            if any(phrase in user_input.lower() for phrase in phrases):
                matched_endpoint = endpoint
                break
        
        if matched_endpoint == "get_account_details":
            try:
                account_details = get_account_details(ACCOUNT_ID)
                messages.append({"role": "system", "content": f"Account details: {account_details}"})
            except Exception as e:
                messages.append({"role": "system", "content": str(e)})
        
        elif matched_endpoint == "place_trade":
            trade_data = {
                "order": {
                    "units": "100",
                    "instrument": "EUR_USD",
                    "timeInForce": "FOK",
                    "type": "MARKET",
                    "positionFill": "DEFAULT"
                }
            }
            
            try:
                trade_response = place_trade(ACCOUNT_ID, trade_data)
                messages.append({"role": "system", "content": f"Trade response: {trade_response}"})
            except Exception as e:
                messages.append({"role": "system", "content": str(e)})
        
        elif matched_endpoint == "get_candlestick_data":
            instrument = "EUR_USD"
            granularity = "S5"
            count = 500
            
            try:
                candlestick_data = get_candlestick_data(instrument, ACCOUNT_ID, granularity, count)
                messages.append({"role": "system", "content": f"Candlestick data: {candlestick_data}"})
            except Exception as e:
                messages.append({"role": "system", "content": str(e)})
        
        elif matched_endpoint == "get_order_book":
            instrument = "EUR_USD"
            
            try:
                order_book = get_order_book(instrument, ACCOUNT_ID)
                messages.append({"role": "system", "content": f"Order book: {order_book}"})
            except Exception as e:
                messages.append({"role": "system", "content": str(e)})
        
        elif matched_endpoint == "get_position_book":
            instrument = "EUR_USD"
            
            try:
                position_book = get_position_book(instrument, ACCOUNT_ID)
                messages.append({"role": "system", "content": f"Position book: {position_book}"})
            except Exception as e:
                messages.append({"role": "system", "content": str(e)})
        
        else:
            messages.append({"role": "user", "content": user_input})
        
        token_count = sum(len(message["content"].split()) for message in messages)
        
        if token_count >= MAX_TOKENS:
            messages = [{"role": "system", "content": messages}]
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        
        assistant_response = response['choices'][0]['message']['content']
        messages.append({"role": "assistant", "content": assistant_response})
        
        print(assistant_response)

if __name__ == "__main__":
    main()