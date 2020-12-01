from django.urls import path
from .views import HomeView, UserRegisterView


app_name = 'registration'

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('register/', UserRegisterView.as_view(), name='register'),
    # path('success/', success, name='success'),
]
