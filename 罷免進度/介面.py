from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views import generic
from django.shortcuts import get_object_or_404
from django.http.response import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q
from 選區資料.模型 import 選區
from 罷免進度.模型 import 罷免
from 罷免進度.表格 import 罷免表格
from dateutil.relativedelta import relativedelta

def 看全部罷免(request):
	全部罷免 = 罷免.objects.all()
	版 = loader.get_template('罷免進度/全部罷免.html')
	文 = RequestContext(request, {
		'全部罷免': 全部罷免,
	})
	return HttpResponse(版.render(文))

def 罷免資訊(request, pk):
	罷免資訊
	選區資料 = 選區.objects.get(pk=pk)
	版 = loader.get_template('罷免進度/選區.html')
	文 = RequestContext(request, {
		'選區': 選區資料,
	})
	return HttpResponse(版.render(文))

def 改罷免(request, pk=None):
	if pk!=None:
		罷免資料=get_object_or_404(罷免, pk=pk)
	else:
		罷免資料=罷免()
		罷免資料.結束罷免時間=罷免資料.結束罷免時間+relativedelta(months=+2)
	if request.method == 'POST':  # If the form has been submitted...
		表格 = 罷免表格(request.POST, instance=罷免資料)
		if 表格.is_valid():  # All validation rules pass
			文章 = 表格.save()
			return redirect('看全部罷免')
	else:
		表格 = 罷免表格(instance=罷免資料)
	版 = loader.get_template('罷免進度/改罷免.html')
	文 = RequestContext(request, {
		'表格': 表格,
	})
	return HttpResponse(版.render(文))