# coding:utf-8
__author__ = 'Helen'
'''
description:邮件发送最新的测试报告
'''
import smtplib
import os
import time
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
def sendEmail(content, title, from_name, from_address, to_address, serverport, serverip, username, password):
    msg = MIMEMultipart()
    text = MIMEText(content, _subtype='html', _charset='utf-8')
    text['Subject'] = Header(title, 'utf-8')
    msg.attach(text)
    msg['Subject'] = Header('自动化测试报告', 'utf-8')
    msg_file = MIMEText(content, _subtype='html', _charset='utf-8')
    msg_file['Content-Type'] = 'application/octet-stream'
    msg_file["Content-Disposition"] = 'attachment; filename="D:\\report\\report.html"'
    msg.attach(msg_file)
    # 这里的to_address只用于显示，必须是一个string
    msg['To'] = '1126865919@qq.com'
    msg['From'] = '2855806083@qq.com'
    try:
        s = smtplib.SMTP_SSL(serverip, serverport)
        s.login(username, password)
        # 这里的to_address是真正需要发送的到的mail邮箱地址需要的是一个list
        s.sendmail(from_address, to_address, msg.as_string())
        print('%s----发送邮件成功' % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    except Exception as err:
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        print(err)
#HEFEN_D = pth.abspath(pth.dirname(__file__))
def new_report(testreport):
    dirs = os.listdir(testreport)
    dirs.sort()
    newreportname = dirs[-1]
    print('The new report name: {0}'.format(newreportname))
    file_new = os.path.join(testreport, newreportname)
    return file_new
def send_report():
    TO = ['1126865919@qq.com']
    config = {
        "from":"2855806083@qq.com",
        "from_name":'自动化测试unittest测试框架报告:', 
        "to": TO,
        "serverip":"smtp.qq.com",
        "serverport":"465",
        "username":"2855806083@qq.com",
        "password":"sdijonugzjnmddjd"  # QQ邮箱的SMTP授权码
    }
    title = "自动化测试unittest测试框架报告"
    f = open("D:\\report\\report.html", 'rb')
    mail_body = f.read()
    f.close()
    sendEmail(mail_body, title, config['from_name'], config['from'], config['to'], config['serverport'], config['serverip'],
              config['username'], config['password'])

#main2()