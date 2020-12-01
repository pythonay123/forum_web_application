from django.urls import path
from . import views


app_name = 'posts'
urlpatterns = [
    # path('', views.PostListView.as_view(), name='blog_home'),
    path('<int:pk>/', views.ThreadDetailView.as_view(), name='thread-detail'),
    path('<int:pk>/post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    # path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    # path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    # path('user/<str:username>/', views.UserListView.as_view(), name='user-posts'),
    # path('about/', views.about, name='blog_about'),
]
