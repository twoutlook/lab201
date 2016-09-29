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



class LabinfoAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(Power,PowerAdmin)
    list_display=['f01','f02','f03']
    class Meta:
        verbose_name = "信息"
        verbose_name_plural = "信息"
admin.site.register(Labinfo,LabinfoAdmin)


class LabpowerAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(Power,PowerAdmin)
    list_display=['f01','f02','f03']
admin.site.register(Labpower,LabpowerAdmin)


class LabteacherAdmin(admin.ModelAdmin):
    list_display=['f01','f02','f03']
    class Meta:
        verbose_name = "老师"
        verbose_name_plural = "老师"
admin.site.register(Labteacher,LabteacherAdmin)

class LabstudentAdmin(admin.ModelAdmin):
    list_display=['f01','f02','f03']
admin.site.register(Labstudent,LabstudentAdmin)

class LabtestAdmin(admin.ModelAdmin):
    list_display=['f01','f02','f03']
admin.site.register(Labtest,LabtestAdmin)

