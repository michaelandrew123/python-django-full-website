from django.db import models
from django.conf import settings
from blog.models import BlogPost

# Create your models here.


class Comment(models.Model):
    comment             = models.TextField(max_length=5000, null=False, blank=False)
    author              = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  
    blog_post           = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    date_published      = models.DateTimeField(auto_now_add=True, verbose_name="date published")
    date_updated        = models.DateTimeField(auto_now=True, verbose_name="date updated")


    def __str__(self):
        return self.comment


class Like(models.Model):
    like_status         = models.IntegerField(blank=True, null=True) 
    author              = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)   
    blog_post           = models.ForeignKey(BlogPost, on_delete=models.CASCADE)

    def __str__(self):
        return self.like_status

