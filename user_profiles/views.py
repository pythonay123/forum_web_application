from django.shortcuts import render, redirect
from django.views import View
from .forms import UserLoginForm, UserUpdateForm, ProfileUpdateForm, DeleteUserForm
from django.contrib.auth.views import LogoutView as AuthLogoutView
from django.views.generic import RedirectView
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from .models import Profile, UserEvaluation
from forums.models import Thread
import pytz
from django.core import exceptions
from django.views.generic.edit import UpdateView
from home.timezone import time_zone
from django.contrib.auth import get_user_model


# Create your views here.
class LoginView(View):
    form_class = UserLoginForm
    template_name = 'user_profiles/login.html'
    redirect_field_name = 'user_profiles:profile'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse(self.redirect_field_name))
        user_form = self.form_class()
        context = {'user_form': user_form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                request.session['django_timezone'] = time_zone(request)
                user.profile.timezone = time_zone(request)
                return HttpResponseRedirect(reverse(self.redirect_field_name))
            else:
                return HttpResponse("Account has been closed")
        user_form = self.form_class()
        context = {'user_form': user_form}
        return render(request, self.template_name, context)


class UserProfileView(View):
    template_name = 'user_profiles/general.html'

    @method_decorator(login_required)
    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    # if user has logged in will be directed to profile page
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_active:
            request.session['django_timezone'] = time_zone(request)
            request.user.profile.timezone = time_zone(request)
            u_form = UserUpdateForm(instance=request.user)
            p_form = ProfileUpdateForm(instance=request.user.profile)
            summary = request.user.profile.summary
            gender = request.user.profile.gender
            joined_date = request.user.profile.reg_date
            threads_number = request.user.userevaluation.number_of_threads_created
            posts_number = UserEvaluation.objects.get(user=request.user).number_of_posts
            profile_views = UserEvaluation.objects.get(user=request.user).profile_views
            userevaluation = UserEvaluation.objects.get(user=request.user)
            try:
                most_recent_thread = Thread.objects.filter(author=request.user).first()
                if len(most_recent_thread.post_set.all().first().content) > 50:
                    summary_of_last_reply = most_recent_thread.post_set.all().first().content[:50]
                else:
                    summary_of_last_reply = most_recent_thread.post_set.all().first().content
            except (exceptions.ObjectDoesNotExist, AttributeError):
                most_recent_thread = ""
                summary_of_last_reply = ""
            except TypeError:
                most_recent_thread = Thread.objects.filter(author=request.user).first()
                summary_of_last_reply = ""
            try:
                last_post = request.user.post_set.all().last()
                last_post_summary = last_post.content[:80]
            except (TypeError, AttributeError):
                last_post = ""
                last_post_summary = ""
            context = {
                'joined_date': joined_date,
                'gender': gender,
                'summary': summary,
                'u_form': u_form,
                'p_form': p_form,
                'threads_number': threads_number,
                'posts_number': posts_number,
                'profile_views': profile_views,
                'user_evaluation': userevaluation,
                'most_recent_thread': most_recent_thread,
                'summary_of_last_reply': summary_of_last_reply,
                'last_post': last_post,
                'last_post_summary': last_post_summary,
            }
            return render(request, self.template_name, context=context)
        else:
            return HttpResponseRedirect(reverse('user_profiles:login'))


class LogoutView(AuthLogoutView):
    template_name = 'user_profiles/logout.html'
    redirect_field_name = 'home:home'

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(self.redirect_field_name)


def set_timezone(request):
    template = 'user_profiles/set_timezone.html'
    if request.user.is_authenticated:
        if request.method == 'POST':
            request.session['django_timezone'] = request.POST['timezone']
            print(request.session.items())
            return redirect(reverse('user_profiles:profile'))
        else:
            return render(request, template, {'timezones': pytz.common_timezones})
    else:
        raise Http404


class UpdateProfileView(SuccessMessageMixin, UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    template_name = 'user_profiles/profile-settings.html'
    success_message = 'Your profile have been successfully updated'

    @method_decorator(login_required)
    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        if self.request.user.is_authenticated and self.request.user.is_active:
            # Call the base implementation first to get a context
            context = super().get_context_data(**kwargs)
            # Add more context to the context
            u_form = UserUpdateForm(instance=self.request.user)
            p_form = ProfileUpdateForm(instance=self.request.user.profile)
            summary = self.request.user.profile.summary
            gender = self.request.user.profile.gender
            joined_date = self.request.user.profile.reg_date
            threads_number = self.request.user.userevaluation.number_of_threads_created
            posts_number = UserEvaluation.objects.get(user=self.request.user).number_of_posts
            profile_views = UserEvaluation.objects.get(user=self.request.user).profile_views
            userevaluation = UserEvaluation.objects.get(user=self.request.user)
            try:
                most_recent_thread = Thread.objects.filter(author=self.request.user).first()
                if len(most_recent_thread.post_set.all().first()) > 30:
                    summary_of_last_reply = most_recent_thread.post_set.all().first()[:30]
                else:
                    summary_of_last_reply = most_recent_thread.post_set.all().first()
            except (exceptions.ObjectDoesNotExist, AttributeError):
                most_recent_thread = ""
                summary_of_last_reply = ""
            except TypeError:
                most_recent_thread = Thread.objects.filter(author=self.request.user).first()
                summary_of_last_reply = ""
            try:
                last_post = self.request.user.post_set.all().first()
                last_post_summary = last_post[:30]
            except TypeError:
                last_post = ""
                last_post_summary = ""
            additional_context = {
                'joined_date': joined_date,
                'gender': gender,
                'summary': summary,
                'u_form': u_form,
                'p_form': p_form,
                'threads_number': threads_number,
                'posts_number': posts_number,
                'profile_views': profile_views,
                'user_evaluation': userevaluation,
                'most_recent_thread': most_recent_thread,
                'summary_of_last_reply': summary_of_last_reply,
                'last_post': last_post,
                'last_post_summary': last_post_summary,
            }
            context.update(additional_context)
            return context


class UserDeleteAccountView(View):
    form_class = DeleteUserForm
    template_name = 'user_profiles/close-account.html'
    redirect_field_name = 'home:home'

    @method_decorator(login_required)
    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user_form = self.form_class()
            context = {'user_form': user_form}
            return render(request, self.template_name, context)
        return HttpResponseRedirect(reverse(self.redirect_field_name))

    def post(self, request, *args, **kwargs):
        pk = request.user.id
        User = get_user_model()
        user = User.objects.get(pk=pk)
        if request.user.is_authenticated and request.user.id == user.id:
            user_form = self.form_class(request.POST, instance=user)
            if user_form.is_valid():
                deactivate_user = user_form.save(commit=False)
                user.is_active = False
                deactivate_user.save()
                return HttpResponseRedirect(reverse(self.redirect_field_name))
