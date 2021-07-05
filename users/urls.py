from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_progress, name="get-progress"),
    path('update', views.update_progress, name="update-progress"),
]
