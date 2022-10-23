import requests
from getpass import getpass


# do request though python clint to the django project


auth_endpoint = "http://localhost:8000/api/auth/"  # list all the products

username = input("What is your username ? \n")
password = getpass("What is your password? \n")
auth_response = requests.post(
    auth_endpoint, json={'username': username, 'password': password})
print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {
        "Authorization": f"Bearer {token}"
    }
    endpoint = "http://localhost:8000/api/products/"  # list all the products

    # API Application programming interface
    get_response = requests.get(endpoint, headers=headers)
    print(get_response.text)
