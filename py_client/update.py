import requests


# do request though python clint to the django project
endpoint = "http://localhost:8000/api/products/1/update/"  # list all the products


data = {
    "title": "Hello darkness my old friend",

    "price": "100",
}
# API Application programming interface
get_response = requests.put(endpoint, json=data)
print(get_response.json())
