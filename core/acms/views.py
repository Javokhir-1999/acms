from rest_framework.generics import (ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView)
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import Person, Device, Event, Group
from .serializers import PersonSerializer, DeviceSerializer, EventSerializer, GroupSerializer


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size = 1000

class PersonListAPIView(ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    pagination_class = LargeResultsSetPagination

class PersonRetrieveAPIView(RetrieveAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class PersonDestroyAPIView(DestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        data = self.perform_destroy(instance)
        return Response('Deleted Successfully', status=201)
    
class PersonCreateAPIView(CreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class DeviceListAPIView(ListAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    pagination_class = LargeResultsSetPagination

class DeviceRetrieveAPIView(RetrieveAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class DeviceDestroyAPIView(DestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        data = self.perform_destroy(instance)
        return Response('Deleted Successfully', status=201)
    
class DeviceCreateAPIView(CreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class EventListAPIView(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    pagination_class = LargeResultsSetPagination

class EventRetrieveAPIView(RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventDestroyAPIView(DestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        data = self.perform_destroy(instance)
        return Response('Deleted Successfully', status=201)
    
class EventCreateAPIView(CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class GroupListAPIView(ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    pagination_class = LargeResultsSetPagination

class GroupRetrieveAPIView(RetrieveAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class GroupDestroyAPIView(DestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        data = self.perform_destroy(instance)
        return Response('Deleted Successfully', status=201)
    
class GroupCreateAPIView(CreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

