# -*- coding: utf-8 -*-
#  @ Date   : 2022/4/6 16:23
#  @ Author : RichardLau_Cx
#  @ Project: Python_Web_Demo
#  @ File   : test_py.py
#  @ IDE    : PyCharm

def add_(x):
    return x + 321


class TestClass(object):
    # 测试类
    def test_add_(self):
        assert add_(199) == 521


# assert 520 == 520
