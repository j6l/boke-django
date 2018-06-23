from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    create_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    abstract = models.CharField(max_length=100,blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    auther = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.title
