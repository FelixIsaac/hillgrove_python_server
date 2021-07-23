from django.urls import path
from . import views

urlpatterns = [
    path('progress', views.progress, name="progress"),
    path('progress/<session>', views.progress, name="progress"),
    path('solution/<topic>/<solution>', views.solution_progress, name="solution"),
    path('xp', views.get_xp, name="get-xp")
]
