# -*- coding: utf-8 -*-
# @Time : 2021/4/7 10:28
# @Author : GUOwendong
# @Email : 1965905496@qq.com
# @File : DemoServer.py
# @Software: PyCharm

from flask import Flask,session,request,Request,make_response

app = Flask(__name__)
request:Request
app.secret_key = "key"

@app.route("/request",methods=['POST','GET'])
def hello():
    query = request.args
    post = request.form
    return  f"query: {query}\n" \
            f"post: {post}"