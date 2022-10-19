from types import MappingProxyType
from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_create_view),

    path('<int:pk>/', views.productDetailAPIView.as_view()),

    path('listall/', views.productsList.as_view()),
]
