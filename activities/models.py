from django.db import models

class Activity(models.Model):
    trip = models.ForeignKey('trips.Trip', on_delete=models.CASCADE)
    activity_name = models.CharField(max_length=200)
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('in_progress', 'In Progress')], max_length=50)
    
    def __str__(self):
        return self.activity_name
