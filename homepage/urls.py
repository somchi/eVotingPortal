from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^homepage/$', views.category.as_view(), name='candidate'),
]