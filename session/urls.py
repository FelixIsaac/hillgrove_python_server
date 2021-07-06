from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_sessions, name="get-sessions"),
    path('<session>', views.get_sessions, name="get-sessions")
]
