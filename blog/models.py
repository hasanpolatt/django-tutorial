from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    info = models.TextField()

class Category(models.Model):
    category = models.CharField(max_length=50)
    description = models.TextField()

class Article(models.Model):
    title = models.CharField(max_length=75)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

