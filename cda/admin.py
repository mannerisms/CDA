from django.contrib import admin
from .models import Person, Source, CellMast
from import_export.admin import ImportExportModelAdmin
from import_export import resources


class PersonResource(resources.ModelResource):
    class Meta:
        model = Person


class PersonAdmin(ImportExportModelAdmin):
    pass


class SourceResource(resources.ModelResource):
    class Meta:
        model = Source


class SourceAdmin(ImportExportModelAdmin):
    pass

class CellMastResource(resources.ModelResource):
    class Meta:
        model = Source


class CellMastAdmin(ImportExportModelAdmin):
    pass


# Register your models here.
admin.site.register(Person, PersonAdmin)
admin.site.register(Source, SourceAdmin)
admin.site.register(CellMast, CellMastAdmin)