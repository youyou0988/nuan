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
        sendEmail('warmframe@aliyun.com', 'mkt@warmframe.com', title, content)
    #     send_mail(title, content, 'web@warmframe.com',
    # ['542413313@qq.com'], fail_silently=False)
    return render(req, 'register.html', locals())

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import smtplib
from nuan.settings import *
def sendEmail(fromAdd, toAdd, subject, plainText):

        strFrom = fromAdd
        strTo =toAdd

        # 设定root信息
        msgRoot = MIMEMultipart('related')
        msgRoot['Subject'] = subject
        msgRoot['From'] = strFrom
        msgRoot['To'] = ','.join(toAdd) #与原文不同
        msgRoot.preamble = 'This is a multi-part message in MIME format.'

        # Encapsulate the plain and HTML versions of the message body in an
        # 'alternative' part, so message agents can decide which they want to display.
        msgAlternative = MIMEMultipart('alternative')
        msgRoot.attach(msgAlternative)

        #设定纯文本信息
        msgText = MIMEText(plainText, 'plain', 'utf-8')
        msgAlternative.attach(msgText)


       #发送邮件
        smtp = smtplib.SMTP()
       #设定调试级别，依情况而定
        smtp.set_debuglevel(1)
        smtp.connect(EMAIL_HOST)
        smtp.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
        smtp.sendmail(strFrom, strTo, msgRoot.as_string())
        smtp.quit()
