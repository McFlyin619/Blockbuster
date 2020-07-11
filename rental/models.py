from django.db import models
from django.utils import timezone

# Create your models here.
"""
    if you modify the models:
        python manage.py makemigrations
        python manage.py migrate
"""

class Genre(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name 



class Movie(models.Model):
    title = models.CharField(max_length=250)
    release_year = models.IntegerField()
    in_stock = models.IntegerField()
    price = models.FloatField()
    image_url = models.CharField(max_length=999)
    length_min = models.IntegerField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        
        return str(self.release_year) + ' | ' + self.title + ' | ' + '$' + str(self.price)