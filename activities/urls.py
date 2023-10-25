from django.urls import path
from . import views

urlpatterns = [
    path('<int:trip_id>/add/', views.add_activity, name='add-activity'),
    path('<int:trip_id>/list/', views.list_activities, name='activity-list'),
]
