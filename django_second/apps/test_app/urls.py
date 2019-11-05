from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.pidr),
    url(r'^new$', views.gnida),
    url(r'^create$', views.create),
    url(r'^(?P<number>[0-9]{2})$', views.show),
    url(r'^(?P<number>\d+)/edit$', views.edit),
    url(r'^(?P<number>\d+)/delete', views.destroy)
]


