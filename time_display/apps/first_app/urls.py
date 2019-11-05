from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^time_display$', views.display_time),
    url(r'^word_generator$', views.word_generator),
    url(r'^process$', views.process),
    url(r'^second_app$', include('apps.generate_word.urls'))
]
