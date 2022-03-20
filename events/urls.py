from django.urls import path

from . import views

urlpatterns = [
    path('', views.events, name='event list page'),
]