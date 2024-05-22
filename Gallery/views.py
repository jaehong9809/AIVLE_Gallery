import base64
from django.utils import timezone

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from Gallery.models import Picture, Comment, Love
from GalleryUser.models import User


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
    return redirect('Gallery:detail', picture_id=picture.picture_id)


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

