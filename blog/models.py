from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class Blogpost(models.Model):
    post_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=50)
    desc=models.CharField(max_length=500)
    name=models.CharField(max_length=20)
    date=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to='blog/images')

    def __str__(self):
        return self.title

class NewBlog(models.Model):
    post_id1=models.AutoField(primary_key=True)
    title1=models.CharField(max_length=50)
    desc1=models.CharField(max_length=500)
    name1=models.CharField(max_length=20)
    image1=models.ImageField(upload_to='blog/images')

    def __str__(self):
        return self.title1


class BlogComment(models.Model):
    sno=models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Blogpost,on_delete=models.CASCADE)
    timestamp= models.DateTimeField(default=now)