from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 200)
    content = models.TextField(blank = True)
    created_at= models.DateTimeField(auto_now_add= True)
    updated_at= models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    post = models.ForeignKey(Blog,on_delete=models.CASCADE) 
    content = models.TextField(blank = True)
    anonymous = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)