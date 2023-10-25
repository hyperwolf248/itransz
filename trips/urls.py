from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_trip, name='create-trip'),
    path('list/', views.list_trips, name='trip-list'),
]
