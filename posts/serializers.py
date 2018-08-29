# posts/serializers.py
from rest_framework import serializers
from . import models


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title', 'upload', 'date',)
        model = models.Post
