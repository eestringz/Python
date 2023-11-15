from django.shortcuts import render
from django.shortcuts import get_list_or_404, get_object_or_404

from .models import Category, Post, Comment
from .serializers import PostListSerializer, CategorySerializer, PostSerializer, CommentSerialzer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET','POST'])
def post_list(request):
  if request.method == 'GET':
    posts = Post.objects.all()
    serializer = PostListSerializer(posts, many=True)
    return Response(serializer.data)
  
  elif request.method == 'POST':
    category = Category.objects.get(pk=request.data.get('category'))
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
       serializer.save(category=category)
       return Response(serializer.data, status=status.HTTP_201_CREATED)
  

@api_view(['GET','POST'])
def category_list(request):
  if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
  
  if request.method == 'POST':
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def post_detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.method == 'GET':
        serialzer = PostSerializer(post)
        return Response(serialzer.data)
    elif request.method == 'PUT':
        category = Category.objects.get(pk=request.data.get('category'))
        serialzer = PostSerializer(data=request.data, instance=post)
        if serialzer.is_valid(raise_exception=True):
            serialzer.save(category=category)
            return Response(serialzer.data)
    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


@api_view(['POST'])
def comment_create(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    serializer = CommentSerialzer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(post=post)
        return Response(serializer.data)
    
@api_view(['DELETE'])
def comment_delete(request, post_pk, comment_pk):
    post = Post.objects.get(pk=post_pk)
    comment = post.comment_set.get(pk=comment_pk)
    comment.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)