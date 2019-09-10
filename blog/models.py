from django.db import models
from django.contrib.auth.models import User



class Post(models.Model):

    title = models.CharField(max_length=50)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):

        return self.title

class Blog(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    post =  models.
