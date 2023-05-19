from fastapi import Response
import openai
import gradio as gr
import jsonlines
import gradio
import spacy
openai.api_key = "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"
9

keywords = ["forex", "crypto", "stock", "market", "trading", "currency", "bitcoin", "equity", "shares",  "forex",
            "currency", "exchange rate", "pip", "lot", "spread", "margin", "leverage", "technical analysis",
            "fundamental analysis", "indicator", "trend", "chart", "candlestick", "support", "resistance",
            "crypto", "cryptocurrency", "bitcoin", "ethereum", "altcoin", "wallet", "blockchain", "mining",
            "trading", "stock", "equity", "share", "market", "stock exchange", "index", "commodity", "futures",
            "options", "bond", "yield", "dividend", "earnings", "valuation", "portfolio", "risk management",
            "order", "stop loss", "take profit", "trailing stop", "position sizing", "risk-reward ratio",
            "position management", "scalping", "day trading", "swing trading", "position trading", "long",
            "short", "buy", "sell", "bid", "ask", "liquidity", "volume", "price action", "moving average",
            "momentum", "oscillator", "RSI", "MACD", "Bollinger Bands", "Fibonacci retracement", "Elliott wave",
            "crossover", "divergence", "support and resistance levels", "whipsaw", "gap", "pullback", "breakout",
            "reversal", "continuation", "trend line", "candlestick pattern", "doji", "hammer", "engulfing", "harami",
            "morning star", "evening star", "bullish", "bearish", "uptrend", "downtrend", "sideways market",
            "volatility", "correlation", "diversification", "risk appetite", "fundamental news", "economic calendar",
            "central bank", "interest rate", "inflation", "unemployment", "GDP", "earnings report", "SEC filings",
            "insider trading", "market sentiment", "technical analysis software", "fundamental analysis software",
            "trading platform", "broker", "spread betting", "CFD", "liquidity provider", "market maker", "order book",
            "depth chart", "trade history", "position book", "risk management tool", "backtesting", "paper trading",
            "live trading"]

phrases = ["place a trade", "close a trade", "modify my strategy", "create a new strategy", "optimize my strategy", "backtest my strategy", "paper trade", "live trade",  "open a position on EUR/USD",     "sell 100 shares of AAPL",     "close all positions",     "adjust my stop loss to 1.2",     "create a buy order for BTC/USD at 40000",     "run a backtest on my trading system",     "execute a paper trade on GBP/JPY",     "place a limit order for EUR/USD at 1.2",    "exit all trades",    "start live trading on my account",    "change my leverage to 1:100",    "cancel all pending orders",    "add a new asset to my watchlist",    "remove TSLA from my watchlist",    "buy 10 contracts of the S&P500",    "sell 50 shares of AMZN",    "modify my take profit to 1.5",    "view my trading history",    "deposit funds into my account",    "withdraw 500 USD from my account"]
conversation_file = "trading_pal.jsonl"
intents_entities_file = "intents_entities.jsonl"

messages = [{"role": "system", "content": "You are Trading Pal 1.0, an expert automatic forex, crypto, and stock trading robot assistant"}]

def generate_response(user_input):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=user_input,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
        presence_penalty=0.5,
        frequency_penalty=0.5
    )
    ChatGPT_reply = response.choices[0].text.strip()

    # Check if the response contains any of the keywords
    restricted_flag = any(keyword in ChatGPT_reply.lower() for keyword in keywords)
    
    # Check if the user input contains any of the phrases
    if not restricted_flag and any(phrase in user_input.lower() for phrase in phrases):
        # Extract the intent and entities from the user's response
        # Here's an example of how you could extract the intent and entities using a natural language processing library like Spacy:
        
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(user_input)
        intent = doc[0].text 
        entities = [{"entity": ent.text, "type": ent.label_} for ent in doc.ents]
      
        # Save the intents and entities to a separate JSONL file
        with jsonlines.open(intents_entities_file, mode='a') as writer:
            writer.write({"intent": intent, "entities": entities})

        # Save the conversation to a separate JSONL file
        with jsonlines.open(conversation_file, mode='a') as writer:
            writer.write({"prompt": user_input, "completion": ChatGPT_reply})

        messages.append({"role": "assistant", "content": ChatGPT_reply})
        return ChatGPT_reply
    else:
        restricted_response = "Sorry, I can only provide information related to the forex, stock, and crypto markets."
        messages.append({"role": "assistant", "content": restricted_response})
        return restricted_response

demo = gradio.Interface(fn=generate_response, inputs = "text", outputs = "text", title = "Trading Pal 1.0")

demo.launch(share=True)