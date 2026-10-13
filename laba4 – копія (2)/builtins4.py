import json #перетвореня у формат JSON

def run():
    data = {"name": "Python", "version": 3}
    print(json.dumps(data, ensure_ascii=False))