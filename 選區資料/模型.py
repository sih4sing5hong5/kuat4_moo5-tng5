from django.db import models
from django.db.models.query import QuerySet
from django.db.models.aggregates import Sum

def 加綜合資訊(陣列, 資料, 全部):
	新資料 = tuple(資料) + (資料[-1] * 100.0 / 全部,)
	陣列.append(新資料)

class 選區(models.Model):
	縣市 = models.CharField(max_length=20)
	第幾區 = models.CharField(max_length=20)
	收錄時間 = models.DateTimeField(auto_now_add=True)
	修改時間 = models.DateTimeField(auto_now=True)
	def 候選人名單(self):
		return self.投開票所.first().候選人名單()
	def 候選人票數(self):
		候選人名單 = self.投開票所.first().候選人名單()
		結果 = []
		for 人 in 候選人名單:
			總票數 = self.投開票所.filter(候選人__人名=人)\
				.aggregate(Sum('候選人__得票情形'))
			結果.append((人, 總票數['候選人__得票情形__sum']))
		return 結果
	def 綜合資訊(self):
		資訊 = []
		候選人票數 = self.候選人票數()
		選區總票數 = self.選區總票數()
		當選人 = self.當選人(候選人票數)
		加綜合資訊(資訊, 當選人, 選區總票數)
		第二高票 = self.第二高票(候選人票數)
		加綜合資訊(資訊, 第二高票, 選區總票數)
		第二高票差 = ('前兩高票差', 當選人[1] - 第二高票[1])
		加綜合資訊(資訊, 第二高票差, 選區總票數)
		投票數 = self.投票數()
		非當選人票 = ('在野陣營', 投票數 - 當選人[1])
		加綜合資訊(資訊, 非當選人票, 選區總票數)
		非當選人票差 = ['在野陣營差當選人', 當選人[1] - 非當選人票[1]]
		加綜合資訊(資訊, 非當選人票差, 選區總票數)
		加綜合資訊(資訊, ('投票數', 投票數,), 選區總票數)
		加綜合資訊(資訊, ('選民數', 選區總票數), 選區總票數)
		print(資訊)
# 		加綜合資訊(資訊,候選人票數)
		return 資訊
	def 當選人(self, 候選人票數):
		return sorted(候選人票數, key=lambda 資:-資[1])[0]
	def 當選人名(self):
		候選人票數 = self.候選人票數()
		return self.當選人(候選人票數)[0].split('\n',1)[1]
	def 第二高票(self, 候選人票數):
		return sorted(候選人票數, key=lambda 資:-資[1])[1]
	def 投票數(self):
		return self.投開票所.aggregate(Sum('投票數C'))['投票數C__sum']
	def 選區總票數(self):
		return self.投開票所.aggregate(Sum('選舉人數G'))['選舉人數G__sum']
	def __str__(self):
		return self.當選人名() + ' ' + self.縣市 + ' ' + self.第幾區

class 投開票所(models.Model):
	選區 = models.ForeignKey(選區, related_name='投開票所')
	鄉鎮區別 = models.CharField(max_length=20)
	村里別 = models.CharField(max_length=20)
	投票所別 = models.IntegerField()
	有效票數A = models.IntegerField()  # A=1+2+...+N"
	無效票數B = models.IntegerField()  # 	"
	投票數C = models.IntegerField()  # C=A+B"	"
	已領未投票數D = models.IntegerField()  # D=E-C"	"
	發出票數E = models.IntegerField()  # E=C+D"
	用餘票數F = models.IntegerField()  # 	"
	選舉人數G = models.IntegerField()  # G=E+F"	"
	發票率H = models.IntegerField()  # H=C÷G"
	收錄時間 = models.DateTimeField(auto_now_add=True)
	修改時間 = models.DateTimeField(auto_now=True)
	def 候選人名單(self):
		資料物件 = []
		for 人 in self.候選人.values_list('人名')\
				.distinct():
			資料物件.append(人[0])
		return sorted(資料物件)

class 候選人(models.Model):
	投開票所 = models.ForeignKey(投開票所, related_name='候選人')
	人名 = models.CharField(max_length=100)
	得票情形 = models.IntegerField()
	收錄時間 = models.DateTimeField(auto_now_add=True)
	修改時間 = models.DateTimeField(auto_now=True)
