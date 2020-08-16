# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm

from django.urls import path
# from educoderapp import views
from . import views  # 上面的优化版（. 表示从当前文件夹导入）


app_name = 'educoder_app'  # 命名空间

urlpatterns = [
    path(r'', views.hello),
    path(r'index/', views.index, name='index'),  # 第一个参数为route地址（人为起名）
    path(r'create/', views.create),
    path(r'create/create_p/', views.create_p),
    path(r'delete<int:ID>/', views.delete),  # 范式表明传参类型，后面承接参数（Web界面当中会显示出来）
    path(r'edit_d<int:ID>/', views.edit_d),
    path(r'edit_s<int:ID>/', views.edit_s),
]
