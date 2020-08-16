# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm

"""定义urls的URL模式"""  # 文档字符串

from django.urls import path, re_path
from django.contrib.auth.views import LoginView
from . import views

app_name = 'users'

urlpatterns = [
    # 登陆页面
    # re_path(r'^login/$', login, {'template_name': 'users/login.html'}, name='login'),  # 1.0 版本表示
    re_path(r'^login/$', LoginView.as_view(template_name='users/login.html'), name='login'),  # 2.0 版本表示

    # 注销页面
    re_path(r'^logout/$', views.logout_view, name='logout'),

    # 注册页面
    re_path(r'^register/$', views.register, name='register'),
]
