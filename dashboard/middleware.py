from django.contrib.auth import REDIRECT_FIELD_NAME, login
from django.shortcuts import redirect, render
from django.urls import resolve
from django.urls import reverse
def simple_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        r = resolve(request.path)
        if r._func_path[:r._func_path.find('.')] in ["dashboard"]: #add app name IN LIST  to APPLY middleware in that app
            if request.user.is_superuser or request.path==reverse('logindashboard'):
                response = get_response(request)
            else:
                rev = reverse('logindashboard') + "?next="+request.get_full_path()
                response = redirect(rev)
        else:
            response = get_response(request)
        return response
    return middleware