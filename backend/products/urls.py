from types import MappingProxyType
from django.urls import path
from . import views

urlpatterns = [

    # FBV -> create_list_FBV
    path('', views.product_list_create_view),
    path('<int:pk>/', views.product_detail_view),
]
