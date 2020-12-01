from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.urls import reverse
from forums.models import Directory, Thread
import geoip2.database
import geoip2.errors
import os
from django.conf import settings
from .timezone import user_ip
from ipaddr import client_ip
from posts.models import Post
from datetime import datetime


# Create your views here.
class ForumListView(ListView):
    template_name = 'home/home.html'

    def get(self, request, *args, **kwargs):
        list_of_directories = Directory.objects.all().order_by('section_name')
        all_posts = Post.objects.all()
        all_thread = Thread.objects.all()
        try:
            last_10 = all_thread[:10]
        except Exception:
            last_10 = all_thread
        reader = geoip2.database.Reader(os.path.join(settings.BASE_DIR, 'static\\static_root\\geoip\\GeoLite2-City.mmdb'))
        ip = user_ip(request)
        if ip in ('127.0.0.1', '192.168.1.10',):
            ip = '109.79.129.171'
        try:
            response = reader.city(ip)
            request.session['django_timezone'] = response.location.time_zone
        except geoip2.errors.AddressNotFoundError:
            pass
        context = {"list_of_directories": list_of_directories, 'all_posts': all_posts, 'recent_threads': last_10}
        return render(request, self.template_name, context)
