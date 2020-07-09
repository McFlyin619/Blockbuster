from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello World! I'm Back!")

def about(request):
    return HttpResponse("OBrien McQuade owns Blockbuster")