from django.db import models


# Create your models here.
# 이용자
class User(models.Model):
    """
        userName: 이용자 ID
        statusMessage: 이용자 상태메시지
        picture: 이용자 프로필사진
    """
    userName = models.CharField(primary_key=True, max_length=100, null=False)
    statusMessage = models.CharField(max_length=200)
    picture = models.BinaryField()

    def __str__(self):
        """A string representation of the model."""
        return self.userName


# 게시물
class Post(models.Model):
    """
        postId: 기본ID
        userId: User의 ID
        content: 게시물내용
        picture: 게시물사진
    """
    postId = models.AutoField(primary_key=True, null=False)
    userName = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    content = models.CharField(max_length=200, null=False)
    picture = models.BinaryField(null=False)

    def __str__(self):
        """A string representation of the model."""
        return self.content


# 댓글
class Comment(models.Model):
    """
        commentId: 댓글ID
        postTitle: 게시물이름
        comment: 댓글내용
        sequence: 대댓글여부
    """
    commentId = models.AutoField(primary_key=True, null=False)
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
        return self.postId


# 팔로잉
class Follow(models.Model):
    followId = models.AutoField(primary_key=True, null=False)
    follower = models.CharField(max_length=100, null=False)
    following = models.CharField(max_length=100, null=False)

    def __str__(self):
        """A string representation of the model."""
        return self.follower
