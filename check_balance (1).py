from bot.client import client

account = client.futures_account_balance()

for asset in account:
    if asset["asset"] == "USDT":
        print(asset)