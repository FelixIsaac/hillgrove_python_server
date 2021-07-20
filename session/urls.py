from django.urls import path
from . import views

urlpatterns = [
    path('solution/<topic>/<solution>', views.get_solution, name="get-solution"),
    path('hint/<topic>/<solution>', views.get_hint, name="get-hint"),
    path('all', views.get_sessions, name="get-sessions"),
    path('<session>', views.get_sessions, name="get-sessions"),
]
