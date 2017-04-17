#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render,redirect
def index(request):
    return  render_to_response("index.html",locals())

def login(request):

    if request.method == 'POST':
        umail = request.POST.get('mail')
        upsw = request.POST.get('psw')

        if umail == 'admin' and upsw == '123':
            red = redirect('/index/')  # 登录成功，则重定向到index
            red.set_cookie('username', umail)  # 将用户名插入cookie
            return red
            # return HttpResponse("ok")
        else:
            return HttpResponse("no")
    else:
        print request.method

