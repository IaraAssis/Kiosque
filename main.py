from management.product_handler import get_product_by_id, get_products_by_type
from management.product_handler import add_product, menu_report
from management.tab_handler import calculate_tab
from menu import products

if __name__ == "__main__":
    # Seus prints de teste aqui
    print(get_product_by_id(28))

if __name__ == "__main__":
    # Seus prints de teste aqui
    print(get_products_by_type("drink"))

if __name__ == "__main__":
    new_product = {
        "title": "X-Python",
        "price": 5.0,
        "rating": 5,
        "description": "Sanduiche de Python",
        "type": "fast-food"
    }
    print(add_product(products, **new_product))

if __name__ == "__main__":
    table_1 = [{"_id": 1, "amount": 5}, {"_id": 19, "amount": 5}]
    table_2 = [
        {"_id": 10, "amount": 3},
        {"_id": 20, "amount": 2},
        {"_id": 21, "amount": 5},
    ]

    print(calculate_tab(table_1))
    print(calculate_tab(table_2))


if __name__ == "__main__":
    products = [
        {"type": "Fruit", "price": 2.5},
        {"type": "Vegetable", "price": 1.8},
        {"type": "Fruit", "price": 3.0},
        # Adicione mais produtos conforme necessário
    ]
    print(menu_report())
