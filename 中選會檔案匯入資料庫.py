# -*- coding: utf-8 -*-

import os
import xlrd
from 選區資料.模型 import 選區
from 選區資料.模型 import 投開票所
from 選區資料.模型 import 候選人
'''
from 中選會檔案匯入資料庫 import 中選會檔案匯入資料庫
中選會檔案匯入資料庫()
'''

class 中選會檔案匯入資料庫:
	def __init__(self):
		檔案所在 = '選區資料/中選會資料'
		for 檔名 in os.listdir(檔案所在):
			if 檔名.endswith('.xls') and '2-(' in 檔名:
# 				立委-A05-2-(苗栗縣).xls
				縣市 = 檔名.split('(')[1].split(')')[0]
				表格檔 = xlrd.open_workbook('{0}/{1}'.format(檔案所在, 檔名))
				for 表格名 in 表格檔.sheet_names():
					表格 = 表格檔.sheet_by_name(表格名)
# 					print(縣市, 表格名)
					這馬選區 = 選區.objects.create(縣市 = 縣市, 第幾區 = 表格名)
# 					print(表格.row_values(0))
# 					print(表格.row_values(1))
					if 表格.row_values(1)[:3] != self.表格分類[:3]:
# 						表格.row_values(1)[-8:]!=self.表格分類[-8:]:
# 有發票率、投票率的無仝
# 						print(self.表格分類)
						raise RuntimeError('標頭毋著')
					候選人名 = []
					for 欄 in 表格.row_values(2):
						欄 = 欄.strip()
						if 欄 != '':
							候選人名.append(欄)
					鄉鎮區 = None
					for 所在 in range(3, 表格.nrows):
						逝 = 表格.row_values(所在)
# 						print(逝)
						第空欄 = 逝[0].strip()
						if 第空欄 != '':
							鄉鎮區 = 第空欄
						第一欄 = 逝[1].strip()
						if 第一欄 != '':
							村里 = 第一欄
							欄位 = []
							for 資料 in 逝[2:-1]:
								欄位.append(int(資料))
							欄位.append(逝[-1])
# 							print(鄉鎮區, 村里,)
# 							print(候選人名, 欄位)
							這馬投開票所 = 投開票所.objects.create(
								選區 = 這馬選區,
								鄉鎮區別 = 鄉鎮區,
								村里別 = 村里 ,
								投票所別 = 欄位[0],
								有效票數A = 欄位[-8],
								無效票數B = 欄位[-7],
								投票數C = 欄位[-6],
								已領未投票數D = 欄位[-5],
								發出票數E = 欄位[-4],
								用餘票數F = 欄位[-3] ,
								選舉人數G = 欄位[-2],
								發票率H = 欄位[-1],)
							if len(候選人名) != len(欄位[1:-8]):
# 								print(候選人名, 欄位[1:-8])
								raise RuntimeError('欄位毋著')
							for 人, 票 in zip(候選人名, 欄位[1:-8]):
								候選人.objects.create(
									投開票所 = 這馬投開票所,
									人名=人,
									得票情形 = 票)
	表格分類 = ['鄉(鎮、市、區)別', '村里別', '投票所別', '各候選人得票情形', '', '有效票數A\nA=1+2+...+N', '無效票數B', '投票數C\nC=A+B', '已領未投票數D\nD=E-C', '發出票數E\nE=C+D', '用餘票數F', '選舉人數G\nG=E+F', '發票率H\nH=C÷G']
if __name__ == '__main__':
	中選會檔案匯入資料庫()
