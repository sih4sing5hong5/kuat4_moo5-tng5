from django.forms import ModelForm
from django.forms import Textarea
from django.forms import Select
from 罷免進度.模型 import 罷免

class 罷免表格(ModelForm):
	class Meta:
		model = 罷免
# 		fields = ['原本標題', '斷詞標題', '原本內容', '斷詞內容']
# 		widgets = {
# 			'原本內容': Textarea(attrs={'class':'文章 橫線','wrap': 'off'}),
# 			'斷詞內容': Textarea(attrs={'class':'文章 橫線','wrap': 'off'}),
# 		}

