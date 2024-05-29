from django.urls import path 
from .views import generate_scenario, commit_message
urlpatterns = [
    path("scenario/", generate_scenario),
    path("commit-message/", commit_message)
]