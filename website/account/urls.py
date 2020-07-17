from django.conf.urls import url, include
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^$', views.rps, name='rps'),
    url(r'^register/$', views.signup, ()),
    url(r'^update/$', views.update_profile, ()),
    url(r'^login/$', login, {'template_name': 'account/login.html'}),
    url(r'^logout/$', logout),
    url(r'^rps_play$', views.rps_play)
]
