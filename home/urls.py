from django.urls import path
from .views import ForumListView


app_name = 'home'

urlpatterns = [
    path('', ForumListView.as_view(), name='home'),
]
