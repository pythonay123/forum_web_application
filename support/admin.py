from django.contrib import admin
from .models import MainSupport, AccountSupportMessage, VendorSupportMessage, GeneralSupportMessage, MarketSupportMessage


# Register your models here.
admin.site.register(MainSupport)
admin.site.register(AccountSupportMessage)
admin.site.register(VendorSupportMessage)
admin.site.register(GeneralSupportMessage)
admin.site.register(MarketSupportMessage)
