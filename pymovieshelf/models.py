from django.db import models


class Movie(models.Model):

    title = models.CharField(max_length=200)
    year = models.PositiveIntegerField()
    genres = models.CharField(max_length=200)
    summary = models.TextField()
    fmt = models.CharField(max_length=20)
    length = models.PositiveIntegerField()
    url = models.URLField()
    img = models.URLField()

    def __unicode__(self):
        return self.title
