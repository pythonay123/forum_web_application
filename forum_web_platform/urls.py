"""forum_web_platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.auth import views as auth_views
from home.views import ForumListView
from products import views as product_views
from carts import views as cart_views
from orders import views as order_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('index/', include('registration.urls')),
    path('user/', include('user_profiles.urls')),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='user_profiles/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='user_profiles/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='user_profiles/password_reset_complete.html'), name='password_reset_complete'),
    path('accounts/', include('allauth.urls')),
    path('forums/', include('forums.urls')),
    path('thread/', include('posts.urls')),
    path('support/', include('support.urls')),
    path('', ForumListView.as_view(), name='home'),
    path('marketplace/', product_views.home, name='marketplace'),
    path('products/', product_views.all, name='all_products'),
    path('product/<slug:slug>/', product_views.single, name='single_product'),
    path('s/', product_views.search, name='search'),
    path('cart/', cart_views.view, name='cart_view'),
    path('remove-from-cart/<int:id>/', cart_views.remove_from_cart, name='remove_from_cart'),
    path('add-to-cart/<slug:product_slug>/', cart_views.add_to_cart, name='add_to_cart'),
    path('checkout/', order_views.checkout, name='checkout'),
    path('orders/', order_views.orders, name='user_orders')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
