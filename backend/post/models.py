from django.db import models

# Create your models here.
# 게시물
class Post(models.Model):
    title = models.CharField(max_length=200, null=False)
    picture = models.CharField(max_length=1000, null=False)
    content = models.TextField(null=False)
    def __str__(self):
        """A string representation of the model."""
        return self.title

# 이용자
class User(models.Model):
    name = models.CharField(max_length=100, null=False)
    statusMessage = models.CharField(max_length=200)
    picture = models.CharField(max_length=1000)
    def __str__(self):
        """A string representation of the model."""
        return self.name

# 좋아요
class Like(models.Model):
    postTitle = models.ForeignKey(Post, on_delete=models.CASCADE)
    like = models.BooleanField(null=False)
    def __str__(self):
        """A string representation of the model."""
        return self.postTitle

# 댓글
class Comment(models.Model):
    postTitle = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField(null=False)
    def __str__(self):
        """A string representation of the model."""
        return self.postTitle

# 팔로잉
class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE)
    following = models.CharField(max_length=100, null=False)
    def __str__(self):
        """A string representation of the model."""
        return self.follower