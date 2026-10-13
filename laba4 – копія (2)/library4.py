from tabulate import tabulate #таблиці

def run():
    print(tabulate([["Python", "Мова"]], headers=["Назва", "Тип"]))