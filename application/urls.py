from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns= [
    path("", views.Index.as_view(), name="home"),
    path("register", views.register, name="register"),
    path('login', auth_views.LoginView.as_view(template_name='application/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='application/index.html'), name='logout'),
    path('home', views.home, name='home'),
    path('create-post', views.create_post, name='create_post')
]