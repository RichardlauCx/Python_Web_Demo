# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


from django import forms

from .models import Topic, Entry


class Topic_Form(forms.ModelForm):
    class Meta:
        model = Topic  # 根据模型Topic创建一个表单
        fields = ['text']  # 表单所含字段：text
        labels = {'text': ''}  # Django不要为字段text生成标签


class Entry_Form(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}  # 为test字段定义了一个空标签
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}  # 修改默认HTML小部件，通过Django使用forms.Textarea，定制字段test输入小部件
