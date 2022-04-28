# 새로 만든 urls.py
from django.urls import path

from . import views
urlpatterns = [
    # path('user/', views.UserView.as_view()),
    # 사용자관리(未完)
    path('user/', views.UserView.as_view()),
    # 프로필 조회(게시물 갖고오기 X)
    path('user/<str:userName>', views.UserDetailView.as_view()),

    # 댓글 등록(未完)
    path('comment/enroll/', views.CommentEnrollView.as_view()),
    # 댓글 삭제(未完)
    path('comment/delete/', views.CommentDeleteView.as_view()),
    # 댓글 조회(未完)
    path('comment/lookup/<str:postName>', views.CommentLookupView.as_view()),
    # 좋아요 등록(未完)
    path('like/enroll/', views.LikeEnrollView.as_view()),
    # 좋아요 삭제(未完)
    path('like/delete/<str:value>', views.LikeDeleteView.as_view()),
    # 팔로우 등록(未完)
    path('follow/enroll/', views.FollowEnrollView.as_view()),
    # 팔로우 삭제(未完)
    path('follow/delete/', views.FollowDeleteView.as_view()),
    # 팔로우, 팔로워 조회(未完)
    path('follow/lookup/<str:name>', views.FollowLookupView.as_view()),


    path('<int:pk>/', views.DetailPost.as_view()),
    path('login/', views.LoginPost.as_view()),
]