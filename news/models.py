from django.db import models


class Feed(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=200)
    is_active = models.BooleanField(default=False)


class Article(models.Model):
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    url = models.URLField()
    description = models.TextField()
    publication_date = models.DateTimeField()
