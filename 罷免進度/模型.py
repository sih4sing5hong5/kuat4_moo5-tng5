from django.db import models
from django.db.models.query import QuerySet
from django.db.models.aggregates import Sum
from 選區資料.模型 import 選區
from datetime import datetime

class 罷免(models.Model):
	選區 = models.ForeignKey(選區, related_name='罷免')
	開始罷免時間 = models.DateField(default=datetime.now)
	結束罷免時間 = models.DateField(default=datetime.now)
	有效罷免文件 = models.IntegerField(default=0)
	無效罷免文件 = models.IntegerField(default=0)
	收錄時間 = models.DateTimeField(auto_now_add=True)
	修改時間 = models.DateTimeField(auto_now=True)
	def 當選人(self):
		候選人票數 = self.選區.候選人票數()
		return self.選區.當選人(候選人票數)[0]
	def 選舉人數(self):
		return self.選區.投票數()
