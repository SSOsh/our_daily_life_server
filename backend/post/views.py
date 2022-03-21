from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *

#from .models import Post
#from .serializers import PostSerializer

class UserView(APIView):
    """
    POST /use
    """
    def post(self, request):
        userSerializer = UserSerializer(data=request.data)

        if userSerializer.is_valid():
            userSerializer.save()
            return Response(userSerializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(userSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
    """
    GET /user
    GET /user/{user_id}
    """
    def get(self, request):
        return Response("test ok", status=200)
    """
    PUT /user/{user_id}
    """
    def put(self, request):
        return Response("test ok", status=200)
    """
    DELETE /user/{user_id}
    """
    def delete(self, request):
        return Response("test ok", status=200)

# class ListPost(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
# class DetailPost(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
# class LoginPost(generics.GenericAPIView):
#     queryset = Post.objects.all()
#     serializers_class = PostSerializer