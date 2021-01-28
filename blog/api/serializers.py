from rest_framework import serializers
from blog.models import *


class SingleArticleSerializer(serializers.Serializer):
    title = serializers.CharField(required=True,max_lenght=128,alow_null=False, allow_blank=False)
    cover = serializers.CharField(required=True,max_lenght=200,alow_null=False, allow_blank=False)
    content = serializers.CharField(required=True,max_lenght=200,alow_null=False, allow_blank=False)
    create_at = serializers.DateTimeField(required=True,alow_null=False, allow_blank=False)


class SubmitAricleSerializer(serializers.Serializer):
    title = serializers.CharField(required=True,max_lenght=128,alow_null=False, allow_blank=False)
    cover = serializers.FileField(required=True)
    content = serializers.CharField(required=True,max_lenght=200,alow_null=False, allow_blank=False)
    category_id = serializers.IntegerField(required=True,)
    author_id = serializers.IntegerField(required=True,)
    promote = serializers.BooleanField(required=True,)



class UpdateArticleSerializers(serializers.Serializer):
    article_id = serializers.IntegerField(required=True)
    cover = serializers.FileField(required=True)


class DeleteArticleSerializers(serializers.Serializer):
    article_id = serializers.IntegerField(required=True)
