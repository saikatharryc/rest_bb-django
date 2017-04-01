from __future__ import unicode_literals
from django.contrib import admin
from import_export import resources
from import_export.resources import ModelResource
from import_export.admin import ImportExportModelAdmin
from .models import Organizations


class CampData(resources.ModelResource):
    """docstring for CampData"""
    class Meta:
        model = Organizations
        exclude = ('id', )
        import_id_fields = ('org_name',)
        skip_unchanged = True


class OrgAdmin(ImportExportModelAdmin):
    """docstring for OrgAdmin"""
    resource_class = CampData
# Register your models here.

# admin.site.register(Organizations)

admin.site.register(Organizations, OrgAdmin)
