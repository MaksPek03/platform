from django.shortcuts import render, redirect
from .models import Post, Uwaga
from .forms import PostForm, UwagaForm

# Create your views here.
def post_list(request):
    post_list = Post.objects.all()
    return render(request, 'post_list.html', {"post_list": post_list})

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'post_detail.html', {'post': post})


def uwagi_detail(request, pk):
    uwaga = Uwaga.objects.get(pk=pk)
    return render(request, 'uwagi_details.html', {'uwaga': uwaga})

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


def uwagi_list(request):
    uwagi_list = Uwaga.objects.all()
    return render(request, 'uwagi_list.html', {'uwagi_list': uwagi_list})

def new_uwaga(request):
    if request.method == "POST":
        form = UwagaForm(request.POST)
        if form.is_valid():
            uwaga = form.save(commit=False)
            uwaga.save()
            return redirect('uwagi_list')
    else:
        form = UwagaForm()
    return render(request, 'new_uwaga.html', {"form": form})

def edit_uwaga(request, pk):
    uwaga = Uwaga.objects.get(pk=pk)
    if request.method == "POST":
        form = UwagaForm(request.POST, instance = uwaga)
        if form.is_valid():
            form.save()
            return redirect('uwagi_detail', pk=uwaga.pk)
    else:
        form = UwagaForm(instance=uwaga)
    return render(request, 'edit_uwaga.html', {'form': form, 'uwaga': uwaga})

def delete_uwaga(request, pk):
    uwaga = Uwaga.objects.get(pk=pk)
    if request.method == "POST":
        uwaga.delete()
        return redirect('uwagi_list')
    return render(request, 'delete_uwaga.html', {'uwaga': uwaga})
def delete_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect('post_list')
    return render(request, "delete_post.html", {"post": post})

def startpage(request):
    return render(request, 'startpage.html')

def register(request):
