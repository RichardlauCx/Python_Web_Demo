# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


from django.http import Http404


def check_topic_owner(request, topic):
    """
    检查当前访问主题，是否为当前登录用户所属
    :param request:
    :param topic:
    :return:
    """
    if topic.owner != request.user:
        raise Http404
