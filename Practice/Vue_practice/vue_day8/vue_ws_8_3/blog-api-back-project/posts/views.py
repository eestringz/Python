from django.shortcuts import render
from django.shortcuts import get_list_or_404, get_object_or_404

from .models import Category, Post, Comment
from .serializers import PostListSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def post_list(request):
  if request.method == 'GET':
    posts = Post.objects.all()
    serializer = PostListSerializer(posts, many=True)
    return Response(serializer.data)