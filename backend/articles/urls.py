from django.urls import path
from . import views

urlpatterns = [

    path('', views.ArticelListView.as_view(), name='aricle-list'),
    path('<int:pk>/', views.ArticelDetialView.as_view(), name='aricle-detail'),

]