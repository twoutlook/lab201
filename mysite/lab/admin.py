from django.contrib import admin

from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportMixin
from import_export import resources, fields
# from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import Info
from .models import Labpower

from .models import Teacher
from .models import Student
from .models import Team


from .models import Labtest
from .models import PrjSpec


# class PrjSpecAdmin(admin.ModelAdmin):
#     list_display=['f00','f01']
# admin.site.register(PrjSpec,PrjSpecAdmin)


class InfoAdmin(admin.ModelAdmin):
    list_display=['f01','f02','f03']
admin.site.register(Info,InfoAdmin)


# class LabpowerAdmin(admin.ModelAdmin):
#     list_display=['f01','f02','f03']
# admin.site.register(Labpower,LabpowerAdmin)


class TeacherAdmin(admin.ModelAdmin):
    list_display=['userid','password','username','mailbox']
admin.site.register(Teacher,TeacherAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display=['userid','password','username','mailbox','teacher','team']
    # list_display=['userid','username','mailbox','teacher']
    
admin.site.register(Student,StudentAdmin)

# class GroupAdmin(admin.ModelAdmin):
#     list_display=['groupid','groupname']
# admin.site.register(Group,GroupAdmin)

class TeamAdmin(admin.ModelAdmin):
    list_display=['teamid','teamname']
admin.site.register(Team,TeamAdmin)





# class LabtestAdmin(admin.ModelAdmin):
#     list_display=['f01','f02','f03']
# admin.site.register(Labtest,LabtestAdmin)

