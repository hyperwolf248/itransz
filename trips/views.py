from django.shortcuts import render, redirect
from .forms import TripForm
from .models import Trip
from api.gpt import generate_itinerary  # Import the function here

def create_trip(request):
    if request.method == 'POST':
        form = TripForm(request.POST)
        if form.is_valid():
            trip = form.save(commit=False)  # Do not save yet
            itinerary = generate_itinerary({
                'destination': trip.destination,
                'trip_type': trip.trip_type,
                'theme': trip.theme,
                # ... include other fields as required
            })
            trip.itinerary = itinerary  # Store the generated itinerary in the Trip model if you have a field for it
            trip.save()  # Now save the trip with the generated itinerary
            return redirect('trip-list')
    else:
        form = TripForm()
    return render(request, 'trips/create_trip.html', {'form': form})
