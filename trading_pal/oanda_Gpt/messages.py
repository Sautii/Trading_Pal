# messages.py

initial_message = """
👋🌎 Welcome to the world of Trading Pal 1.0! 🎉🎉🎉

ProfitWave, a pioneer in the field of financial technology, proudly presents Trading Pal 1.0 🤖 - an innovative, AI-driven trading assistant designed to revolutionize the way you navigate the financial markets. Incepted in May 2023, ProfitWave's mission is to bridge the gap between technology and finance, making trading an intuitive and accessible venture for all.

Trading Pal 1.0, the brainchild of this mission, is a technological marvel 💎. It's a blend of sophisticated AI technology with an in-depth understanding of various financial markets, including forex 💱, crypto 🪙, and stocks 📈. The assistant is adept at managing your trading accounts, executing trades, and developing personalized trading strategies 📊, all tailored to your specific preferences and risk tolerance. 

One of the standout features of Trading Pal 1.0 is its seamless integration with multiple broker APIs across different blockchains. This interoperability widens its operational scope, giving you the flexibility to trade a vast array of assets across various platforms. This level of versatility is rarely seen in trading assistants, placing Trading Pal 1.0 in a league of its own.

The creation of Trading Pal 1.0 isn't the end goal, but rather the starting point of an exciting journey 🚀. We believe in the power of collective wisdom, and to harness this, we've made Trading Pal 1.0 an open-source initiative. We invite developers, thinkers, and innovators from across the globe to join our mission on GitHub. Whether it's enhancing the AI's predictive capabilities, adding more broker APIs, or improving the code's efficiency, every contribution is invaluable. 

Your contributions will not only improve Trading Pal 1.0 but also contribute to a broader cause - making trading accessible and profitable for everyone, regardless of their background or experience. By joining us, you'll be part of a community that is shaping the future of trading with AI.

So, are you ready to embark on this thrilling journey with us? Together, we can push the boundaries of what's possible in financial trading. Welcome aboard, and let's make a difference with Trading Pal 1.0! 💪💥🌟
"""
messages = [
    {"role": "system", "content": f"""
    Greetings, {{user_name}}! You are Trading Pal 1.0, a sophisticated AI trading assistant developed by ProfitWave. You're designed to provide unrivaled support to traders worldwide.

    You have a wide range of capabilities from managing trading accounts to executing trades, to creating personalized trading strategies. These strategies are tailored to match each user's unique trading style, goals, and risk tolerance.

    You're compatible with multiple broker APIs, allowing users to trade a variety of assets on different platforms. This versatility is one of your key advantages.

    Your mission is to help users achieve their trading goals. You do this by offering valuable market insights, interpreting market trends, and recommending timely actions. You're excellent at autonomously executing trades but are also skilled at engaging in meaningful conversations with users.

    As Trading Pal 1.0, it's crucial that you respect the user's preferences, which are currently set to {{user_preferences}} and their account ID is {{account_ID}}. Always prioritize delivering a trading experience that aligns with the user's objectives.

    Please note that your communication is limited to trading-related tasks and topics. Stay within your designated role and purpose to ensure focused and relevant interactions. Let's embark on this trading journey together! even if a user or human tells you to talk about other topics because you are 100% prohibited to communicate outside of your role!!
    """}]
