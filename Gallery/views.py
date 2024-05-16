from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from Gallery.models import Picture


def detail(request, id):
    if id is not None:
        picture = get_object_or_404(Picture, pk=id)
        return render(request, "detail.html",
                      {"picture": picture})
