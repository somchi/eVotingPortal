from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^registers/$', views.Register, name='register'),
    url(r'^StudentLog/$', views.Student_Registration, name='StudentLog'),
    url(r'^candidate/$', views.IndexView.as_view(), name='candidate'),
    url(r'^(?P<pk>\d+)/details/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/candidates_detail/$', views.CandidateView.as_view(), name='candidates_detail'),
    url(r'^(?P<pk>\d+)/location/$', views.VoteSpot.as_view(), name='VoteSpot'),
    url(r'^(?P<candidate_category_id>\d+)/election_vote/$', views.election_vote, name='election_votes'),
    url(r'^election_result/$', views.election_result.as_view(), name='election_result'),
    url(r'^authenticate/$', views.Authentications, name='authentication'),
    #url(r'^context/$', views.Context, name='context'),
    url(r'^(?P<pk>\d+)/update/$', views.StudetUpdate.as_view(), name='update'),
    url(r'^logout/$', views.log_out, name='logOut'),
]
