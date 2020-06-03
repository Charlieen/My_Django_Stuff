
from django.conf.urls import url
from AppTwo import views

urlpatterns = [
    url(r'^', views.show, name='show'),
    url(r'^', views.help, name='help'),

]