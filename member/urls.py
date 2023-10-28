from django.urls import path
from django.urls import path
from .views import Homepage, PostDetailView
app_name = 'member'
urlpatterns=[
    path('',Homepage.as_view(), name='index'),
    path('detail/<int:pk>/',PostDetailView.as_view(), name='detail')
]