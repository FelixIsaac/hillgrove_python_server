from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/email', views.get_email, name='get-email')
]
