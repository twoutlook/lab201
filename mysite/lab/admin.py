from django.contrib import admin

from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportMixin
from import_export import resources, fields
# from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import Labinfo
from .models import Labpower

from .models import Labteacher
from .models import Labstudent
from .models import Labtest
from .models import PrjSpec


class PrjSpecAdmin(admin.ModelAdmin):
    list_display=['f00','f01']
admin.site.register(PrjSpec,PrjSpecAdmin)


class LabinfoAdmin(admin.ModelAdmin):
    list_display=['f01','f02','f03']
admin.site.register(Labinfo,LabinfoAdmin)


class LabpowerAdmin(admin.ModelAdmin):
    list_display=['f01','f02','f03']
admin.site.register(Labpower,LabpowerAdmin)


class LabteacherAdmin(admin.ModelAdmin):
    list_display=['f01','f02','f03']
admin.site.register(Labteacher,LabteacherAdmin)

class LabstudentAdmin(admin.ModelAdmin):
    list_display=['f01','f02','f03']
admin.site.register(Labstudent,LabstudentAdmin)

class LabtestAdmin(admin.ModelAdmin):
    list_display=['f01','f02','f03']
admin.site.register(Labtest,LabtestAdmin)

