from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.dumb_santa_register, name='dumb_santa_register'),
]