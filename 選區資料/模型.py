from django.db import models
from django.db.models.query import QuerySet
from django.db.models.aggregates import Sum

class 選區(models.Model):
	縣市 = models.CharField(max_length = 20)
	第幾區 = models.CharField(max_length = 20)
	收錄時間 = models.DateTimeField(auto_now_add = True)
	修改時間 = models.DateTimeField(auto_now = True)
	def 候選人名單(self):
		return self.投開票所.first().候選人名單()
	def 候選人票數(self):
		候選人名單=self.投開票所.first().候選人名單()
		結果=[]
		for 人 in 候選人名單:
			總票數=self.投開票所.filter(候選人__人名=人)\
				.aggregate(Sum('候選人__得票情形'))
			結果.append((人,總票數['候選人__得票情形__sum']))
		return 結果

class 投開票所(models.Model):
	選區 = models.ForeignKey(選區, related_name = '投開票所')
	鄉鎮區別 = models.CharField(max_length = 20)
	村里別 = models.CharField(max_length = 20)
	投票所別 = models.IntegerField()
	有效票數A = models.IntegerField()  # A=1+2+...+N"
	無效票數B = models.IntegerField()  # 	"
	投票數C = models.IntegerField()  # C=A+B"	"
	已領未投票數D = models.IntegerField()  # D=E-C"	"
	發出票數E = models.IntegerField()  # E=C+D"
	用餘票數F = models.IntegerField()  # 	"
	選舉人數G = models.IntegerField()  # G=E+F"	"
	發票率H = models.IntegerField()  # H=C÷G"
	收錄時間 = models.DateTimeField(auto_now_add = True)
	修改時間 = models.DateTimeField(auto_now = True)
	def 候選人名單(self):
		資料物件 =[]
		for 人 in self.候選人.values_list('人名')\
				.distinct():
			資料物件.append(人[0])
		return 資料物件

class 候選人(models.Model):
	投開票所 = models.ForeignKey(投開票所, related_name = '候選人')
	人名 = models.CharField(max_length = 100)
	得票情形 = models.IntegerField()
	收錄時間 = models.DateTimeField(auto_now_add = True)
	修改時間 = models.DateTimeField(auto_now = True)
