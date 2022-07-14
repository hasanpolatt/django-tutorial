from django.db import models
import datetime
from django.utils import timezone

class Author(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    info = models.TextField()

class Question(models.Model):
    questionText = models.CharField(max_length=200)
    pubDate = models.DateTimeField('date published')
    def __str__(self):
        return self.questionText
    def wasPublishedRecently(self):
        return self.pubDate >= timezone.now() - datetime.timedelta(days=1)

class Category(models.Model):
    category = models.CharField(max_length=50)
    description = models.TextField()

class Article(models.Model):
    title = models.CharField(max_length=75)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

