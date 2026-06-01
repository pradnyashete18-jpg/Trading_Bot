from bot.order import place_market_order

try:
    response = place_market_order(
        symbol="BTCUSDT",
        side="BUY",
        quantity=0.001
    )

    print("Order placed!")
    print(response)

except Exception as e:
    print("Error:")
    print(e)