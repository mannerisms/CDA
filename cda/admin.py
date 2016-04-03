from django.contrib import admin
from .models import Person, PersonInGroup, Group, GroupType
from import_export.admin import ImportExportModelAdmin
from import_export import resources


class PersonResource(resources.ModelResource):

    class Meta:
        model = Person


class PersonAdmin(ImportExportModelAdmin):
    pass


# Register your models here.
admin.site.register(Group)
admin.site.register(GroupType)
admin.site.register(PersonInGroup)
admin.site.register(Person, PersonAdmin)