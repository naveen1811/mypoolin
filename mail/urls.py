from django.conf.urls import url
from django.views.generic.base import RedirectView

from . import views

urlpatterns = [
    url(r'^login/$', views.login_page),
    url(r'^get_google_login/$', views.get_google_login),
    url(r'^login/google_login/', RedirectView.as_view(permanent=False,
                                           url="https://accounts.google.com/o/oauth2/auth?redirect_uri="
                                               "http://localhost:8000/mail/get_google_login/"
                                               "&response_type=code&client_id="
                                               "977890289014-oug5ohgk1q6qod8gp1hbllm4c4qo2cjh.apps.googleusercontent.com"
                                               "&scope=https://www.googleapis.com/auth/userinfo.email "
                                               "https://www.googleapis.com/auth/contacts")),
]