from django.conf.urls import url
from .views import PostListView, PostDetailView
from . import views

urlpatterns = [
    url('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    url('about/', views.about, name='blog-about'),
    url('', PostListView.as_view(), name='blog-home'),
]
