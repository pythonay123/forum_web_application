from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from .models import Profile
from dobwidget import DateOfBirthWidget


class UserLoginForm(AuthenticationForm):

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']

    # def clean_username(self):
    #     username = self.cleaned_data['username']
    #     if 1 <= frame_quality <= 31:
    #         return frame_quality
    #     else:
    #         raise forms.ValidationError('Frame Quality Value must be in this range (1 to 31)')


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = get_user_model()
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['title', 'image', 'address_line_1', 'address_line_2', 'street_address', 'country', 'summary',
                  'gender', 'gender', 'date_of_birth', 'phone']
        widgets = {
            'date_of_birth': DateOfBirthWidget(),
        }


class DeleteUserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['is_active']
        labels = {
            "is_active": "deactivate"
        }

    def __init__(self, *args, **kwargs):
        super(DeleteUserForm, self).__init__(*args, **kwargs)
        self.fields['is_active'].help_text = "Check this box if you are sure you want to delete this account."

    def clean_is_active(self):
        is_active = not(self.cleaned_data["is_active"])
        return is_active
