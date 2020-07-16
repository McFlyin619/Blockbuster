from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='root'),
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('catalog', views.catalog, name='catalog'),
    path('details/<int:id>', views.details, name='details'),
]
