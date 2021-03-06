# -*- coding: utf-8 -*-
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
import json

def 看全部選區(request):
	全部選區 = 選區.objects.all()
	版 = loader.get_template('選區資料/全部選區.html')
	文 = RequestContext(request, {
		'全部選區': 全部選區,
	})
	return HttpResponse(版.render(文))

def 看選區json(request):
	全部選區 = 選區.objects.all()
	資料=[]
	for 一个選區 in 全部選區:
		資料.append((一个選區.縣市,一个選區.第幾區,一个選區.選區總票數()))
# 	return HttpResponse(json.dumps(資料)+'\n'+str(資料))
	return HttpResponse(str(資料))

def 看選區(request,pk):
	選區資料 = 選區.objects.get(pk=pk)
	版 = loader.get_template('選區資料/選區.html')
	文 = RequestContext(request, {
		'選區': 選區資料,
	})
	return HttpResponse(版.render(文))