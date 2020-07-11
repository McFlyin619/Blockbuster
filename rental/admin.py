# django-admin startproject
# cd blockbuster
# python manage.py

from django.contrib import admin
from.models import Movie, Genre

# Create Template Classes for admin module
class MovieTemplate(admin.ModelAdmin):
    list_display = ("id" ,  "title", "genre", "release_year", "price", "in_stock")
    list_display_links = ("id", "title")

    #fields = ("title", "release_year", "genre", "in_stock", "image_url", "length_min", "date_created")
    #exclude = ("price",)

class GenreTemplate(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")


# Register your models here.
admin.site.register(Movie, MovieTemplate)
admin.site.register(Genre, GenreTemplate)
