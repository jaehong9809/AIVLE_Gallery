from django.db import models


class Picture(models.Model):
    pid = models.IntegerField(primary_key=True,db_column='picture_id')
    title = models.CharField(max_length=200)
    image = models.ImageField()
    content = models.TextField()
    created_at = models.DateTimeField()
    user_id = models.CharField(max_length=200)

    class Meta:
        db_table = 'picture'


# class Love(models.Model):
#     love_id = models.IntegerField(blank=False, null=False)
#     user_id = models.IntegerField(blank=False, null=False)
#     picture_id = models.IntegerField(blank=False, null=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#
# class Comment(models.Model):
#     comment_id = models.IntegerField(blank=False, null=False)
#     user_id = models.IntegerField(blank=False, null=False)
#     picture_id = models.IntegerField(blank=False, null=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     content = models.TextField()
