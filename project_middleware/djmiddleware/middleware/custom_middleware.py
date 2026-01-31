from django.http import HttpResponseForbidden
from middleware.models import Store


# Blocked_IPS = ['127.0.0.1', '987.56.65.21']
Blocked_IPS = ['987.56.65.21']


class IPBlockingMiddleware:
    """
    Middleware to block requests from specific IP addresses.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def get_ip(self, request):
        return request.META.get('REMOTE_ADDR')

    def __call__(self, request):
        ip = self.get_ip(request)
        print(ip)
        if ip in Blocked_IPS:
            return HttpResponseForbidden("<h2>Forbidden: IP not allowed.</h2>")
        response = self.get_response(request)
        return response
    
class CheckBMPHeader:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        headers =  request.headers
        if 'bmp' not in headers:
            return HttpResponseForbidden("<h2>Forbidden: BMP header missing.</h2>")
        else:
            if not Store.objects.filter(bmp_id = headers.get('bmp')).exists():
                return HttpResponseForbidden("<h2>Wrong bmp</h2>")
        response = self.get_response(request)
        return response
