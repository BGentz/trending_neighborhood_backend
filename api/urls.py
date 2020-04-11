from django.urls import path
from .views import user_submit

urlpatterns = [
    # need url endpoints for the other views
    path("user_submit", user_submit, name="user_submit"),  # Guess - 'POST', {}
]