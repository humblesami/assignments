from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    UserSubjectPostListView
)
from . import views

urlpatterns = [
    path('', views.welcome, name='blog-home'),
    path('projects', PostListView.as_view(), name='projects-list'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('user/<str:username>/<int:subject>', UserSubjectPostListView.as_view(), name='user-posts-by-subject'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('media/Files/<int:pk>',PostDeleteView.as_view(),name='post-delete' ),
    path('search/',views.search,name='search' ),
    path('about/', views.about, name='blog-about'),
    path('contact/', views.contact, name='contact-us'),
]
