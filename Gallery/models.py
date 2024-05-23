from django.db import models
from GalleryUser.models import User


class Picture(models.Model):
    picture_id = models.IntegerField(primary_key=True, db_column='picture_id')
    title = models.CharField(max_length=200, db_column='title')
    image = models.BinaryField(null=True, db_column='image')
    content = models.TextField(db_column='content')
    created_at = models.DateTimeField(auto_now=True, db_column='created_at')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    # user_id = models.CharField(max_length=200, db_column='user_id')

    def __str__(self):
        return self.title

    class Meta:
        managed = False
        db_table = 'picture'


class Comment(models.Model):
    comment_id = models.IntegerField(primary_key=True, blank=False, null=False, auto_created=True, db_column='comment_id')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    # user_id = models.CharField(max_length=200, db_column='user_id')
    picture_id = models.ForeignKey(Picture, on_delete=models.CASCADE, db_column='picture_id')
    created_at = models.DateTimeField(auto_now_add=True, db_column='created_at')
    content = models.TextField(db_column='content')

    class Meta:
        managed = False
        db_table = 'comment'


class Love(models.Model):
    love_id = models.IntegerField(primary_key=True, db_column='love_id')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    picture_id = models.ForeignKey(Picture, on_delete=models.CASCADE, db_column='picture_id')
    created_at = models.DateTimeField(auto_now_add=True, db_column='created_at')

    class Meta:
        managed = False
        db_table = 'love'