from django.urls import path

from . import views

urlpatterns = [
    path('', views.list_menu),
    path('add', views.add_menu),
]

