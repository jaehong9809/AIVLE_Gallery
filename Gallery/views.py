from django.shortcuts import render, get_object_or_404, redirect
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

def new_register(request):
    return render(request, 'gallery/new_register.html')


def create(request):
    picture = Picture(
        title = request.POST.get('title'),
        image = request.POST.get('image'),
        content = request.POST.get('content'),
        created_at = request.POST.get('created_at'),
        user_id = request.POST.get('user_id')
    )
    picture.save()

    return redirect('gallery:index')

def search(request):
    q = Picture.objects.filter(title__contains = request.GET.get('search'))
    context = {'gallery_li': q}
    print(q)
    return render(request, 'gallery/gallery.html', context)
