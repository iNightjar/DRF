from django.http import JsonResponse # it's built in with django. cool

def api_home(request, *args, **kwargs):
    return JsonResponse({"message": "hi there, this is your django api response!!"})