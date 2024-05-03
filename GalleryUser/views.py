from django.shortcuts import render, HttpResponse, get_object_or_404
from GalleryUser.models import User

# Create your views here.

def login(request):
    User(user_id ="iddsdsadsa", pw = "pw").save()
    return HttpResponse("hi")
