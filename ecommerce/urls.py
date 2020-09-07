from django.urls import path
from .api import views

urlpatterns = [
    path("/", views.PersonView.as_view(), name="person")
]
