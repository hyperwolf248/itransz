from django.utils.deprecation import MiddlewareMixin

class ActivityTrackerMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Track user's real-time activity here
        pass
