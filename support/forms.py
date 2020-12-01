from django import forms
from .models import AccountSupportMessage, VendorSupportMessage, GeneralSupportMessage, MarketSupportMessage


class AccountSupportForm(forms.ModelForm):

    class Meta:
        model = AccountSupportMessage
        fields = ['main_category', 'sub_category', 'username', 'email', 'message']

    def __init__(self, *args, **kwargs):
        super(AccountSupportForm, self).__init__(*args, **kwargs)
        self.fields['main_category'].disabled = True


class VendorSupportForm(forms.ModelForm):

    class Meta:
        model = VendorSupportMessage
        fields = ['main_category', 'sub_category', 'username', 'email', 'message']

    def __init__(self, *args, **kwargs):
        super(VendorSupportForm, self).__init__(*args, **kwargs)
        self.fields['main_category'].disabled = True


class GeneralSupportForm(forms.ModelForm):

    class Meta:
        model = GeneralSupportMessage
        fields = ['main_category', 'sub_category', 'username', 'email', 'message']

    def __init__(self, *args, **kwargs):
        super(GeneralSupportForm, self).__init__(*args, **kwargs)
        self.fields['main_category'].disabled = True


class MarketSupportForm(forms.ModelForm):

    class Meta:
        model = MarketSupportMessage
        fields = ['main_category', 'sub_category', 'username', 'email', 'message']

    def __init__(self, *args, **kwargs):
        super(MarketSupportForm, self).__init__(*args, **kwargs)
        self.fields['main_category'].disabled = True
