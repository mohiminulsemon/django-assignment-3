from django.urls import path
from . import views

urlpatterns = [
    path('show-items', views.index, name='show-items'),
]