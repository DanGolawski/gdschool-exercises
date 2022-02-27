from django.forms import model_to_dict
from django.shortcuts import render, redirect
from .models import Book, Chapter, Exercise, Topic
from django.contrib import messages
from django.http import JsonResponse

def display(request):
    books = Book.objects.all()
    return render(request, 'home.html', {'books': books})

def get_chapters(request, book_index):
    chapters = list(Chapter.objects.raw(f'SELECT * FROM homepage_chapter WHERE book="{book_index}"'))
    chapters = list(map(lambda chapter: model_to_dict(chapter), chapters))
    return JsonResponse(chapters, safe=False)

def get_topics(request, book_index, chapter_nr):
    topics = list(Topic.objects.raw(f'SELECT * FROM homepage_topic WHERE book="{book_index}" AND chapter="{chapter_nr}"'))
    topics = list(map(lambda topic: model_to_dict(topic), topics))
    return JsonResponse(topics, safe=False)

def get_exercises(request, book_index, chapter_nr, topic_nr):
    exercises = list(Exercise.objects.raw(f'SELECT * FROM homepage_exercise WHERE book="{book_index}" AND chapter="{chapter_nr}" AND topic="{topic_nr}"'))
    exercises = list(map(lambda exercise: model_to_dict(exercise), exercises))
    return JsonResponse(exercises, safe=False)

def show_exercise(request):
    return redirect(request.GET.get('exercise'))