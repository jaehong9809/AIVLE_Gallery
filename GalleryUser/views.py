from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from GalleryUser.models import User
from django.views.decorators.csrf import csrf_exempt
import datetime


# Create your views here.
@csrf_exempt
def login(request):
    if request.method == 'GET':
        return render(request, "login.html")

    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        print(user)

        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            pass
        #
        # user = User.objects.filter(username=username).values()
        # if len(user) == 0:
        #     return redirect('/auth/login')
        #
        # user = User.objects.get(pk=username)
        #
        # if user.password != password:
        #     return redirect('/auth/login')
        #
        # now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # user.last_login = now
        #
        # user.is_active = 1
        # user.save()
        return redirect("/")

@csrf_exempt
def join(request):
    if request.method == 'GET':

        return render(request, "join.html")

    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']
        e_mail = request.POST['e_mail']

        user = User.objects.filter(username=username).values()

        if len(user) > 0:
            return redirect('/auth/join')

        if password != confirmPassword:
            return redirect('/auth/join')

        User(username=username,
             password=password,
             last_login="2024-02-02",
             is_superuser=0,
             e_mail=e_mail,
             is_active=0
             ).save()

        return redirect('/auth/login')
