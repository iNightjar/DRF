from rest_framework import serializers
from api.serializers import UserProductInlineSerializer
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    author = UserProductInlineSerializer(source='user', read_only=True)

    class Meta:
        model = Article
        fields = ['pk',
                  'author',
                  'title',
                  'body',
                  ]
