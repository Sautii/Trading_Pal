# preferences.py

def get_user_name():
    user_name = input("Before we start, may I know your name? ")
    return user_name




# Get the user's account ID
ACCOUNT_ID = input("Please enter your account ID: ")


def collect_preferences():
    preferences = {}
    
    print("\nFirst, we need to understand more about your trading style and goals. This will help us provide a personalized trading experience for you.")
    
    trading_styles = ["Scalping", "Day Trading", "Swing Trading", "Position Trading"]
    trading_goals = ["Short-term profit", "Long-term investment", "Portfolio diversification"]
    risk_tolerance = ["Low", "Medium", "High"]
    preferred_markets = ["Forex", "Crypto", "Stocks"]
    investment_amount = ["Less than $1,000", "$1,000 - $10,000", "More than $10,000"]
    time_commitment = ["Less than 1 hour a day", "1-3 hours a day", "Full-time"]
    
    preferences_collections = {
        "trading_style": trading_styles,
        "trading_goals": trading_goals,
        "risk_tolerance": risk_tolerance,
        "preferred_markets": preferred_markets,
        "investment_amount": investment_amount,
        "time_commitment": time_commitment
    }
    
    for preference, options in preferences_collections.items():
        while True:
            for i, option in enumerate(options, 1):
                print(f"{i}. {option}")
            
            user_choice = input(f"Please choose your {preference.replace('_', ' ')} (1-{len(options)}): ")
            
            if user_choice.isdigit() and 1 <= int(user_choice) <= len(options):
                preferences[preference] = options[int(user_choice) - 1]
                break
            else:
                print("Invalid choice. Please enter a number corresponding to the options listed.")
    
    return preferences
