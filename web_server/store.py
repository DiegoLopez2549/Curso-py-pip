import requests

api_requests_categories = "https://api.escuelajs.co/api/v1/categories"


def get_categories():
    r = requests.get(api_requests_categories)
    print(r.status_code)
    print(r.text)
    categories = r.json()
    for category in categories:
        print(category["name"])
