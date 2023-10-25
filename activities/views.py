from django.shortcuts import render, redirect
from .forms import ActivityForm
from .models import Activity

def add_activity(request, trip_id):
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            form.instance.trip_id = trip_id  # Assuming the trip_id is passed in the URL
            form.save()
            return redirect('activity-list', trip_id=trip_id)
    else:
        form = ActivityForm()
    return render(request, 'activities/add_activity.html', {'form': form})

def list_activities(request, trip_id):
    activities = Activity.objects.filter(trip_id=trip_id)
    return render(request, 'activities/list_activities.html', {'activities': activities})
