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
from .models import Equipment
from .models import Experiment
from .models import Request
from .models import Request2

from .models import Action
from .models import AuthDevice
from .models import CurrentDevice
from .models import Board




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
    list_display=['id','userid','password','username','mailbox']
admin.site.register(Teacher,TeacherAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display=['id','userid','studentid','password','username','mailbox','teacher','team']
    # list_display=['userid','username','mailbox','teacher']
    
admin.site.register(Student,StudentAdmin)



class TeamAdmin(admin.ModelAdmin):
    list_display=['id','teamid','teamname']
admin.site.register(Team,TeamAdmin)

class EquipmentAdmin(admin.ModelAdmin):
    list_display=['id','equipid','equipname','equipnote']
admin.site.register(Equipment,EquipmentAdmin)

class ExperimentAdmin(admin.ModelAdmin):
    list_display=['id','expname','expnote','equipment']
admin.site.register(Experiment,ExperimentAdmin)

class RequestAdmin(admin.ModelAdmin):
    list_display=['id','teacher','experiment','team','rqsttime','starttime','endtime','status','remarks']
admin.site.register(Request,RequestAdmin)

class Request2Admin(admin.ModelAdmin):
    list_display=['id','student','experiment','rqsttime','starttime','endtime','status','remarks']
admin.site.register(Request2,Request2Admin)

class ActionAdmin(admin.ModelAdmin):
    # list_display=['id','request','student','apvd1','apvd2','score']
    list_display=['id','requestby','request','student','score']
    
    # list_display=['id','request','student']
    
admin.site.register(Action,ActionAdmin)


class AuthDeviceAdmin(admin.ModelAdmin):
    list_display=['id','hwnote']
admin.site.register(AuthDevice,AuthDeviceAdmin)

class CurrentDeviceAdmin(admin.ModelAdmin):
    list_display=['id','hwnote']
admin.site.register(CurrentDevice,CurrentDeviceAdmin)

class BoardAdmin(admin.ModelAdmin):
    list_display=['id','boardname','dido','addr','var1','var2','equipment']
admin.site.register(Board,BoardAdmin)



# class LabtestAdmin(admin.ModelAdmin):
#     list_display=['f01','f02','f03']
# admin.site.register(Labtest,LabtestAdmin)

