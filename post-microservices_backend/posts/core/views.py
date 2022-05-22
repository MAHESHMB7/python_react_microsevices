from ast import Return
from django.shortcuts import render
from rest_framework.views import APIView
from .models import Post
from .serializers import PostSerializer
from rest_framework.response import Response

class PostAPIView(APIView):
    def get(self,request):
        posts=Post.objects.all()
        serializer=PostSerializer(posts,many=True)
        return Response(serializer.data)