from django.shortcuts import render, redirect
from .forms import AccountSupportForm, VendorSupportForm, GeneralSupportForm, MarketSupportForm
from django.views import View
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib import messages


# Create your views here.
class SupportView(View):
    context = {}
    template_name = 'support/support.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)


class AccountSupportView(View):
    context = {}
    template_name = 'support/account_support.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)


class VendorSupportView(View):
    context = {}
    template_name = 'support/vendor_support.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)


class GeneralSupportView(View):
    context = {}
    template_name = 'support/general_support.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)


class MarketSupportView(View):
    context = {}
    template_name = 'support/marketplace_support.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)


class AccountFormView(View):
    form_class = AccountSupportForm
    template_name = 'support/support_form.html'
    redirect_field_name = 'user_profiles:profile'

    def get(self, request, *args, **kwargs):
        support_form = self.form_class()
        context = {'support_form': support_form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        support_form = self.form_class(request.POST)
        User = get_user_model()
        context = {'support_form': support_form}
        if support_form.is_valid():
            support_form.save()
            check_user = support_form.cleaned_data.get('username')
            if check_user == request.user.username and request.user.is_authenticated:
                messages.success(request, f'Your query has been successfully sent to support')
                return redirect('support:instant-reply')
            messages.error(request, f'You have to be logged in and use your username to send a query to support')
            return render(request, self.template_name, context)
        messages.warning(request, f'Your query form is missing some required parameters')
        return render(request, self.template_name, context)


class VendorFormView(View):
    form_class = VendorSupportForm
    template_name = 'support/support_form.html'
    redirect_field_name = 'user_profiles:profile'

    def get(self, request, *args, **kwargs):
        support_form = self.form_class()
        context = {'support_form': support_form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        support_form = self.form_class(request.POST)
        User = get_user_model()
        context = {'support_form': support_form}
        if support_form.is_valid():
            support_form.save()
            check_user = support_form.cleaned_data.get('username')
            if check_user == request.user.username and request.user.is_authenticated:
                messages.success(request, f'Your query has been successfully sent to support')
                return redirect('support:instant-reply')
            messages.error(request, f'You have to be logged in and use your username to send a query to support')
            return render(request, self.template_name, context)
        messages.warning(request, f'Your query form is missing some required parameters')
        return render(request, self.template_name, context)


class GeneralFormView(View):
    form_class = GeneralSupportForm
    template_name = 'support/support_form.html'
    redirect_field_name = 'user_profiles:profile'

    def get(self, request, *args, **kwargs):
        support_form = self.form_class()
        context = {'support_form': support_form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        support_form = self.form_class(request.POST)
        User = get_user_model()
        context = {'support_form': support_form}
        if support_form.is_valid():
            support_form.save()
            check_user = support_form.cleaned_data.get('username')
            if check_user == request.user.username and request.user.is_authenticated:
                messages.success(request, f'Your query has been successfully sent to support')
                return redirect('support:instant-reply')
            messages.error(request, f'You have to be logged in and use your username to send a query to support')
            return render(request, self.template_name, context)
        messages.warning(request, f'Your query form is missing some required parameters')
        return render(request, self.template_name, context)


class MarketFormView(View):
    form_class = MarketSupportForm
    template_name = 'support/support_form.html'
    redirect_field_name = 'user_profiles:profile'

    def get(self, request, *args, **kwargs):
        support_form = self.form_class()
        context = {'support_form': support_form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        support_form = self.form_class(request.POST)
        User = get_user_model()
        context = {'support_form': support_form}
        if support_form.is_valid():
            support_form.save()
            check_user = support_form.cleaned_data.get('username')
            if check_user == request.user.username and request.user.is_authenticated:
                messages.success(request, f'Your query has been successfully sent to support')
                return redirect('support:instant-reply')
            messages.error(request, f'You have to be logged in and use your username to send a query to support')
            return render(request, self.template_name, context)
        messages.warning(request, f'Your query form is missing some required parameters')
        return render(request, self.template_name, context)


class InstantReplyView(View):
    context = {}
    template_name = 'support/message.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)
