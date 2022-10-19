import requests


# do request though python clint to the django project
endpoint = "http://localhost:8000/api/products/listall/"  # list all the products



# API Application programming interface
get_response = requests.get(endpoint)
print(get_response.json())
