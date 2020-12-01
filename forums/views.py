from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .models import Directory, Thread
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache


directories = Directory.objects.all()
threads = Thread.objects.all()


# Create your views here.
class MarketplaceListView(ListView):
    model = Directory
    template_name = 'forums/marketplace_list_view.html'
    context_object_name = 'directories'
    # paginate_by = 5


class ThreadListView(ListView):
    model = Thread
    template_name = 'forums/thread_list_view.html'
    context_object_name = 'threads'
    # paginate_by = 5


class DirectoryThreadView(ListView):
    model = Directory
    template_name = 'forums/category-threads.html'

    def get(self, request, *args, **kwargs):
        directory = Directory.objects.get(section_name=self.kwargs['category'])
        thds = directory.thread_set.all()
        category = self.kwargs['category']
        context = {'threads': thds, 'category': category}
        return render(request, self.template_name, context)


class CreateThreadView(CreateView):
    template_name = 'forums/thread_form.html'
    model = Thread
    fields = ['topic', 'content']
    context_object_name = 'thread'

    @method_decorator(login_required)
    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        if self.get_form().is_valid:
            category = Directory.objects.get(section_name=kwargs['category'])
            topic = self.request.POST.get('topic')
            content = self.request.POST.get('content')
            new_thread = Thread.objects.create(directory=category, topic=topic, content=content, author=self.request.user)
            # number_of_threads = self.model.objects.all().count()
            category.number_topics = category.thread_set.all().count()
            category.save()
            print(category.number_topics)
            return redirect(reverse('forums:category', kwargs={'category': category}))

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.category = Directory.objects.get(section_name=self.kwargs.get('category'))
        return super().form_valid(form)


class ThreadDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Thread
    context_object_name = 'thread'
    success_url = '/'

    def test_func(self):
        thread = self.get_object()
        if self.request.user == thread.author:
            return True
        return False


class ThreadUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Thread
    fields = ['topic', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        thread = self.get_object()
        if self.request.user == thread.author:
            return True
        return False
