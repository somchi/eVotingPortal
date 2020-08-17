from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^registers/$', views.Register, name='register'),

    url(r'^Location/(?P<pk>[0-9]+)/$', views.LocationChange.as_view(), name='Location'),
    url(r'^registration/$', views.Registratio, name='registration'),
]