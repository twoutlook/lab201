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
     
class Labinfo(models.Model):
    f01 = models.CharField(default=".", max_length=99,verbose_name="TITLE")
    f02 = models.CharField(default=".", max_length=99,verbose_name="INFOTYPE")
    f03 = models.TextField(default=".",verbose_name="CONTENT")
    def __str__(self):
        return self.f01+" "+self.f02;
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
        
# 学生      

class Labstudent(models.Model):
    f01 = models.CharField(default=".", max_length=99,verbose_name="用户名")
    f02 = models.CharField(default=".", max_length=99,verbose_name="密码")
    f03 = models.CharField(default=".", max_length=99,verbose_name="姓名")
    f04 = models.CharField(default=".", max_length=99,verbose_name="邮箱")
    def __str__(self):
        return self.f01+" "+self.f02+" "+self.f03+" "+self.f04;
    class Meta:
        verbose_name = "学生"
        verbose_name_plural = "学生"
# 老师      
class Labteacher(models.Model):
    f01 = models.CharField(default=".", max_length=99,verbose_name="用户名")
    f02 = models.CharField(default=".", max_length=99,verbose_name="密码")
    f03 = models.CharField(default=".", max_length=99,verbose_name="姓名")
    f04 = models.CharField(default=".", max_length=99,verbose_name="邮箱")
    def __str__(self):
        return self.f01+" "+self.f02+" "+self.f03+" "+self.f04;
    class Meta:
        verbose_name = "老师"
        verbose_name_plural = "老师"

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
		
'''
		
		

