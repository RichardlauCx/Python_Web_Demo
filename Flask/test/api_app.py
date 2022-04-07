# -*- coding: utf-8 -*-
#  @ Date   : 2022/4/6 17:32
#  @ Author : RichardLau_Cx
#  @ Project: Python_Web_Demo
#  @ File   : api_app.py
#  @ IDE    : PyCharm


from flask import Flask
from controller.test_controller import testModule


app = Flask(__name__)
app.register_blueprint(testModule, url_prefix='/testModule')
app.debug = True


@app.route('/')
def hello_world():
    return 'flask_test is running!!'


if __name__ == '__main__':
    app.run(port=8088)
    # print("testModule: " + str(testModule))

