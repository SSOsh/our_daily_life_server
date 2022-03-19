# 새로 만든 urls.py
from django.urls import path

from . import views
urlpatterns = [
    path('', views.ListPost.as_view()),
    path('<int:pk>/', views.DetailPost.as_view()),
    path(r'viewuser/', views.LookupUser.getUser()),
]