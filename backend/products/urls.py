from types import MappingProxyType
from django.urls import path
from . import views

urlpatterns = [
    path('', views.productCreateListAPIView.as_view()),

    path('<int:pk>/', views.productDetailsAPIView.as_view()),

    # path('listall/', views.productsList.as_view()),


]
