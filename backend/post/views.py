from django.shortcuts import render
from rest_framework import status, generics
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
            # DB에 저장
            userSerializer.save()
            # 클라에 JSON으로 보내줌
            return Response(userSerializer.data, status=status.HTTP_201_CREATED)
        else:
            # 클라에 실패했다고 알림
            return Response(userSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
    """
    GET /user
    GET /user/{user_id}
    """
    # **kwargs가 뭔지 확인필요
    def get(self, request, **kwargs):
        # 전부 갖고옹기
        if kwargs.get('userId') is None:
            if(User.objects.all() is None):
                pass
            else:
                userQueryset = User.objects.all()
                userQuerysetSerializer = UserSerializer(userQueryset, many=True)
                return Response(userQuerysetSerializer.data, status=status.HTTP_200_OK)
        # 기준으로 갖고오기
        else:
            #userId를 파라미터로 받겠다는 뜻인듯
            userId = kwargs.get('userId')
            userSerializer = UserSerializer(User.objects.get(id=userId))
            return Response(userSerializer.data, status=status.HTTP_200_OK)
        #return Response("test ok", status=200)
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

class ListPost(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class DetailPost(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class LoginPost(generics.GenericAPIView):
    queryset = Post.objects.all()
    serializers_class = PostSerializer