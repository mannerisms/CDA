from django.contrib import admin
from .models import Person, PersonInGroup, Group, GroupType

# Register your models here.
admin.site.register(Person)
admin.site.register(Group)
admin.site.register(GroupType)
admin.site.register(PersonInGroup)

