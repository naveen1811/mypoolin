from django.conf.urls import url
from django.views.generic.base import RedirectView

from utils import gplus_url
from . import views

urlpatterns = [
    url(r'^login/$', views.login_page),
    url(r'^get_google_login/$', views.get_google_login),
    url(r'^login/google_login/', RedirectView.as_view(permanent=False,
                                           url=gplus_url)),
]