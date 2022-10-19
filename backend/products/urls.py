from types import MappingProxyType
from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.productDetailAPIView.as_view()),

]
