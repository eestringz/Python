from rest_framework import serializers
from .models import Category, Post, Comment

class PostListSerializer(serializers.ModelSerializer):
  class Meta:
    model= Post
    fields = ('id', 'title', 'category',)