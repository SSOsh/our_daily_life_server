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
    GET 사용자 정보 가져오기
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
    POST 회원가입
    """
    def post(self, request):
        userSerializer = UserSerializer(data=request.data) # , many=True
        if userSerializer.is_valid():
            userSerializer.save()
            return Response(userSerializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(userSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
    """
    PUT 사용자 정보 수정
    """
    def put(self, request):
        return Response("test ok", status=200)
    """
    DELETE 회원탈퇴
    """
    def delete(self, request):
        try:
            postObject = Post.objects.get(content=request.data)
            likeObject = Like.objects.get(postId=postObject.postId)
            likeObject.delete()
            return Response("Post OK", status=status.HTTP_202_ACCEPTED)
        except Post.DoesNotExist:
            try:
                commentObject = Comment.objects.get(comment=request.data)
                likeObject = Like.objects.get(commentId=commentObject.commentId)
                likeObject.delete()
                return Response("Comment OK", status=status.HTTP_202_ACCEPTED)
            except Comment.DoesNotExist:
                return Response("not exist", status=status.HTTP_400_BAD_REQUEST)

class UserDetailView(APIView):
    def get(self, request, userName):
        if not User.objects.filter(userName=userName).exists():
            return Response("USER_DOES_NOT_EXIST", status=404)

        postingList = [{
            "userName": User.objects.get(userName=userName).userName,
            "statusMessage": User.objects.get(userName=userName).statusMessage,
            "picture": User.objects.get(userName=userName).picture,
        }
        ]
        return Response({'data':postingList}, status=200)

# 댓글 등록(기본틀ㅇ, 예외상황 생각안함)
class CommentEnrollView(APIView):
    #파라미터 대기
    def post(self, request):
        commentSerializer = CommentSerializer(data=request.data)
        if commentSerializer.is_valid():
            commentSerializer.save()
            return Response(commentSerializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(commentSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 댓글 삭제
class CommentDeleteView(APIView):
    #파라미터 대기
    def get(self, request):
        return Response("test", status=200)
#
#     def delete(self, request):
#         return Response("deleteTest", status=200)
#
# # 댓글 조회(postid로 postName들고와서 그걸 comment에, 미완)
class CommentLookupView(APIView):
    #파라미터 대기
    def get(self, request, postName):
        post = Post.objects.get(postName=postName)
        comments = Comment.objects.filter(postId=post.postId)
        commentSerializer = CommentSerializer(comments, many=True)
        return Response(commentSerializer.data)

# 좋아요 등록(기본틀ㅇ, 예외상황 생각안함)
class LikeEnrollView(APIView):
    #파라미터 대기
    # def get(self, request):
    #     likeSerializer = LikeSerializer(data=request.data) # , many=True
    #     if likeSerializer.is_valid():
    #         likeSerializer.save()
    #         return Response(likeSerializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(likeSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def post(self, request):
        likeSerializer = LikeSerializer(data=request.data) # , many=True
        if likeSerializer.is_valid():
            likeSerializer.save()
            return Response(likeSerializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(likeSerializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 좋아요 삭제(확인필요)
class LikeDeleteView(APIView):
    def delete(self, request, value):
        # if not User.objects.filter(name=name).exists():
        #     return Response("USER_DOES_NOT_EXIST", status=404)
        #request.data에는 값이 content(Post)나 comment(Comment)가 들어감
        try:
            postObject = Post.objects.get(content=request.data)
            likeObject = Like.objects.get(postId=postObject.postId)
            likeObject.delete()
            return Response("Post OK", status=status.HTTP_202_ACCEPTED)
        except Post.DoesNotExist:
            try:
                commentObject = Comment.objects.get(comment=request.data)
                likeObject = Like.objects.get(commentId=commentObject.commentId)
                likeObject.delete()
                return Response("Comment OK", status=status.HTTP_202_ACCEPTED)
            except Comment.DoesNotExist:
                return Response("not exist", status=status.HTTP_400_BAD_REQUEST)


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

# 팔로우 삭제
class FollowDeleteView(APIView):
    # 파라미터 대기
    def get(self, request):
        return Response("test", status=200)
    def delete(self, request):
        return Response("OK", status=status.HTTP_202_ACCEPTED)

# 팔로우, 팔로워 갯수 조회
class FollowLookupView(APIView):
    def get(self, request, name):
        follows = Follow.objects.filter(follower=name)
        followSerializer = FollowSerializer(follows, many=True)
        return Response(followSerializer.data)

class ListPost(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class DetailPost(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class LoginPost(APIView):
    def get(self, request):
        try:
            userSerializer = UserSerializer(data=request.data)
            if userSerializer.is_valid():
                return Response("{\"status\":\"ok\"}", status=status.HTTP_200_OK)
        #아이디존재X
        except User.DoesNotExist:
            return None
