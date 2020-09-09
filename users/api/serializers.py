from ..models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
  #uuid = serializers.CharField(max_length=36)
  
  class Meta:
    model = User
    fields = '__all__'