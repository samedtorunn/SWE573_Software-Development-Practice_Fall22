from django.shortcuts import  render, redirect
from django.http import HttpResponseRedirect
from django.views import View
from django.contrib import messages
from .forms import UserRegistrationForm, PostForm
from .models import Post, User


class Index(View):
    def get(self, request):
        return render(request, "application/index.html")


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')
            return redirect('home')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'application/register.html', context)


class Home(View):
    def get(self, request):
            return render(request, "application/home.html")

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect("home")
    else:
        form = PostForm()
    return render(request, 'application/create_post.html', {'form': form})

def home(request):
    posts = Post.objects.all()
    return render(request, 'application/home.html', {'posts': posts})
