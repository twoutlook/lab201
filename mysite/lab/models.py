from django.db import models

# class Item011(models.Model):
#     f01 = models.CharField(default=".", max_length=99,verbose_name="机台吨位")
#     f02 = models.CharField(default=".", max_length=99,verbose_name="生产订单号")
#     f03 = models.CharField(default=".", max_length=99,verbose_name="物料代码")        	  	        	
#     f04 = models.CharField(default=".", max_length=99,verbose_name="物料说明")
#     f05 = models.CharField(default=".", max_length=99,verbose_name="材料")
#     f06 = models.IntegerField(default=0,verbose_name="订单数量")
#     f07 = models.IntegerField(default=0,verbose_name="未生产数量")
#     f08 = models.FloatField(default=0,verbose_name="工时")
#     f09 = models.FloatField(default=0,verbose_name="生产周期")
#     f10 = models.FloatField(default=0,verbose_name="生产天数")
#     def __str__(self):
#         return self.f01+" "+self.f02+" "+self.f03+" "+str(self.f06)+" ";
class Labpower(models.Model):
    f01 = models.IntegerField(default=0,verbose_name="ZUBIE ID")
    f02 = models.CharField(default=".", max_length=99,verbose_name="ZUBIE")
    f03 = models.IntegerField(default=0,verbose_name="STATE")
    def __str__(self):
        return str(self.f01)+" "+self.f02+" "+str(self.f01)+" ";
     
     



class Info(models.Model):
    f01 = models.CharField(default=".", max_length=99,verbose_name="标题")
    f02 = models.DateTimeField(verbose_name="时间")
    f03 = models.TextField(default=".",verbose_name="内容")
    def __str__(self):
        return self.f01;
    class Meta:
        verbose_name = "信息"
        verbose_name_plural = "信息"


# 学生实验信息
class Labtest(models.Model):
    f01 = models.CharField(default=".", max_length=99,verbose_name="用户名")
    f02 = models.CharField(default=".", max_length=99,verbose_name="实验项目")
    f03 = models.CharField(default=".", max_length=99,verbose_name="申请状态")
    f04 = models.CharField(default=".", max_length=99,verbose_name="分数")
    f05 = models.CharField(default=".", max_length=99,verbose_name="申请时间")
    f06 = models.CharField(default=".", max_length=99,verbose_name="所属实验组")
    def __str__(self):
        return self.f01+" "+self.f02;
        

'''
学生只有一个指导老师，这个指导老师就是给他们上课的老师，
然后每个实验室有专门的老师，也就是说，实验室的老师是和申请的实验关联，
不同的实验，对应的实验室老师可能不一样，但是指导老师就是上课的老师就一个

用户ID
用户名
密码
姓名
邮箱
身份
指导老师
所属实验组



'''

class Student(models.Model):
    userid = models.CharField( unique=True, max_length=16,verbose_name="用户名")
    studentid = models.CharField(default=".", max_length=16,verbose_name="学号")
    username = models.CharField(default=".", max_length=16,verbose_name="姓名")
    password = models.CharField(default=".", max_length=16,verbose_name="密码")
    mailbox = models.EmailField(unique=True,max_length=99,verbose_name="邮箱")
    teacher = models.ForeignKey('Teacher',verbose_name="老師")
    # group = models.ForeignKey('Group',verbose_name="組別")
    # team = models.CharField(default=".", max_length=16,verbose_name="組別")
    # team = models.IntegerField(default=1,verbose_name="組別")
    team = models.ForeignKey('Team',verbose_name="組別")
    
    # groupname = models.CharField(default=".", max_length=16,verbose_name="組別")
    def __str__(self):
        return self.username;
    class Meta:
        verbose_name = "学生"
        verbose_name_plural = "学生"

class Teacher(models.Model):
    userid = models.CharField( unique=True, max_length=16,verbose_name="用户名")
    username = models.CharField(default=".", max_length=16,verbose_name="姓名")
    password = models.CharField(default=".", max_length=16,verbose_name="密码")
    mailbox = models.EmailField(unique=True,max_length=99,verbose_name="邮箱")
  
    
    def __str__(self):
        return self.username;
    class Meta:
        verbose_name = "老师"
        verbose_name_plural = "老师"
'''
实验设备		
字段名称	数据类型	值
设备ID	数字	
设备名称	文本	
变量地址	文本	
'''
class Equipment(models.Model):
    equipid = models.CharField( unique=True, max_length=16,verbose_name="设备ID")
    equipname = models.CharField(unique=True,default=".", max_length=96,verbose_name="设备名称")
    equipnote = models.CharField(default=".", max_length=96,verbose_name="变量地址")
  
    
    def __str__(self):
        return self.equipname;
    class Meta:
        verbose_name = "实验设备"
        verbose_name_plural = "实验设备"
'''
实验项目		
字段名称	数据类型	值
实验名称	文本	
实验内容	文本	
设备ID	数字	
experiment
'''
class Experiment(models.Model):
    # expid = models.CharField( unique=True, max_length=16,verbose_name="设备ID")
    expname = models.CharField(default=".", max_length=96,verbose_name="实验名称")
    expnote = models.CharField(default=".", max_length=96,verbose_name="实验内容")
    equipment = models.ForeignKey('Equipment',verbose_name="设备名称")
   
    
    def __str__(self):
        return self.expname;
    class Meta:
        verbose_name = "实验项目"
        verbose_name_plural = "实验项目"

'''
实验申请信息		
字段名称	数据类型	值
实验申请ID	数字	（按顺序递加）
用户名	文本	
实验项目ID	数字	
申请状态	文本	申请、审核、实施，完成
申请时间	时间	
实验開始时间	时间	
实验結束时间	时间	
所属实验组	文本	“学生”的申请，此项无效
备注		
'''
class Request(models.Model):
    # expid = models.CharField( unique=True, max_length=16,verbose_name="设备ID")
    teacher = models.ForeignKey('Teacher',verbose_name="用户")
    experiment = models.ForeignKey('Experiment',verbose_name="实验项目")
    
    # team = models.IntegerField(default=1,verbose_name="组别")
    team = models.ForeignKey('Team',verbose_name="组别")
    
    rqsttime = models.DateField(auto_now_add=True,verbose_name="申请时间")
    starttime = models.DateTimeField(null=True,verbose_name="start时间")
    endtime = models.DateTimeField(null=True,verbose_name="end时间")
    
    # expnote = models.CharField(default=".", max_length=96,verbose_name="实验内容")
    # equipment = models.ForeignKey('Equipment',verbose_name="设备名称")
    CHOICE_STATUS = (
        ('申请','申请'),
        ('审核','审核'),
        ('实施','实施'),
        ('完成','完成'),
    )
       
    status = models.CharField(default="申请",max_length=16,verbose_name="申请状态", choices=CHOICE_STATUS)
    remarks = models.CharField(default=".", max_length=250,verbose_name="备注")
    
    def __str__(self):
        return str(self.id);
    class Meta:
        verbose_name = "实验申请信息(老师)"
        verbose_name_plural = "实验申请信息(老师)"

class Request2(models.Model):
    # expid = models.CharField( unique=True, max_length=16,verbose_name="设备ID")
    student = models.ForeignKey('Student',verbose_name="用户")
    experiment = models.ForeignKey('Experiment',verbose_name="实验项目")
    
    # team = models.IntegerField(default=1,verbose_name="组别")
    # team = models.ForeignKey('Team',verbose_name="组别")
    
    rqsttime = models.DateField(auto_now_add=True,verbose_name="申请时间")
    starttime = models.DateTimeField(null=True,verbose_name="start时间")
    endtime = models.DateTimeField(null=True,verbose_name="end时间")
    
    # expnote = models.CharField(default=".", max_length=96,verbose_name="实验内容")
    # equipment = models.ForeignKey('Equipment',verbose_name="设备名称")
    # 核准
    # 恩，可以，就是审批状态里面“指导老师核可”改成“核准”
    CHOICE_STATUS = (
        ('申请','申请'),
        # ('指导老师核可','指导老师核可'),
        ('核准','核准'),
        
        ('审核','审核'),
        ('实施','实施'),
        ('完成','完成'),
    )
       
    status = models.CharField(default="申请",max_length=16,verbose_name="申请状态", choices=CHOICE_STATUS)
    remarks = models.CharField(default=".", max_length=250,verbose_name="备注")
    
    def __str__(self):
        return str(self.id);
    class Meta:
        verbose_name = "实验申请信息(学生)"
        verbose_name_plural = "实验申请信息(学生)"

'''
学生实验课程		
字段名称	数据类型	值
实验申请ID	数字	
用户名	文本	
分数	数字	
'''
class Action(models.Model):
    # expid = models.CharField( unique=True, max_length=16,verbose_name="设备ID")
    CHOICE_BY = (
        ('老师','老师'),
        ('学生','学生'),
    )
    requestby = models.CharField(default="老师",max_length=16,verbose_name="申请類型", choices=CHOICE_BY)
    request = models.ForeignKey('Request',verbose_name="实验申请信息")
    student = models.ForeignKey('Student',verbose_name="学生")
    # CHOICE_STATUS = (
    #     ('未审核','未审核'),
    #     ('已审核','已审核'),
    # )
    # # byteacherent = models.ForeignKey('Student',verbose_name="用户名")
    # apvd1 = models.CharField(default="未审核",max_length=99,verbose_name="审核1", choices=CHOICE_STATUS)
    # apvd2 = models.CharField(default="未审核",max_length=99,verbose_name="审核2", choices=CHOICE_STATUS)
   
    # http://stackoverflow.com/questions/16527308/how-to-set-null-for-integerfield-instead-of-setting-0
    score = models.IntegerField(default=-1, verbose_name="分数")
    # team = models.ForeignKey('Team',verbose_name="组别")
        
    def __str__(self):
        return str(self.id);
    class Meta:
        verbose_name = "学生实验课程"
        verbose_name_plural = "学生实验课程"



# class Group(models.Model):
#     groupid = models.CharField(unique=True, default=".", max_length=16,verbose_name="組別編號")
#     groupname = models.CharField(unique=True,default=".", max_length=16,verbose_name="組別名稱")
    
#     def __str__(self):
#         return self.groupname;
#     class Meta:
#         verbose_name = "組別"
#         verbose_name_plural = "組別"
        
class Team(models.Model):
    teamid = models.IntegerField(unique=True, default=1,verbose_name="組別編號")
    teamname = models.CharField(unique=True,default=".", max_length=16,verbose_name="組別名稱")
    
    def __str__(self):
        return self.teamname;
    class Meta:
        verbose_name = "組別"
        verbose_name_plural = "組別"


class PrjSpec(models.Model):
    f00 = models.CharField(default=".", max_length=99,verbose_name="編號")
    f01 = models.CharField(default=".", max_length=200,verbose_name="主題")
    f02 = models.CharField(default=".", max_length=2000,verbose_name="說明")

    def __str__(self):
        return self.f01+" "+self.f02;
    class Meta:
        verbose_name = "項目需求說明"
        verbose_name_plural = "項目需求說明"
        # app_label = u"項目"


        
'''        
实验设备		
字段名称	数据类型	值
设备ID	数字	
设备名称	文本	
变量地址	文本	
		
		
板卡信息		
字段名称	数据类型	值
ID	数字	
类型	文本	DI/DO
变量地址	文本	
变量值	数字	0/1
通讯状态	数字	0/1
设备ID	数字	
		
		实验项目		
字段名称	数据类型	值
实验项目ID	数字	
实验名称	文本	
实验内容	文本	
设备ID	数字	
指导老师	文本	
实验状态	文本	申请、审核、实施，完成
申请时间	时间	
实验时间	时间	


授权设备		
字段名称	数据类型	值
ID	数字	（按顺序递加）
硬件序列号	文本	
	
	
	
	
授权设备		
字段名称	数据类型	值
ID	数字	（按顺序递加）
硬件序列号	文本	
		
'''
class AuthDevice(models.Model):
    # H/W Note
    hwnote = models.CharField(unique=True,default=".", max_length=99,verbose_name="硬件序列号")
    
    def __str__(self):
        return self.hwnote;
    class Meta:
        verbose_name = "授权设备"
        verbose_name_plural = "授权设备"
        # app_label = 'myapp'
		
class CurrentDevice(models.Model):
    # H/W Note
    hwnote = models.CharField(unique=True,default=".", max_length=99,verbose_name="硬件序列号")
    
    def __str__(self):
        return self.hwnote;
    class Meta:
        verbose_name = "当前设备"
        verbose_name_plural = "当前设备"
        # app_label = 'myapp'
'''	
板卡信息		
字段名称	数据类型	值
ID	数字	
类型	文本	DI/DO
变量地址	文本	
变量值	数字	0/1
通讯状态	数字	0/1
设备ID	数字
'''	
class Board(models.Model):
    # expid = models.CharField( unique=True, max_length=16,verbose_name="设备ID")
    # expname = models.CharField(default=".", max_length=96,verbose_name="实验名称")
    # expnote = models.CharField(default=".", max_length=96,verbose_name="实验内容")
    # 板卡名称
    boardname = models.CharField(default=".", max_length=96,verbose_name="板卡名称")
    CHOICE_DIDO = (
        ('DI','DI'),
        ('DO','DO'),
    )
    dido = models.CharField(default="DI",max_length=16,verbose_name="类型", choices=CHOICE_DIDO)
    addr = models.CharField(default=".", max_length=96,verbose_name="变量地址")
  
    CHOICE_01 = (
        (0,0),
        (1,1),
    )
    var1 = models.IntegerField(default=0, verbose_name="变量值", choices=CHOICE_01)
    var2 = models.IntegerField(default=0, verbose_name="通讯状态", choices=CHOICE_01)
    equipment = models.ForeignKey('Equipment',verbose_name="设备名称")
    
    def __str__(self):
        return str(self.id);
    class Meta:
        verbose_name = "板卡信息"
        verbose_name_plural = "板卡信息"

