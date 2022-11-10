from telnetlib import STATUS
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import productSerializer
from products.models import products

# Actual django models using!!
@api_view(["POST"])
def api_home(request, *args, **kwargs):
    
    """
    API VIEW WITH DRF
    """
    # # doing it with django
    # if request.method != "POST":
    #     return Response({"detial": "GET is not allowed"}, status=405)
    # data = request.data
    # return JsonResponse(data)

    serializer = productSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        # instance = form.save()
        print(serializer.data)
        return Response(serializer.data)
    return Response({"invalid": "not good data"}, status=400)
       
       
       
       
       
       
       
       
       
       
       
       
        # data['headers'] = dict(request.headers)
        # print(data)
        # data = dict(data)
    # json_data_str = json.dumps(data)
    # model intanse (model_data)
    # turn a python dict
    # return JSON to my clint
    # serialzation
    # return JsonResponse(data , headers={"contect_type": "application/json"})
    
    # data['id'] = model_data.id  # type: ignore
    # data['title'] = model_data.title
    # data['content'] = model_data.content
    # data['price'] = model_data.price
    # data['params'] = dict(request.GET)

 
    
    
    # # request -> HttpRequest -> Django
    # # print(dir(requst))
    # # reqeust.body
    # print(request.GET) # url query params
    # # print(request.POST)

    # body = request.body # byte string of json data
    # data = {}
    # try:
    #     data = json.loads(body) # string of json data -> python dictionary

    # except:
    #     pass
    # print(data)
    # # return JsonResponse({"message": "hi there, this is your django api response!!"})
    # # d = request.headers # request.META in old versions
    # data['params'] = dict(request.GET)
    # data['headers'] = dict(request.headers)
    # data['content_type'] = request.content_type
    # # print(data)
    # return JsonResponse(data)
 