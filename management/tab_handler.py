from menu import products


def calculate_tab(consumptions: list) -> dict:
    prices = {product["_id"]: product["price"] for product in products}

    subtotal = sum(
        prices[consumption["_id"]] * consumption["amount"]
        for consumption in consumptions
    )

    subtotal = round(subtotal, 2)

    return {"subtotal": f"${subtotal}"}
