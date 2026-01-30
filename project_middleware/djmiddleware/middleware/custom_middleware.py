from django.http import HttpResponseForbidden


Blocked_IPS = ['127.0.0.1', '987.56.65.21']

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
