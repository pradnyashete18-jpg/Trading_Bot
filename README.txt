# Binance Futures Testnet Trading Bot

## Overview

This project is a Python-based CLI trading bot that places Market and Limit orders on Binance Futures Testnet (USDT-M). The application validates user input, handles API errors, logs requests and responses, and provides clear order execution output.

## Features

* Place MARKET orders
* Place LIMIT orders
* BUY and SELL support
* Input validation
* Error handling
* Logging of API requests and responses
* Binance Futures Testnet integration
* Command-line interface using argparse

## Project Structure

trading_bot/

bot/

* **init**.py
* client.py
* order.py
* validators.py
* loggingconfig.py

logs/

* tradingbot.log

cli.py
requirements.txt
README.md

## Installation

1. Clone the repository

2. Create a virtual environment

python -m venv venv

3. Activate the virtual environment

Windows:

venv\Scripts\activate

4. Install dependencies

pip install -r requirements.txt

## Environment Variables

Create a `.env` file in the project root:

API_KEY=your_testnet_api_key
API_SECRET=your_testnet_secret_key

## Running the Application

### Market Order

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

### Limit Order

python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 200000

## Example Output

ORDER SUCCESS

Order ID: 13690076832

Status: NEW

Executed Qty: 0.0000

Avg Price: 0.00

## Logging

All API requests, responses, and errors are written to:

logs/tradingbot.log

## Assumptions

* Binance Futures Testnet account is active.
* Valid API credentials are provided.
* User has sufficient testnet balance.
* Only MARKET and LIMIT orders are supported.
