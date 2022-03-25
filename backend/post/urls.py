# 새로 만든 urls.py
from django.urls import path

from . import views
urlpatterns = [
    # path('user/', views.UserView.as_view()),
    path('user/', views.UserView.as_view()),

    # path('<string:userId>', views.UserView.as_view()),
    path('<int:pk>/', views.DetailPost.as_view()),
    path('login/', views.LoginPost.as_view()),
]