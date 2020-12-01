from django.db import models
from PIL import Image
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
import os
from django.conf import settings


# Create your models here.
class Directory(models.Model):
    section_name = models.CharField(max_length=120, unique=True)
    number_topics = models.IntegerField(null=False, blank=False, default=0)
    number_posts = models.IntegerField(null=False, blank=False, default=0)
    dir_image = models.ImageField(default='directories/images/default-image.jpg', upload_to='directories/images/', null=True, blank=True)

    def __str__(self):
        return self.section_name

    # Override the save method
    def save(self):
        super().save()
        img = Image.open(self.dir_image.path)
        if img.width != 200 and img.height != 200:
            output_size = (200, 200)
            img.resize(output_size, Image.ANTIALIAS).save(self.dir_image.path)

    def delete(self, using=None, keep_parents=False):
        super().delete()
        if self.dir_image.path != os.path.join(settings.MEDIA_ROOT, 'directories/images/default-image.jpg'):
            os.remove(self.dir_image.path)

    def get_absolute_url(self):
        return reverse('forums:category', kwargs={'category': self.section_name})

    class Meta:
        ordering = ['section_name']


# class OrderThreadsManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().order_by()


class Thread(models.Model):
    directory = models.ForeignKey(Directory, on_delete=models.CASCADE)
    topic = models.CharField(max_length=100)
    content = models.TextField(max_length=5000)
    posted_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    number_of_views = models.IntegerField(null=False, blank=False, default=0)
    active = models.BooleanField(default=True)
    number_of_posts = models.IntegerField(null=False, blank=False, default=0)
    last_active_post = models.DateTimeField(auto_now_add=True, auto_now=False)
    admin_message = models.TextField(max_length=600, null=True, blank=True)

    def __str__(self):
        return self.topic

    def get_absolute_url(self):
        return reverse('posts:thread-detail', args=(self.pk,))

    class Meta:
        ordering = ['-posted_date']
