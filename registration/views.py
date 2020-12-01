from django.shortcuts import render
from django.views import View
from .forms import UserLoginForm, UserRegisterForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth import login, authenticate
import pytz
from home.timezone import time_zone


# Create your views here.
class HomeView(View):
    form_class = UserLoginForm
    template_name = 'registration/index.html'

    def get(self, request, *args, **kwargs):
        user_form = self.form_class()
        context = {'user_form': user_form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        user_form = self.form_class(request.POST)
        context = {'user_form': user_form}
        if user_form.is_valid():
            cd = user_form.cleaned_data()
            print(cd.get('username'), cd.get('password'))
            return HttpResponseRedirect(reverse('home:home'))
        return render(request, self.template_name, context)


# Create your views here.
class RegisterView(View):
    form_class = UserLoginForm
    template_name = 'registration/index.html'

    def get(self, request, *args, **kwargs):
        user_form = self.form_class()
        context = {'user_form': user_form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        user_form = self.form_class(request.POST)
        context = {'user_form': user_form}
        if user_form.is_valid():
            cd = user_form.cleaned_data()
            print(cd.get('username'), cd.get('password'))
            return HttpResponseRedirect(reverse('success'))
        return render(request, self.template_name, context)


class UserRegisterView(View):
    form_class = UserRegisterForm
    template_name = 'registration/register.html'

    def get(self, request, *args, **kwargs):
        user_form = self.form_class()
        context = {'user_form': user_form, 'timezones': pytz.common_timezones}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        user_form = self.form_class(request.POST)
        context = {'user_form': user_form, 'timezones': pytz.common_timezones}
        User = get_user_model()
        if user_form.is_valid():
            new_user = user_form.save()
            new_user.refresh_from_db()
            new_user.save()
            username = user_form.cleaned_data.get('username')
            password = user_form.cleaned_data.get('password1')
            country = user_form.cleaned_data.get('country')
            request.session['django_timezone'] = time_zone(request)
            user = authenticate(request, username=username, password=password)
            user.profile.timezone = request.session['django_timezone']
            login(request, user)
            return HttpResponseRedirect(reverse('user_profiles:profile'))
        return render(request, self.template_name, context)
