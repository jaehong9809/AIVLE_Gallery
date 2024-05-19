from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from Gallery.models import Picture

def gallery_list(request):
    gallery_list = Picture.objects.all()
    context = {'gallery_li': gallery_list}

    return render(request, 'gallery/gallery.html', context)

def detail(request, id):
    if id is not None:
        picture = get_object_or_404(Picture, pk=id)
        return render(request, "detail.html",
                      {"picture": picture})
