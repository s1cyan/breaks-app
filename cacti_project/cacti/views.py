from django.shortcuts import render


# Create your views here.


def render_home_page(request):
    return render(request, "default.html")


def render_user_registration(request):
    return render(request, "user_registration.html")