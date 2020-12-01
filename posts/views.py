from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.core import exceptions
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from forums.models import Thread

posts = Post.objects.all()
threads = Thread.objects.all()


def number_of_post_category(category):
    number_posts = 0
    global threads
    threads_in_category = Thread.objects.filter(directory=category)
    number_in_category = threads_in_category.count()
    # print(number_in_category)
    for thread in threads_in_category:
        num_posts = thread.number_of_posts
        number_posts += num_posts
    print(number_posts)
    return number_posts


# Create your views here.
class ThreadDetailView(LoginRequiredMixin, DetailView):
    template_name = 'posts/thread_detail.html'
    model = Thread
    context_object_name = 'thread'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the posts related to this thread
        pk = self.kwargs.get(self.pk_url_kwarg)
        current_thread = self.model.objects.get(pk=pk)
        thread_posts = current_thread.post_set.order_by('posted_date')
        context['posts'] = thread_posts
        return context


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    context_object_name = 'post'


class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = 'posts/post_form.html'
    model = Post
    fields = ['content']

    def post(self, request, *args, **kwargs):
        if self.get_form().is_valid:
            thread = Thread.objects.get(pk=kwargs['pk'])
            new_post = Post(content=self.request.POST.get('content'), thread=thread, author=self.request.user)
            new_post.save()
            thread.number_of_posts = thread.post_set.all().count()
            thread.save()
            thread.directory.number_posts = number_of_post_category(thread.directory)
            thread.directory.save()
            return HttpResponseRedirect(reverse('posts:thread-detail', kwargs={'pk': thread.id}))

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
