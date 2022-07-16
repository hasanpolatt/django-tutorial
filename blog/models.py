from django.db import models
import datetime
from django.utils import timezone

class Author(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    info = models.TextField()

    def __str__(self):
        return self.name

class Category(models.Model):
    category = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.category

class Article(models.Model):
    title = models.CharField(max_length=75)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="uploads/", default='1.jpg')

    def __str__(self):
        return self.title
