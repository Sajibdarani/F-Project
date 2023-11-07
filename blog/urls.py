from django.urls import path
from . import views
from .views import PostListView, PostDetailsView, PostCreateView,PostUpdateView

urlpatterns = [
    path('', PostListView.as_view(), name="blog-home"),
    path('post/<int:pk>', PostDetailsView.as_view(), name="post-detail"),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name="post-Update"),
    path('post/new/', PostCreateView.as_view(), name="post-create"),
    path('about/', views.about, name="blog-about"),

]
