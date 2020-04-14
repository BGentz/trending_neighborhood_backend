from django.urls import path
from .views import user_submit, neighborhoods_data, events

urlpatterns = [
    # need url endpoints for the other views
    path("default_view/<str:city>", neighborhoods_data, name="default_view"),
    path("user_submit", user_submit, name="user_submit"),  # Guess - 'POST', {}
    path("events/<str:city>", events, name="events")
]