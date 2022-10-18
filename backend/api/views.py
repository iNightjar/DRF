from django.http import JsonResponse  # it's built in with django. cool
import json

# Actual django models using!!

def api_home(request, *args, **kwargs):
    # request -> HttpRequest -> Django
    # print(dir(requst))
    # reqeust.body
    print(request.GET) # url query params
    # print(request.POST)

    body = request.body # byte string of json data
    data = {}
    try:
        data = json.loads(body) # string of json data -> python dictionary

    except:
        pass
    print(data)
    # return JsonResponse({"message": "hi there, this is your django api response!!"})
    # d = request.headers # request.META in old versions
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    # print(data)
    return JsonResponse(data)
 