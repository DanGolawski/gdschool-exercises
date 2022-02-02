from django.db import models

class Exercise(models.Model):
    book = models.CharField(max_length=15)
    chapter = models.IntegerField()
    exercise = models.IntegerField()
    image = models.CharField(max_length=100)
