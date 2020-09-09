""" from rest_framework.views import APIView
from rest_framework.response import Response """
from rest_framework.generics import ListCreateAPIView
from .serializers import PersonSerializer
from ..models import Person

from users.models import User

class PersonView(ListCreateAPIView):
  """ def get(self, request):
    if request.method == 'GET':
      all_persons = Person.objects.all()
      serialized_persons = PersonSerializer(all_persons, many=True)
      return Response(serialized_persons.data)
  def post(self, request):
    #TODO un-hardcore this
    user1 = User.objects.all()
    user1 = user1[1]
    serializer = PersonSerializer(data=request.data)
    if serializer.is_valid():
      user = {}
      user.update({**serializer.data, 'user_id': user1})
      person_instance = Person.objects.create(**user)
      return Response({"message": "id{} created".format(person_instance.id)})
    else:
      return Response({"errors": serializer.errors}) """

  serializer_class = PersonSerializer
  queryset = Person.objects.all()

  """ def perform_create(self, serializer):
    user1 = User.objects.all()
    user1 = user1[1]
    user = {}
    data = self.request.data
    print(data)
    user.update({**data, 'user_id': user1})

    serializer.save(user=user) """

  def post(self, request, *args, **kwargs):
    print("this is a: {}".format(request.data))