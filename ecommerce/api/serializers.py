from ..models import *
from rest_framework import serializers

class PersonSerializer(serializers.ModelSerializer):
  class Meta:
    model = Person
    fields = ('user_id', 'name', 'last_named')