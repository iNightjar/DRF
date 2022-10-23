import requests


headers = {'Authorization': 'Bearer 20018e27f7707f46a8e8418f993a643e9ecdc8c2'}

# do request though python clint to the django project
endpoint = "http://localhost:8000/api/products/"
# http://localhost:8000/admin/
# session -> post data
# selenuim


data = {
    "title": "visual studio code",

    "price": 200.2
}

get_response = requests.post(endpoint, json=data, headers= headers) # API Application programming interface
print(get_response.json())
