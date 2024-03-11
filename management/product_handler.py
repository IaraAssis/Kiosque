from menu import products


def get_product_by_id(product_id: int) -> dict:
    if type(product_id) is not int:
        raise TypeError("product id must be an int")
    for product in products:
        if product["_id"] == product_id:
            return product
    return {}


def get_products_by_type(product_type: str):
    filtered_types = []
    if type(product_type) is not str:
        raise TypeError("product type must be a str")
    for product in products:
        if product["type"] == product_type:
            filtered_types.append(product)
    return filtered_types


def add_product(menu: list, **product_data: dict) -> dict:
    if not menu:
        id = 1
    else:
        id = max(product["_id"] for product in menu) + 1

    product_data["_id"] = id
    menu.append(product_data)
    return product_data


def menu_report() -> str:
    product_count = len(products)
    total_price = sum(product["price"] for product in products)

    types_count = {}
    for product in products:
        product_type = product.get("type", "Undefined")
        types_count[product_type] = types_count.get(product_type, 0) + 1

    most_common_type = max(types_count, key=types_count.get)

    average_price = round(total_price / product_count, 2)

    report_string = f"Products Count: {product_count} - Average Price: ${round(average_price, 1)} - Most Common Type: {most_common_type}"

    return report_string
