from django.db import models

class Trip(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    destination = models.CharField(max_length=200)
    trip_type = models.CharField(choices=[('family', 'Family'), ('friends', 'Friends'), ('backpack', 'Backpack')], max_length=50)
    theme = models.CharField(choices=[('adventure', 'Adventure'), ('holiday', 'Holiday'), ('spiritual', 'Spiritual')], max_length=50)
    staying_preference = models.TextField()
    cost_parameter = models.CharField(choices=[('cheap', 'Cheap'), ('budget', 'Budget'), ('luxury', 'Luxury')], max_length=50)
    itinerary = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.destination
