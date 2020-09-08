from ..models import *
from . import serializers
from rest_framework import generics, status
from rest_framework.response import Response
from django.http.response import JsonResponse

def PersonView(request):
  return JsonResponse({"message": "hello world!"})