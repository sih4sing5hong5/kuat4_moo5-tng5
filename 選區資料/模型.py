from django.db import models
from django.db.models.query import QuerySet

class 選區(models.Model):
	縣市 = models.CharField(max_length = 20)
	第幾區 = models.CharField(max_length = 20)
	收錄時間 = models.DateTimeField(auto_now_add = True)
	修改時間 = models.DateTimeField(auto_now = True)

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

class 候選人(models.Model):
	投開票所 = models.ForeignKey(投開票所, related_name = '候選人')
	得票情形 = models.IntegerField()
	收錄時間 = models.DateTimeField(auto_now_add = True)
	修改時間 = models.DateTimeField(auto_now = True)
