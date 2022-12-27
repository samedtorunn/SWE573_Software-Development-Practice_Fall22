from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect


# Create your models here.
class UserProfile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    bio = models.TextField(blank=True)
    followers = models.ManyToManyField("UserProfile", related_name='following', blank=True)

    def __str__(self):
        return f"{self.user.first_name}  {self.user.last_name}"

# User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


class Post(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="uploads/", null=True, blank=True)
    content = models.TextField()
    link = models.CharField(max_length=500, null=True)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    # user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True)
    slug = models.SlugField(default="", null=False, blank=True, db_index=True)
    likers = models.ManyToManyField("UserProfile", related_name='liked_posts', blank=True)
    bookmarkers = models.ManyToManyField("UserProfile", related_name='bookmarked_posts', blank=True)
    space = models.ForeignKey("Space", related_name='posts', blank=True, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def get_absolute_url(self):
        return reverse("postDetailUrl", args=[self.slug])

    def __str__(self):
        return f"{self.title}  {self.author}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    text = models.TextField()

class Space(models.Model):
    admin = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    members = models.ManyToManyField("UserProfile", related_name='spaces', blank=True)
    title = models.CharField(max_length=50)
    slug = models.SlugField(default="")

    def __str__(self):
        return f"{self.title} "
