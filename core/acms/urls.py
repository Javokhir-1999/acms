from django.urls import path
from . import views

urlpatterns = [
   path(r'get/person', views.PersonListAPIView.as_view(), name='get-person-list'),
   path(r'get/device', views.DeviceListAPIView.as_view(), name='get-device-list'),
   path(r'get/event', views.EventListAPIView.as_view(), name='get-event-list'),
   path(r'get/group', views.GroupListAPIView.as_view(), name='get-group-list'),
   
   path(r'get/person/<int:pk>', views.PersonRetrieveAPIView.as_view(), name='get-person'),
   path(r'get/device/<int:pk>', views.DeviceRetrieveAPIView.as_view(), name='get-device'),
   path(r'get/event/<int:pk>', views.EventRetrieveAPIView.as_view(), name='get-event'),
   path(r'get/group/<int:pk>', views.GroupRetrieveAPIView.as_view(), name='get-group'),

   path(r'create/person', views.PersonCreateAPIView.as_view(), name='create-person'),
   path(r'create/device', views.DeviceCreateAPIView.as_view(), name='create-device'),
   path(r'create/event', views.EventCreateAPIView.as_view(), name='create-event'),
   path(r'create/group', views.GroupCreateAPIView.as_view(), name='group-event'),

   path(r'delete/person/<int:pk>', views.PersonDestroyAPIView.as_view(), name='delete-person'),
   path(r'delete/device/<int:pk>', views.DeviceDestroyAPIView.as_view(), name='delete-device'),
   path(r'delete/event/<int:pk>', views.EventDestroyAPIView.as_view(), name='delete-event'),
   path(r'delete/group/<int:pk>', views.GroupDestroyAPIView.as_view(), name='group-event'),
   
]