from django.contrib import admin
from django.contrib.auth.models import Group as DjGroup
from .models import Person, Device, Event, Group


admin.site.unregister(DjGroup)

class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'active', 'group', 'photo_tag')
    readonly_fields = ('photo_tag',)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'address', 'login', 'password')
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'source', 'type', 'address', 'time', 'details')
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(Person, PersonAdmin)
admin.site.register(Device, DeviceAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Group, GroupAdmin)
