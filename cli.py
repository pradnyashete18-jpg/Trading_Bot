import argparse

from bot.order import (
    place_market_order,
    place_limit_order
)

from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity
)

try:

    parser = argparse.ArgumentParser()

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    validate_side(args.side)
    validate_order_type(args.type)
    validate_quantity(args.quantity)

    if args.type == "MARKET":

        response = place_market_order(
            args.symbol,
            args.side,
            args.quantity
        )

    else:

        if args.price is None:
            raise ValueError(
                "Price required for LIMIT order"
            )

        response = place_limit_order(
            args.symbol,
            args.side,
            args.quantity,
            args.price
        )

    print("\nORDER SUCCESS")
    print("-" * 40)

    print("Order ID:", response["orderId"])
    print("Status:", response["status"])
    print("Executed Qty:", response["executedQty"])
    print("Avg Price:", response["avgPrice"])

except Exception as e:
    print("\nORDER FAILED")
    print(e)