import base64

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone

from Gallery.models import Picture, Comment, Love
from GalleryUser.models import User


def gallery_list(request):
    gallery_list = Picture.objects.all()
    context = {'gallery_li': gallery_list}
    return render(request, 'gallery/gallery.html', context)


def detail(requests, picture_id):
    if picture_id is not None:
        picture = get_object_or_404(Picture, picture_id=picture_id)
        image_data = base64.b64encode(picture.image).decode()  # <-- 이 부분 해결하면 될 것 같음
        image_data = 'iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w38GIAXDIBKE0DHxgljNBAAO9TXL0Y4OHwAAAABJRU5ErkJggg=='
        return render(requests, "detail.html",
                      {"picture": picture, 'img': image_data})


def create_comment(requests, picture_id):
    picture = get_object_or_404(Picture, pk=picture_id)
    user = get_object_or_404(User, pk=requests.user)
    comment = Comment(user_id=user, picture_id=picture, content=requests.POST.get('content'),
                      created_at=timezone.now())
    comment.save()
    return redirect('gallery:detail', picture_id=picture.picture_id)


def create_love(requests, picture_id):
    picture = get_object_or_404(Picture, pk=picture_id)
    user = get_object_or_404(User, pk=requests.user)
    love = Love(user_id=user, picture_id=picture, created_at=timezone.now())
    love.save()
    return redirect('Gallery:detail', picture_id=picture.picture_id)


def update_post(requests, picture_id):
    picture = get_object_or_404(Picture, pk=picture_id)
    if requests.method == 'POST':
        picture.title = requests.POST['title']
        picture.content = requests.POST['content']
        picture.image = requests.POST['image']
        picture.save()
        return redirect('Gallery:detail', picture_id=picture_id)
    else:
        return render('Gallery:update', {'picture_id':picture_id})


def new_register(request):
    return render(request, 'gallery/new_register.html')


def create(request):
    picture = Picture(
        title=request.POST.get('title'),
        image=request.POST.get('image'),
        content=request.POST.get('content'),
        created_at=request.POST.get('created_at'),
        user_id=request.POST.get('user_id')
    )
    picture.save()

    return redirect('gallery:index')


def search(request):
    q = Picture.objects.filter(title__contains=request.GET.get('search'))
    context = {'gallery_li': q}
    print(q)
    return render(request, 'gallery/gallery.html', context)
