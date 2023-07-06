"""Example URL configuration."""

from django.urls import path, re_path
from django.http import HttpResponse
from . import views
from .views import add, index

urlpatterns = [
    re_path(r'^$', views.index, name='pde'),
    re_path(r'^details/(?P<user>\w+)$', views.details, name='user'),
    re_path(r'^add/$', views.add, name='add'),
    # url(r'files/(?P<path>.*)$', views.serve),
    re_path(
        r"^files/(?P<path>.+)",  # up to you, but path is required
        views.get, name='get'  # your view, your permissions

    ),

]
