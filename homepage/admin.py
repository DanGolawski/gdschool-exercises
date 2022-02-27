from django.contrib import admin
from .models import Book, Chapter, Exercise, Topic

admin.site.register(Exercise)
admin.site.register(Book)
admin.site.register(Chapter)
admin.site.register(Topic)
