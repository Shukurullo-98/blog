from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from accounts.models import CustomUser
from django.http import HttpResponse
from mainapp.models import Posts
from mainapp.forms import PostForm

# Create your views here.

from .forma import Custom_UserForm, EditUserForm


def user_register(request):
    form = Custom_UserForm(request.POST)
    if request.method == "POST":
        form = Custom_UserForm(request.POST)
        if form.is_valid():
            user =form.changed_data.get('username')
            form.save()

            return redirect('user_login')
        else:
            form = Custom_UserForm()

    context = {
        'form': form
    }
    return render(request, 'profil/register.html', context)


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')

        else:
            messages.error(request, 'Not found')
            return redirect('user_login')

    return render(request, 'profil/login.html')


def user_logout(request):
    logout(request)
    return redirect('index')


def user_Profile(request, username):
    try:
        user_Profile = CustomUser.objects.all().get(username=username)
    except CustomUser.DoesNotExist:
        return HttpResponse('Page Not Found')
    posts = Posts.objects.filter(author=user_Profile).order_by('-date')
    form = PostForm(request.POST, request.FILES)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            print('1')
            obj = form.save(commit=False)
            author = CustomUser.objects.filter(username=username).first()
            obj.author = author
            obj.save()
            form.save()
            return redirect('user_Profile', request.user.username)
    context = {
        'user_Profile': user_Profile,
        'posts': posts,
    }
    return render(request, 'profil/profile.html', context)


def edit_user(request, username):
    user = CustomUser.objects.get(username=username)
    form = EditUserForm(request.POST or None, request.FILES or None, instance=user)
    if request.method == "POST":
        form = EditUserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_Profile', request.user.username)
    context = {
        'form': form,
        'user': user,
    }
    return render(request, 'profil/edit_user.html', context)


def post_delete(request, pk):
    post = Posts.objects.get(id=pk)
    post.delete()
    return redirect('user_Profile', request.user.username)
