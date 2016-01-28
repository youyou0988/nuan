# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail


def index(req):
    if req.REQUEST.get('lag', None) and req.REQUEST['lag'] == 'en':
        lan_type = 'en'
    else:
        lan_type = 'ch'
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
        work = req.POST.get('input', None)
        content = ''
        for key in req.POST:
            content += key + req.POST.get(key, None)
        success_msg = '注册成功'
        # print str(content)
        if work:
            title = u'客户公司 '+str(work)+u' - 客户查询'
        else:
            title = '客户查询'
        send_mail(title, content, 'web@warmframe.com',
    ['542413313@qq.com'], fail_silently=False)
    return render(req, 'register.html', locals())
