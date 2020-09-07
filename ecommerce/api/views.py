from ..models import *
from . import serializers
from rest_framework import generics, status
from rest_framework.response import Response

class PersonView(generics.ListAPIView):
  queryset = Person.objects.all()
  serializer_class = serializers.PersonSerializer
  print(queryset)