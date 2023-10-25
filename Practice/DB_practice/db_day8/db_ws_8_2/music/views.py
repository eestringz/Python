from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import MusicListSerializer, MusicSerializer
from .models import Music


@api_view(['GET','POST'])
def music_list(request):
    if request.method == 'GET':
        musics = Music.objects.all()
        serializer = MusicListSerializer(musics, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = MusicSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET','PUT','DELETE'])
def  music_detail(request, music_pk):
    music = Music.objects.get(pk = music_pk)
    if request.method == 'GET':
        serializer = MusicSerializer(music)
        return Response(serializer.data)    
    
    elif request.method =='PUT':
        serializer = MusicSerializer(music, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        message = f'음악 {music.pk}번이 삭제되었습니다. '
        music.delete()
        return Response(data={'message':message}, status=status.HTTP_204_NO_CONTENT)
