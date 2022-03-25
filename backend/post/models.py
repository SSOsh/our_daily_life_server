from django.db import models

# Create your models here.
# 게시물
class Post(models.Model):
    """
        postId: 기본ID
        userId: User의 ID
        content: 게시물내용
        picture: 게시물사진
    """
    postId = models.AutoField(primary_key=True, null=False)
    userId = models.IntegerField(null=False)
    content = models.CharField(max_length=200, null=False)
    picture = models.BinaryField(null=False)
    def __str__(self):
        """A string representation of the model."""
        return self.title

# 이용자
class User(models.Model):
    userId = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=100, null=False)
    statusMessage = models.CharField(max_length=200)
    picture = models.BinaryField()
    def __str__(self):
        """A string representation of the model."""
        return self.name

# 댓글
class Comment(models.Model):
    comemntId = models.AutoField(primary_key=True, null=False)
    postTitle = models.ForeignKey(Post, on_delete=models.CASCADE, null=False)
    comment = models.TextField(null=False)
    sequence = models.SmallIntegerField(null=False)
    def __str__(self):
        """A string representation of the model."""
        return self.postTitle

# 좋아요
class Like(models.Model):
    likeId = models.AutoField(primary_key=True, null=False)
    postId = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentId = models.ForeignKey(Comment, on_delete=models.CASCADE)
    like = models.SmallIntegerField(null=False)
    def __str__(self):
        """A string representation of the model."""
        return self.postTitle

# 팔로잉
class Follow(models.Model):
    followId = models.AutoField(primary_key=True, null=False)
    follower = models.CharField(max_length=100, null=False)
    following = models.CharField(max_length=100, null=False)
    def __str__(self):
        """A string representation of the model."""
        return self.follower