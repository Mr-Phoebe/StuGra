#coding: utf-8
from django.shortcuts import render

# 页面跳转至teacher.html

#num1 = 55
#num2 = 88
#num3 = 199
#arr1 = [65,59,90,81,56]

keys = {'n1':55,'n2':88,'n3':199,'n4':33,'n5':27}

def grade_home(req):
	return render(req,'chart.html',{'keys':keys})

# Create your views here.
