import validators #правильність формату даних

def run():
    print("Email правильний:", validators.email("test@example.com"))