from django.contrib import admin

from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportMixin
from import_export import resources, fields
# from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import Power

class PowerAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(Power,PowerAdmin)
    list_display=['f01','f02','f03']
admin.site.register(Power,PowerAdmin)
