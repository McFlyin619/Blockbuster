from django.db import models
from tastypie.resources import ModelResource, ALL, fields
from rental.models import Movie, Genre
from tastypie.authorization import Authorization



# Create your models here.
# resources /api/?????

class GenreResource(ModelResource):
    class Meta:
        queryset = Genre.objects.all()
        resource_name = 'genres'
        ordering = ['id','name']
        filtering = {
            'id': ALL,
            'name': ALL
        }

class MovieResource(ModelResource):
    genre = fields.ToOneField(GenreResource, 'genre', full=True)
    class Meta:
        queryset = Movie.objects.all()
        resource_name = 'movies'
        ordering = ['title', 'id', 'price', 'release_year']
        filtering = {
            'title': ALL,
            'price': ALL,
            'release_year': ALL,
        }
        allowed_methods = ['get','post','patch','put','delete','options'] #allows api to create to post
        authorization = Authorization()  # authorize all requests to have write db permissions



        
        

"""
ordering: 
/api/movies/?order_by=price  ascending
/api/movies/?order_by=-price descending


filtering:
/api/movies/?price=12 Exact price
/api/movies/?price__lt=20  lower than
/api/movies/?price__gt=5  greater than

/api/movies/?title_conatins=bad  contains

"""