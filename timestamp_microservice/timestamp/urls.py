from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:time_string>', views.service, name='service'),
]