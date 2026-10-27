def logger(func):
    def wrapper():
        print("Початок роботи")
        func()
        print("Кінець роботи")
    return wrapper


@logger
def hello():
    print("Привіт!")


hello()