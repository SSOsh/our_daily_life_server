from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *


# from .models import Post
# from .serializers import PostSerializer

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
        # 전부 갖고오기
        if kwargs.get('userId') is None:
            if (User.objects.all() is None):
                pass
            else:
                # User.objects.all()은 User의 모든 데이터를 가져옴
                userQueryset = User.objects.all()
                userQuerysetSerializer = UserSerializer(userQueryset, many=True)
                return Response(userQuerysetSerializer.data, status=status.HTTP_200_OK)
        # 기준으로 갖고오기
        else:
            # userId를 파라미터로 받겠다는 뜻인듯
            userId = kwargs.get('userId')
            userSerializer = UserSerializer(User.objects.get(id=userId))
            return Response(userSerializer.data, status=status.HTTP_200_OK)
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

class UserDetailView(APIView):
    def get(self, request, name):
        if not User.objects.filter(name=name).exists():
            return Response("USER_DOES_NOT_EXIST", status=404)

        postingList = [{
            "name": User.objects.get(name=name).name,
            "statusMessage": User.objects.get(name=name).statusMessage,
            "picture": User.objects.get(name=name).picture,
        }
        ]
        return Response({'data':postingList}, status=200)

# 댓글 등록
class CommentEnrollView(APIView):
    #파라미터 대기
    def get(self, request):
        return Response("test", status=200)

# 댓글 삭제
class CommentDeleteView(APIView):
    #파라미터 대기
    def get(self, request):
        return Response("test", status=200)

# 댓글 조회
class CommentLookupView(APIView):
    #파라미터 대기
    def get(self, request):
        return Response("test", status=200)

# 좋아요 등록
class LikeEnrollView(APIView):
    #파라미터 대기
    def get(self, request):
        return Response("test", status=200)

# 좋아요 삭제
class LikeDeleteView(APIView):
    #파라미터 대기
    def get(self, request):
        return Response("test", status=200)

# 팔로우 등록(등록성공 but 중복제거 안됨)
class FollowEnrollView(APIView):
    def get(self, request, **kwargs):
        return Response("getTest", status=200)

    # def post(self, request, follower, following):
    def post(self, request):
        followSerializer = FollowSerializer(data=request.data) # , many=True
        if followSerializer.is_valid():
            followSerializer.save()
            return Response(followSerializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(followSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # return Response("postTest", status=200)

# 팔로우 삭제
class FollowDeleteView(APIView):
    # 파라미터 대기
    def get(self, request):
        return Response("test", status=200)

# 팔로우, 팔로워 갯수 조회
class FollowLookupView(APIView):
    def get(self, request, **kwargs):
        follows = Follow.objects.filter(active=True, many=True)
        followSerializer = FollowSerializer(follows)
        return Response(followSerializer.data)

class ListPost(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class DetailPost(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class LoginPost(generics.GenericAPIView):
    queryset = Post.objects.all()
    serializers_class = PostSerializer
