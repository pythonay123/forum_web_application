from django.db import models
from django.contrib.auth import get_user_model
from PIL import Image
import os
from django.conf import settings
from django_countries.fields import CountryField
from phone_field import PhoneField
from django.urls import reverse


GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

# Create your models here.
User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=25, null=True, blank=True)
    summary = models.TextField(max_length=500, null=True, blank=True)
    image = models.ImageField(default='user_profiles/images/default.jpg', upload_to='user_profiles/images/', null=True)
    address_line_1 = models.CharField(max_length=200, null=True, blank=True)
    address_line_2 = models.CharField(max_length=200, null=True, blank=True)
    street_address = models.TextField(max_length=500, null=True, blank=True)
    country = CountryField(blank_label='(select country)')
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_birth = models.DateField(null=True, blank=True)
    phone = PhoneField(blank=True)
    reg_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    modified_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    timezone = models.CharField(max_length=50, default='UTC')

    def __str__(self):
        return '{} Profile'.format(self.user.username.capitalize())

    # Override the save method
    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.width != 200 and img.height != 200:
            output_size = (200, 200)
            img.resize(output_size, Image.ANTIALIAS).save(self.image.path)

    def delete(self, using=None, keep_parents=False):
        super().delete()
        if self.image.path != os.path.join(settings.MEDIA_ROOT, 'user_profiles/images/default.jpg'):
            os.remove(self.image.path)

    def get_absolute_url(self):
        return reverse('user_profiles:profile')


USER_LEVEL = (
    ('No Level', 'No Level'),
    ('Bronze', 'Bronze'),
    ('Silver', 'Silver'),
    ('Gold', 'Gold'),
)

SENIORITY_CHOICES = (
        ('Newcomer', 'Newcomer'),
        ('Basic Experience', 'Basic Experience'),
        ('Intermediate Experience', 'Intermediate Experience'),
        ('Advanced Experience', 'Advanced Experience'),
    )


class UserEvaluation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_rating = models.IntegerField(null=False, blank=False, default=0)
    points = models.IntegerField(null=False, blank=False, default=0)
    user_level = models.CharField(max_length=100, choices=USER_LEVEL, default='No Level')
    seniority = models.CharField(max_length=100, choices=SENIORITY_CHOICES, default='Newcomer')
    number_of_threads_created = models.IntegerField(null=False, blank=False, default=0)
    number_of_posts = models.IntegerField(null=False, blank=False, default=0)
    active = models.BooleanField(default=True)
    profile_views = models.IntegerField(null=False, blank=False, default=0)
    admin_message = models.TextField(max_length=600, null=True, blank=True)
