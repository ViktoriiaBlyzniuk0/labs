# Дані користувачів
users = {"vika":
    {
        "password": "1234",
        "grades": [12, 10, 8, 5, 3, 11]
    },
    "ivan": {
        "password": "qwerty",
        "grades": [9, 7, 4, 10, 6, 2]
    },
    "anna": {
        "password": "1111",
        "grades": [12, 11, 10, 8, 9, 12]
    },
    "max": {
        "password": "pass123",
        "grades": [4, 3, 6, 7, 5, 2]
    }
}

# Введення логіна та пароля
login = input("Введіть логін: ")   #дані з клавіатури через термінал
password = input("Введіть пароль: ")

# Перевірка даних
if login in users and users[login]["password"] == password: #адаємо умову якщо
    print("\nВхід виконано успішно!")

    grades = users[login]["grades"] #Знайти користувача, якого ввів користувач, і взяти його пароль

    # Виведення всіх оцінок
    print("Ваші оцінки:", grades)

    # Підрахунок оцінок
    satisfactory = 0
    unsatisfactory = 0

    for grade in grades:
        if 5 <= grade <= 12:
            satisfactory += 1
        elif 1 <= grade <= 4:  #інакше, якщо
            unsatisfactory += 1

    print("Кількість задовільних оцінок (5-12):", satisfactory)
    print("Кількість незадовільних оцінок (1-4):", unsatisfactory)

else:
    print("\nНеправильний логін або пароль!")