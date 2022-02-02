from django.shortcuts import render, redirect
from .models import Exercise
from django.contrib import messages

book_titles = {
    'pazdro_1_1': 'Pazdro 1 p.rozsz.',
    'pazdro_2_1': 'Pazdro 2 p.rozsz.',
    'pazdro_3_1': 'Pazdro 3 p.rozsz.',
    'pazdro_4_1': 'Pazdro 4 p.rozsz.',
    'pazdro_1_0': 'Pazdro 1 p.podst.',
    'pazdro_2_0': 'Pazdro 2 p.podst.',
    'pazdro_3_0': 'Pazdro 3 p.podst.',
    'pazdro_4_0': 'Pazdro 4 p.podst.',
    'nowaera_1_1': 'Nowa Era 1 p.rozsz.',
    'nowaera_2_1': 'Nowa Era 2 p.rozsz.',
    'nowaera_3_1': 'Nowa Era 3 p.rozsz.',
    'nowaera_4_1': 'Nowa Era 4 p.rozsz.',
    'nowaera_1_0': 'Nowa Era 1 p.podst.',
    'nowaera_2_0': 'Nowa Era 2 p.podst.',
    'nowaera_3_0': 'Nowa Era 3 p.podst.',
    'nowaera_4_0': 'Nowa Era 4 p.podst.',
}

def get_dropdown_values():
    books = list(Exercise.objects.values_list('book', flat=True))
    books = list(set(books))
    return list(map(lambda b: {'id': b, 'displayedValue': book_titles[b]}, books))

def display(request):
    books = get_dropdown_values()
    return render(request, 'home.html', {'books': books})


def getexercise(request):
    book = request.GET.get('book')
    chapter = request.GET.get('chapter')
    exercise = request.GET.get('exercise')
    selected_exercises = Exercise.objects.raw(f'SELECT id, image FROM homepage_exercise WHERE book="{book}" AND chapter={chapter} AND exercise={exercise}')
    selected_exercises = [ex for ex in selected_exercises]
    if not len(selected_exercises):
        return render(request, 'imageview.html')
    selected_exercise = selected_exercises[0]
    # return render(request, 'imageview.html', {'image': selected_exercise.image})
    return redirect(selected_exercise.image)