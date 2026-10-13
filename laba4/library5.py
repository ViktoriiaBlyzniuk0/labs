import psutil #інфо про ресурси комп'ютера

def run():
    print("Завантаження CPU:", psutil.cpu_percent(), "%")