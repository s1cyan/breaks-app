from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.render_home_page, name="home"),
    url(r'^user-registration', views.render_user_registration, name="user-registration")
]
