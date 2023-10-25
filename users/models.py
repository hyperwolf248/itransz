from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    dietary_preferences = models.CharField(max_length=200, null=True, blank=True)
    # Add other custom fields if required
