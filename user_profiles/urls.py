from django.urls import path
from .views import LoginView, UserProfileView, LogoutView, UpdateProfileView, set_timezone, UserDeleteAccountView
from django.contrib.auth import views as auth_views


app_name = 'user_profiles'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('timezone/', set_timezone, name='set_timezone'),
    path('update/<int:pk>/', UpdateProfileView.as_view(), name='update-profile'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='user_profiles/edit-password.html'),
         name='password_reset'),
    path('close-account/', UserDeleteAccountView.as_view(), name='close_account'),
]
