from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('addMovie', views.addmovierequest),
    path('addReview', views.addreviewrequest),
    path('addReview/<str:moviename>', views.addreviewrequest),
]

