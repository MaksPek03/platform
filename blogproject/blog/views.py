from django.shortcuts import render, redirect
from .models import Post, Uwaga
from .forms import PostForm, UwagaForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login

# Create your views here.
def post_list(request):
    post_list = Post.objects.all()
    return render(request, 'post_list.html', {"post_list": post_list})

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'post_detail.html', {'post': post})


def uwagi_list(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    uwagi = post.uwaga_set.all()
    return render(request, 'uwagi_list.html', {'post': post, 'uwagi': uwagi})

def newPost(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'newPost.html', {'form': form})

def edit_post(request,pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'edit_post.html', {"form": form, "post": post})


def uwagi_detail(request, post_pk, uwaga_pk):
    post = Post.objects.get(pk=post_pk)
    uwagi = post.uwaga_set.all()
    uwaga = uwagi.get(pk=uwaga_pk)
    return render(request, 'uwagi_details.html', {'post':post, 'uwaga': uwaga})

def new_uwaga(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.method == "POST":
        form = UwagaForm(request.POST)
        if form.is_valid():
            uwaga = form.save(commit=False)
            uwaga.post = post
            uwaga.save()
            return redirect('uwagi_list', post_pk=post_pk)
    else:
        form = UwagaForm()
    return render(request, 'new_uwaga.html', {"form": form})

def edit_uwaga(request, post_pk, uwaga_pk):
    post = Post.objects.get(pk=post_pk)
    uwagi = post.uwaga_set.all()
    uwaga = uwagi.get(pk=uwaga_pk)
    if request.method == "POST":
        form = UwagaForm(request.POST, instance = uwaga)
        if form.is_valid():
            form.save()
            return redirect('uwagi_detail', post_pk = post_pk, uwaga_pk=uwaga_pk)
    else:
        form = UwagaForm(instance=uwaga)
    return render(request, 'edit_uwaga.html', {'form': form, 'post': post, 'uwaga': uwaga})

def delete_uwaga(request, post_pk, uwaga_pk):
    post = Post.objects.get(pk=post_pk)
    uwaga = Uwaga.objects.get(pk=uwaga_pk)
    if request.method == "POST":
        uwaga.delete()
        return redirect('uwagi_list', post_pk = post_pk)
    return render(request, 'delete_uwaga.html', {'post': post, 'uwaga': uwaga})


def delete_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect('post_list')
    return render(request, "delete_post.html", {"post": post})

def startpage(request):
    return render(request, 'startpage.html')

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('startpage')
    else:
        form = UserCreationForm()
    return render(request, 'sign_up.html', {"form": form})

def login_views(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('startpage')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {"form": form})