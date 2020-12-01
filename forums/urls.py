from django.urls import path
from .views import MarketplaceListView, ThreadListView, DirectoryThreadView, CreateThreadView, ThreadDeleteView, ThreadUpdateView


app_name = 'forums'

urlpatterns = [
    path('', ThreadListView.as_view(), name='forum'),
    path('category/<path:category>/', DirectoryThreadView.as_view(), name='category'),
    path('<path:category>/thread/new/', CreateThreadView.as_view(), name='create-thread'),
    path('thread/<int:pk>/delete/', ThreadDeleteView.as_view(), name='thread-delete'),
    path('thread/<int:pk>/update/', ThreadUpdateView.as_view(), name='thread-update'),
    path('marketplace/', MarketplaceListView.as_view(), name='marketplace'),
    # path('success/', success, name='success'),
]
