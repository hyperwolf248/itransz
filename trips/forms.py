from django import forms
from .models import Trip

class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['start_date', 'end_date', 'destination', 'trip_type', 'theme', 'staying_preference', 'cost_parameter']
