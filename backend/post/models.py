from django.db import models

# Create your models here.
# 게시물
class Post(models.Model):
    title = models.CharField(max_length=200)
    picture = models.CharField(max_length=1000)
    content = models.TextField()

    def __str__(self):
        """A string representation of the model."""
        return self.title

# 이용자
class User(models.Model):
    name = models.CharField(max_length=100)
    statusMessage = models.CharField(max_length=200)
    picture = models.CharField(max_length=1000)

# 댓글
class comment(models.Model):
    postTitle = models.CharField(max_length=200)
    comment = models.TextField()

# 팔로잉
class Follow(models.Model):
    follower = models.CharField(max_length=100)
    following = models.CharField(max_length=100)
