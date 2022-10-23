from django.urls import path
from . import views
# from .views import api_home
from rest_framework.authtoken.views import obtain_auth_token

# localhost:8000/api/
urlpatterns = [

    path('', views.api_home),
    path('auth/', obtain_auth_token),
    

]