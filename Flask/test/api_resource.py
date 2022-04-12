# -*- coding: utf-8 -*-
#  @ Date   : 2022/4/7 15:08
#  @ Author : RichardLau_Cx
#  @ Project: Python_Web_Demo
#  @ File   : api_resource.py
#  @ IDE    : PyCharm

from flask import Flask
from flask_restful import Resource, reqparse, Api


class MyApi(Resource):
    def __init__(self):
        # 接口参数
        self.parser = reqparse.RequestParser(bundle_errors=True)

        # json格式的参数，可以设置type=dict，直接解析为dict
        # json里嵌套json也同样适用
        self.parser.add_argument('para1', location=['json', 'args'], type=dict, trim=True, required=False)

        # json数组，需要设置action='append'，否则只会捕获到一个json
        self.parser.add_argument('para2', location=['json', 'args'], type=dict, trim=True, required=False,
                                 action='append')

        # 但，如果是json里面嵌套json数组，则不需要设置action='append'

        self.parser.add_argument('para3', location=['json', 'args'], type=str, trim=True, required=True)
        self.parser.add_argument('para4', location=['json', 'args'], type=int, required=True)

        self.args = self.parser.parse_args()

        super(MyApi, self).__init__()

    def post(self):
        p1 = self.args['para1']
        p2 = self.args['para2']
        p3 = self.args['para3']
        p4 = self.args['para4']

        print("p1: {}\n p2: {}\n p3: {}\n p4: {}".format(p1, p2, p3, p4))

        ret = {
            "message": "success",
            "status": 1,
            "data": [1, 2, 3]
        }

        return ret

    # def get(self):
    #     p1 = self.args['para1']
    #     p2 = self.args['para2']
    #     p3 = self.args['para3']
    #     p4 = self.args['para4']
    #
    #     ret = {"message": "success", "status": 1, "data": [1, 2, 3]}
    #
    #     return ret


if __name__ == '__main__':
    app = Flask(__name__)
    app.debug = True
    api = Api(app, catch_all_404s=True)
    api.add_resource(MyApi, '/api/test/', endpoint='my_api')
    app.run(host='0.0.0.0')
