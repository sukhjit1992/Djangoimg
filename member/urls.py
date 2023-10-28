from django.urls import path
from django.urls import path
from .views import Homepage
app_name = 'member'
urlpatterns=[
    path('',Homepage.as_view(), name='index'),
]