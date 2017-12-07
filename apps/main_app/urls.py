from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.main),
        url(r'^create$', views.create),
        url(r'^add/(?P<id>\d+)$', views.add), 
        url(r'^song/(?P<id>\d+)$', views.songUser),
        url(r'^show/(?P<id>\d+)$', views.showUser),
]
