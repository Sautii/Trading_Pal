 # Trading Pal 
(https://github.com/Deion24x/TradingPal-/assets/128738398/35db9ba7-401c-4f1e-b916-4d5b98b57b79)
Trading Pal is a powerful, flexible, and 
easy-to-use trading bot designed for Forex trading. With Trading Pal, you can automate your trading strategies, manage your risk, and monitor your performance, all from the comfort of your own command line.

## Features

- **Automated Trading Strategies:** Trading Pal allows you to implement and automate a variety of trading strategies. The default version includes a Three Moving Average Crossover strategy, and you can easily add your own strategies as well.

- **Risk Management:** Trading Pal includes built-in tools for managing your risk, including stop-loss and take-profit functionality.

- **Real-Time Data Streaming:** Trading Pal uses the OANDA API to stream real-time Forex data, allowing your strategies to respond instantly to market conditions.

- **Conversation Model:** Trading Pal uses an AI-powered conversation model, allowing you to interact with the bot using natural language. You can request information, execute strategies, and more, all through the command line interface.

## Getting Started

To get started with Trading Pal, you'll need Python 3.7 or later and an OANDA account. Once you've set up your environment, you can install Trading Pal by cloning this repository and installing the required dependencies:

```bash
git clone https://github.com/username/trading-pal.git
cd trading-pal
pip install -r requirements.txt
```

You'll also need to set up your OANDA API key as an environment variable. See [this guide](link-to-guide) for more information.

## Usage

To start Trading Pal, run the following command:

```bash
python main.py
```

You can interact with Trading Pal using the command line interface. For example, to execute the Three Moving Average Crossover strategy, you can say:

```
Trading Pal, can you execute the 3_sma_crossover_strategy?
```

Trading Pal will then ask for your risk management strategy. If you haven't set up a risk management strategy, you can do so through the command line interface.

## Contributing

Contributions to Trading Pal are welcome! Please see the [Contributing Guide](link-to-contributing-guide) for more information.

## Security

Security is a top priority for Trading Pal. Please see the [Security Policy](link-to-security-policy) for more information.

## License

Trading Pal is licensed under the [MIT License](link-to-license).
