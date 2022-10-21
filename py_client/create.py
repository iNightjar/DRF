import requests


# do request though python clint to the django project
endpoint = "http://localhost:8000/api/products/"

data = {
    "title": "visual studio code",

    "price": "101002",
}

get_response = requests.post(endpoint, json=data)  # API Application programming interface
print(get_response.json())
