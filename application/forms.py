# Create your forms here.
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Post, UserProfile, Comment, Space
from django.db import models



class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'link', "image", 'content', 'space']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
          'text': forms.Textarea(attrs={'rows':2}),
        }


class UserRegistrationForm(UserCreationForm):
    id = models.AutoField(primary_key=True)
    first_name = forms.CharField(max_length=101)
    last_name = forms.CharField(max_length=101)
    email = forms.EmailField()
    profile_picture = forms.ImageField(required=False)


    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', "profile_picture", 'email', 'password1', 'password2']


class SpaceForm(forms.ModelForm):
    class Meta:
        model = Space
        fields = ['title', 'slug']

