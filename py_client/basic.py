from calendar import HTMLCalendar
import requests

# endpoints is like url but many actauly, working with restframework,
# we will have alot of endpoint with the project
# endpoint = "https://httpbin.org/status/200/"


# do request though python clint to the django project
endpoint = "http://localhost:8000/api/"

get_response = requests.get(endpoint, json={
                            "product_id": 123})  # API Application programming interface

# params = {"abc": 123},
# print(get_response.headers)
# print(get_response.text)  # print the raw text response code

print(get_response.json()) # print in json format

# print(get_response.status_code)

# HTTP Request > HMTL
# Rest API HTTP Request > JSON


# {
#     "args": {},
#     "data": "",
#     "files": {},
#     "form": {},
#     "headers": {
#         "Accept": "*/*",
#         "Accept-Encoding": "gzip, deflate",
#         "Host": "httpbin.org",
#         "User-Agent": "python-requests/2.28.1",
#         "X-Amzn-Trace-Id": "Root=1-634e23d7-1018e13b682431bc04b8c047"
#     },
#     "json": null,
#     "method": "GET",
#     "origin": "41.34.212.3",
#     "url": "https://httpbin.org/anything"
# }

# JavaScript Object Notation ~ Python Dict

# {'args': {}, 'data': '', 'files': {}, 'form': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.28.1',
#                                                               'X-Amzn-Trace-Id': 'Root=1-634e24ca-6914cdf728561f3110acc6f1'}, 'json': None, 'method': 'GET', 'origin': '41.34.212.3', 'url': 'https://httpbin.org/anything'}
