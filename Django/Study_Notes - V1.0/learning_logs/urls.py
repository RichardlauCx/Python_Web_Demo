# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm

"""定义learning_logs的URL模式"""  # 文档字符串

from django.conf.urls import url
from django.urls import path, re_path
from . import views

app_name = 'learning_logs'  # 应用命名空间

urlpatterns = [
    # 网址样式

    # 主页
    re_path(r'^$', views.index, name='index'),

    # 显示所有主题
    # re_path(r'^topics/$', views.topics, name='topics')
    path(r'topics/', views.topics, name='topics'),
    re_path(r'^topic/(?P<topic_id>\d+)/$', views.topic, name='topic'),  # 其中的正则相当于分组捕获，将值存至topic_id中
    re_path(r'^new_topic/$', views.new_topic, name='new_topic'),  # 用于添加新主题的网页
    re_path(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    re_path(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]
