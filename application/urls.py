from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns= [
    path("", views.Index.as_view(), name="home"),
    path("register", views.register, name="register"),
    path('login', auth_views.LoginView.as_view(template_name='application/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='application/index.html'), name='logout'),
    path('home', views.home, name='home'),
    path('create-post', views.create_post, name='create_post'),
    path('user/<int:id>/', views.user_profile, name='user_profile'),
    path('follow/<int:pk>/', views.follow_user, name='follow_user'),
    path('like/<int:pk>/', views.like_post, name='like_post'),
    path('space/<str:slug>/', views.space_posts, name='space_posts'),
    path('submit_comment/<int:post_pk>/', views.submit_comment, name='submit_comment'),
    path('search/', views.search_keywords, name='search_keywords'),
    path('spaces/', views.list_spaces, name='list_spaces'),
    path('create-space/', views.create_space, name='create_space'),
    path('join-space/<slug:slug>/', views.join_space, name='join_space'),
    path('leave-space/<slug:slug>/', views.leave_space, name='leave_space'),
    path('people/', views.people_list, name='people_list'),
    path('search_people/', views.search_people, name='search_people'),
    path('post/<int:post_pk>/edit/', views.edit_post, name='edit_post'),
    path('post/<int:post_pk>/save/', views.save_changes, name='save_changes'),

]