from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie, Genre
# Create your views here.
def home(request):
    all_movies = Movie.objects.all() # read the movie table into a list
    return render(request, 'index.html', {'title': 'Blockbuster 20/20', 'movies' : all_movies})

def catalog(request):
    return render(request, 'catalog.html')

def details(request, id):
    return render(request, 'details.html')

def about(request):
    return render(request, 'about.html')