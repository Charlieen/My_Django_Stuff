from django.urls import path
from basic_app import views


# TEMPLATE TAGGING
app_name = 'basic_app88'

urlpatterns = [
    path('other/',views.other,name='other'),
    path('base/',views.base,name='base'),
    path('relative/',views.relative, name="relative")
]