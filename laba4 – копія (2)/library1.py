import requests #запити через інтернет

def run():
    try:
        response = requests.get("https://example.com", timeout=5)
        print("requests:", response.status_code)
    except requests.RequestException:
        print("Сайт недоступний")