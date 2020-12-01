from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from forums.models import Thread
from django.urls import reverse
import string


# Create your models here.
# class OrderPostsManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().order_by('posted_date')


class Post(models.Model):
    # Title will be the same as the thread title prefix with Re: or could exist with no title
    content = models.TextField(max_length=5000, blank=False, null=False)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    posted_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        # Create post name/designation using the post and author
        name = str(self.thread)[:10]
        name = name.translate({ord(c): None for c in string.whitespace})
        post_name = str(self.author) + '_' + name + str(self.posted_date)
        return post_name

    def get_absolute_url(self):
        return reverse('posts:post-detail')

    def get_form_url(self):
        return reverse('posts:post-create')

    def get_post_preview(self):
        return self.content[:50]

    class Meta:
        ordering = ['posted_date']
        get_latest_by = ["posted_date"]
