from ipaddr import client_ip
import geoip2.database
import os
from django.conf import settings


def user_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def time_zone(request):
    ipaddr = client_ip(request)
    reader = geoip2.database.Reader(os.path.join(settings.BASE_DIR, 'static\\static_root\\geoip\\GeoLite2-City.mmdb'))
    if ipaddr in ('127.0.0.1', '192.168.1.10',):
        ipaddr = '109.79.129.171'
    try:
        response = reader.city(ipaddr)
        timezone = response.location.time_zone
    except geoip2.errors.AddressNotFoundError:
        timezone = None
    return timezone
