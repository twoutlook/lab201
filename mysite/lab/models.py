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
class Power(models.Model):
    f01 = models.IntegerField(default=0,verbose_name="ZUBIE ID")
    f02 = models.CharField(default=".", max_length=99,verbose_name="ZUBIE")
    f03 = models.IntegerField(default=0,verbose_name="STATE")
    def __str__(self):
        return str(self.f01)+" "+self.f02+" "+str(self.f01)+" ";
     
