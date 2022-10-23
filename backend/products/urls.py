from types import MappingProxyType
from django.urls import path
from . import views

urlpatterns = [

    # FBV -> create_list_FBV
    # list all, post requuests to create new product
    path('', views.product_list_create_view, name='product-list'),
    path('<int:pk>/', views.product_detail_view, name='product-detail'),  # list spicif product
    path('<int:pk>/update/', views.product_update_view, name='product-edit'),  # update spicif product
    path('<int:pk>/delete/', views.product_delete_view, name='product-delete'),  # delete spicif product
]
