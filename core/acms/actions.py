from isapi.hikapi.AccessControl import AccessControl
from isapi.hikapi.Intelligent import Intelligent
from isapi.hikapi.System import System
from isapi.hikapi.Event import Event
from .models import Person, Device, Event, Group

obj1 = AccessControl()
obj2 = Intelligent()
obj3 = Event()
obj4 = System()

def create_person_action(user):
    print('\n > create_person_action < \n')
    devices = Device.objects.all()
    obj1.add_UserInfoRecord(devices, user)

def modify_person_action(user):
    print('\n > modify_person_action < \n')
    devices = Device.objects.all()
    obj1.put_UserInfoModify(devices, user)

def create_person_faceID_action(user):
    print('\n > create_person_faceID_action < \n')
    devices = Device.objects.all()
    obj2.add_FaceDataRecord(devices, user)

def delete_person_action(user):
    print('\n > delete_person_action < \n')
    devices = Device.objects.all()
    obj1.del_UserInfoDetailDelete(devices, user)