# -*- coding: utf-8 -*-
from django.contrib import admin
from 選區資料.模型 import 候選人
from 選區資料.模型 import 投開票所
from 選區資料.模型 import 選區
admin.site.register(選區)
admin.site.register(投開票所)
admin.site.register(候選人)