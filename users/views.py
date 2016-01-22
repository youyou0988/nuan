# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail


def index(req):
    return render(req, 'front.html', locals())


def privacy(req):
    type = 'privacy'
    current = '隐私声明'
    return render(req, 'condition.html', locals())


def condition(req):
    type = 'condition'
    current = '使用条件'
    return render(req, 'condition.html', locals())


@csrf_exempt
def register(req):
    if req.method == 'POST':
        content = ''
        for key in req.POST:
            content += key + req.POST.get(key, None)
        success_msg = '注册成功'
        # print str(content)
    #     send_mail('暖框用户注册信息', content, '542413313@qq.com',
    # ['yu_yang8909@163.com'], fail_silently=False)
    return render(req, 'register.html', locals())
