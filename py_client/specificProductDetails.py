import requests


# do request though python clint to the django project
endpoint = "http://localhost:8000/api/products/2/"

get_response = requests.get(endpoint)  # API Application programming interface

# params = {"abc": 123},
# print(get_response.headers)
print(get_response.text)
print(get_response.json())  # print the raw text response code
