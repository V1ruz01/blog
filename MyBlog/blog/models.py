from django.db import models
from datetime import timedelta
from django.utils import timezone


class Author(models.Model):
    name = models.CharField(max_length=20)
    bio = models.TextField(max_length=5000)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=5000)
    published_date = models.DateTimeField()
    author = models.ForeignKey(Author,
                                on_delete=models.CASCADE,
                                related_name='posts')

    def __str__(self):
        return self.title

    def published_recently(self) -> bool:
        now = timezone.now() # <- broken
        return now - timedelta(days=7) <= self.published_date <= now

    
