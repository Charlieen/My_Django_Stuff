from django.urls import path, include

from basic_app import views
from basic_app.views import SchoolListView,SchoolDetailView,SchoolCreateView,SchoolUpdateView,SchoolDeleteView
from django.conf.urls import url

app_name ='basic_app'

urlpatterns = [
    path('',SchoolListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$',SchoolDetailView.as_view(), name='detail'),
    url(r'^create/$',SchoolCreateView.as_view(), name ='create'),
    url(r'^update/(?P<pk>\d+)/$',SchoolUpdateView.as_view(), name ='update'),
    url(r'^delete/(?P<pk>\d+)/$',SchoolDeleteView.as_view(), name ='delete')
]