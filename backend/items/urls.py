from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverView, name='home'),  # home page

    path('create/', views.add_items, name='add_items'),  # create page

    path('all/', views.view_items, name='list_items'),  # list all items

    path('update/<int:pk>/', views.update_items,
         name='update_item'),  # update item

    path('item/<int:pk>/delete/', views.delete_items,
         name='update_item'),  # delete item

]
