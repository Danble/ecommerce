from django.urls import path
from .api.views import PersonView

urlpatterns = [
    path('person', PersonView, name="person")
]
