from django.db import models

# Create your models here.
class Post(models.Model):
    Title = models.CharField(max_length=50)
    Description = models.TextField(max_length=500)
    Post_Time = models.DateTimeField()
    posts = models.Manager()
    