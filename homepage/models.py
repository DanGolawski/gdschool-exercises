from django.db import models

class Book(models.Model):
    book_id = models.CharField(max_length=15)
    displayed_value = models.CharField(max_length=50)

class Chapter(models.Model):
    index = models.IntegerField()
    book = models.CharField(max_length=15)
    displayed_value = models.CharField(max_length=50)

class Topic(models.Model):
    index = models.IntegerField()
    book = models.CharField(max_length=15)
    chapter = models.IntegerField()
    displayed_value = models.CharField(max_length=50)

class Exercise(models.Model):
    exercise_nr = models.IntegerField()
    book = models.CharField(max_length=15)
    chapter = models.IntegerField()
    topic = models.IntegerField()
    image = models.CharField(max_length=100)
