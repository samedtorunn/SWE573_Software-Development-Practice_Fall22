from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import View
from django.contrib import messages
from .forms import UserRegistrationForm, PostForm, CommentForm, SpaceForm
from .models import Post, User, UserProfile, Comment, Space
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import Http404




# Landing Page View Function
class Index(View):
    def get(self, request):
        return render(request, "application/index.html")


# Register Page Register Function
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Create a user profile for the newly created user
            user_profile = UserProfile(user=user, id=user.id, profile_picture=form.cleaned_data['profile_picture'])
            user_profile.save()


            messages.success(request, f'Your account has been created. You can log in now!')
            if user is not None:
                login(request, user)
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
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user.profile
            post.save()
            return HttpResponseRedirect("home")
    else:
        form = PostForm()
    return render(request, 'application/create_post.html', {'form': form})


def home(request):
    posts = Post.objects.all().order_by('-created_at')
    comment_form = CommentForm()

    return render(request, 'application/home.html', {'posts': posts, 'comment_form': comment_form, "title": "Home Feed"})

@login_required
def space_posts(request, slug):
    space = get_object_or_404(Space, slug=slug)
    posts = space.posts.all()
    comment_form = CommentForm()

    return render(request, 'application/space_page.html', {'posts': posts, 'comment_form': comment_form, "title": f"Space: {space.title}"})


def user_profile(request, id):
    profile = get_object_or_404(UserProfile, id=id)

    return render(request, 'application/user_profile.html', {
        'profile': profile,
        'is_following': profile.followers.contains(request.user.profile),
        "posts": Post.objects.filter(Q(author=profile) | Q(likers=profile)),
        "comment_form": CommentForm(),
        "follower_count": profile.followers.count()
    })


@login_required
def follow_user(request, pk):
    # Get the user that the logged-in user wants to follow
    user_to_follow = get_object_or_404(User, pk=pk)
    target_profile = user_to_follow.profile
    user = request.user


    user_profile = request.user.profile
    print(user_profile)
    if target_profile.followers.contains(user_profile):
        target_profile.followers.remove(user_profile)
    else:
        target_profile.followers.add(user_profile)
    target_profile.save()
    print("Successfully added to followers")


    return HttpResponseRedirect('/user/' + str(user_to_follow.pk))


@login_required
def like_post(request, pk):
    # Get the user that the logged-in user wants to follow
    post_to_like = get_object_or_404(Post, pk=pk)
    user = request.user

    # Get the logged-in user's profile
    user_profile = request.user.profile
    # print(user_profile)
    if post_to_like.likers.contains(user_profile):
        post_to_like.likers.remove(user_profile)
        is_liked = False

    else:
        post_to_like.likers.add(user_profile)
        liked = True

    # Redirect back to the profile page
    return redirect(request.META.get('HTTP_REFERER'))

@login_required
def submit_comment(request, post_pk):
    # Get the user that the logged-in user wants to follow
    post = get_object_or_404(Post, pk=post_pk)
    # Get the logged-in user's profile
    user_profile = request.user.profile

    form = CommentForm(request.POST, request.FILES)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user.profile
        comment.post = post
        comment.save()

    return redirect(request.META.get('HTTP_REFERER'))



@login_required
def search_keywords(request):
  query = request.GET.get('q')
  if query:
    posts = Post.objects.filter(Q(title__contains=query) | Q(content__contains=query))
  else:
    posts = Post.objects.all()
  return render(request, 'application/home.html', {'posts': posts})


@login_required
def list_spaces(request):
    spaces = Space.objects.all()
    return render(request, 'application/list_spaces.html', {'spaces': spaces})

@login_required
def create_space(request):
    if request.method == 'POST':
        form = SpaceForm(request.POST)
        if form.is_valid():
            space = form.save()
            space.save()
            return redirect('home')
            print("space saved.")
    else:
        form = SpaceForm()
    return render(request, 'application/create_space.html', {'form': form})

@login_required
def join_space(request, slug):
    space = Space.objects.get(slug=slug)
    space.members.add(request.user.profile)
    space.save()
    print(request.user.profile, "has joined")
    return redirect('home')

@login_required
def leave_space(request, slug):
    space = Space.objects.get(slug=slug)
    space.members.remove(request.user.profile)
    space.save()
    return redirect('home')

@login_required
def people_list(request):
    profiles = UserProfile.objects.all()
    return render(request, 'application/people.html', {'profiles': profiles})

@login_required
def search_people(request):
  query = request.GET.get('q')
  if query:
    profiles = UserProfile.objects.filter(Q(user__first_name__contains=query) | Q(user__last_name__contains=query) | Q(user__username__contains=query))
  else:
    profiles = UserProfile.objects.all()
  return render(request, 'application/people.html', {'profiles': profiles})


@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post_id=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'application/edit_post.html', {'form': form})

