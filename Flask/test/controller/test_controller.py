# -*- coding: utf-8 -*-
#  @ Date   : 2022/4/6 17:31
#  @ Author : RichardLau_Cx
#  @ Project: Python_Web_Demo
#  @ File   : test_controller.py
#  @ IDE    : PyCharm


import json
import datetime
from flask import Blueprint, request


testModule = Blueprint('testModule', __name__)


# 1. GET请求，不带参数
# URL: http://127.0.0.1:8088/testModule/get_test1
@testModule.route("/get_test1", methods=["GET"])
def get_test1():
    return_dict = {
        'return_code': '200',
        'return_info': '处理成功',
        'result': None
    }

    return json.dumps(return_dict, ensure_ascii=False)


# 2. GET请求，带参数
# URL: http://127.0.0.1:8088/testModule/get_test2?name=Mark&version=88
@testModule.route("/get_test2", methods=["GET"])
def get_test2():
    return_dic = {
        'return_code': '200',
        'return_info': '处理成功',
        'result': None
    }

    # 判断请求参数的情况
    if len(request.args) == 0:
        # print("requests.args: " + str(request.args))
        return_dic['return_code'] = '5004'
        return_dic['return_info'] = '请求参数为空'

        return json.dumps(return_dic, ensure_ascii=False)

    get_data = request.args.to_dict()
    name = get_data.get('name')
    age = get_data.get('version')
    return_dic['result'] = "%s目前是第%s代：%s" % (name, age, datetime.datetime.now())

    return json.dumps(return_dic, ensure_ascii=False)


# 3. POST请求，带参数
# URL: http://127.0.0.1:8088/testModule/post_test1
@testModule.route("/post_test1", methods=["POST"])
def post_test1():
    return_dic = {
        'return_code': '200',
        'return_info': '处理成功',
        'result': None
    }

    if len(request.get_data()) == 0:
        return_dic['return_code'] = '5004'
        return_dic['return_info'] = '请求参数为空'

        return json.dumps(return_dic, ensure_ascii=False)

    name = request.values.get('name')
    version = request.values.get('version')

    return_dic['result'] = "%s目前是第%s代：%s" % (name, version, datetime.datetime.now())

    print("return_dic: " + str(return_dic))
    return json.dumps(return_dic, ensure_ascii=False)