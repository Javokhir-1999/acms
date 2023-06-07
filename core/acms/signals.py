from .models import Person, Device, Event, Group
from django.db.models.signals import post_save, post_delete
from .actions import create_person_action, create_person_faceID_action, delete_person_action, modify_person_action

def create_person(sender, created, instance, **kwargs):
    if created:
        print('\n ~ create_person - signal ~ \n')
        create_person_action(instance)
        create_person_faceID_action(instance)
    else:
        print('\n ~ modify_person - signal ~ \n')
        modify_person_action(instance)


def delete_person(sender, instance, **kwargs):
    print('\n ~ delete_person - signal ~ \n')
    delete_person_action(instance)
    import os
    os.remove('media/'+instance.photo.name)

post_save.connect(create_person, sender=Person)
post_delete.connect(delete_person, sender=Person)

