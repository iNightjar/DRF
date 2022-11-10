from django.shortcuts import render
from rest_framework import generics
from .serializers import ArticleSerializer
from .models import Article


class ArticelListView(generics.ListAPIView):
    queryset = Article.objects.public()
    serializer_class = ArticleSerializer


class ArticelDetialView(generics.RetrieveAPIView):
    queryset = Article.objects.public()
    serializer_class = ArticleSerializer
