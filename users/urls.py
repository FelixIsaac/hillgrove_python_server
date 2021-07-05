from django.urls import path
from . import views

urlpatterns = [
    path('progress', views.progress, name="progress"),
]
