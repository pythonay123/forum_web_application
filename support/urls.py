from django.urls import path
from .views import SupportView, AccountSupportView, VendorSupportView, GeneralSupportView, MarketSupportView
from .views import AccountFormView, VendorFormView, GeneralFormView, MarketFormView, InstantReplyView

app_name = 'support'

urlpatterns = [
    path('', SupportView.as_view(), name='support'),
    path('account/', AccountSupportView.as_view(), name='account'),
    path('vendor/', VendorSupportView.as_view(), name='vendor'),
    path('general/', GeneralSupportView.as_view(), name='general'),
    path('market/', MarketSupportView.as_view(), name='market'),
    path('account/message', AccountFormView.as_view(), name='account-message'),
    path('vendor/message', VendorFormView.as_view(), name='vendor-message'),
    path('general/message', GeneralFormView.as_view(), name='general-message'),
    path('market/message', MarketFormView.as_view(), name='market-message'),
    path('query/', InstantReplyView.as_view(), name='instant-reply')
    # path('profile/', UserProfileView.as_view(), name='profile'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    # path('timezone/', set_timezone, name='set_timezone'),
]
