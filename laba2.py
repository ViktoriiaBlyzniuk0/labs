products = [
    {"id": 1, "name": "Ноутбук", "price": 25000.00, "quantity": 5},
    {"id": 2, "name": "Мишка", "price": 500.00, "quantity": 10},
    {"id": 3, "name": "Клавіатура", "price": 1200.00, "quantity": 7},
    {"id": 4, "name": "Навушники", "price": 1800.00, "quantity": 6}
]

cart = []


# Перегляд каталогу
def show_catalog():
    print("\n===== КАТАЛОГ =====")

    for product in products:
        print(
            f"{product['id']}. {product['name']} — "
            f"{product['price']:.2f} грн"
        )


# Додавання товару в кошик
def add_to_cart():
    show_catalog()

    product_id = int(input("Введіть ID товару: "))
    amount = int(input("Введіть кількість: "))

    for product in products:
        if product["id"] == product_id:

            if amount <= product["quantity"]:
                cart.append({
                    "id": product["id"],
                    "name": product["name"],
                    "price": product["price"],
                    "amount": amount
                })

                print("Товар додано до кошика!")
            else:
                print("Недостатньо товару на складі.")

            return

    print("Товар не знайдено.")


# Перегляд кошика
def show_cart():
    print("\n===== КОШИК =====")

    if len(cart) == 0:
        print("Кошик порожній.")
        return

    total = 0

    for item in cart:
        item_total = item["price"] * item["amount"]
        total += item_total

        print(
            f"{item['name']} — "
            f"{item['amount']} шт. — "
            f"{item_total:.2f} грн"
        )

    print(f"Разом: {total:.2f} грн")


# Видалення товару
def remove_from_cart():
    show_cart()

    if len(cart) == 0:
        return

    product_id = int(input("Введіть ID товару для видалення: "))

    for item in cart:
        if item["id"] == product_id:
            cart.remove(item)
            print("Товар видалено з кошика.")
            return

    print("Товар не знайдено в кошику.")


# Покупка
def buy_products():
    if len(cart) == 0:
        print("Кошик порожній.")
        return

    show_cart()

    answer = input("Купити товари? (так/ні): ")

    if answer == "так":

        # lambda-функція
        calculate_total = lambda item: item["price"] * item["amount"]

        total = sum(map(calculate_total, cart))

        for item in cart:
            for product in products:
                if product["id"] == item["id"]:
                    product["quantity"] -= item["amount"]

        print(f"Покупку здійснено!")
        print(f"До сплати: {total:.2f} грн")

        cart.clear()

    else:
        print("Покупку скасовано.")


# Вхід адміністратора
def admin_login():
    login = input("Логін: ")
    password = input("Пароль: ")

    if login == "admin" and password == "1234":
        print("\nВхід успішний!")
        show_stock()
    else:
        print("Неправильний логін або пароль.")


# Перегляд залишків
def show_stock():
    print("\n===== ЗАЛИШКИ =====")

    for product in products:
        print(
            f"{product['name']} — "
            f"{product['quantity']} шт."
        )


# Головна функція
def main():

    while True:

        print("\n===== МІНІ-МАГАЗИН =====")
        print("1. Переглянути каталог")
        print("2. Додати товар у кошик")
        print("3. Переглянути кошик")
        print("4. Видалити товар з кошика")
        print("5. Купити товари")
        print("6. Увійти як адміністратор")
        print("0. Вийти")

        choice = input("Оберіть дію: ")

        if choice == "1":
            show_catalog()

        elif choice == "2":
            add_to_cart()

        elif choice == "3":
            show_cart()

        elif choice == "4":
            remove_from_cart()

        elif choice == "5":
            buy_products()

        elif choice == "6":
            admin_login()

        elif choice == "0":
            print("До побачення!")
            break

        else:
            print("Невірний вибір.")


# Точка входу
if __name__ == "__main__":
    main()