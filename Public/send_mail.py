'''
Created on 2018年6月12日

@author: admin
'''
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import HTMLTestRunner
import os,time
def send_mail(file_new):
    f=open(file_new,'rb')
    mail_body=f.read()
    f.close()
    # 发送邮箱服务器
    serverip ='smtp.qq.com'
    serverport='465'
    # 发件人邮箱
    sender ='2855806083@qq.com'
    # 接收人邮箱
    receiver ='1126865919@qq.com'
    # 发送邮箱用户信息
    username ='2855806083@qq.com'
    # 客户端授权码
    password ='sdijonugzjnmddjd'
    #通过  模块构造的带附件的邮件如图
    msg = MIMEMultipart()
    #编写html类型的邮件正文，MIMEtext()用于定义邮件正文
    #发送正文
    text = MIMEText(mail_body, 'html', 'utf-8')
    text['Subject'] = Header('自动化测试报告', 'utf-8')
    msg.attach(text)
    #发送附件
    #Header()用于定义邮件标题
    msg['Subject'] = Header('自动化测试报告', 'utf-8')
    msg_file = MIMEText(mail_body, 'html', 'utf-8')
    msg_file['Content-Type'] = 'application/octet-stream'
    msg_file["Content-Disposition"] = 'attachment; filename="D:\\report\\report.html"'
    msg.attach(msg_file)
    msg['from'] = '2855806083@qq.com'  # 发送邮件的人
    msg['to'] = '1126865919@qq.com'
    # smtp = smtplib.SMTP('smtp.163.com', 25)  # 连接服务器
    try:
        s = smtplib.SMTP_SSL(serverip, serverport)
        s.login(username, password)
        # 这里的to_address是真正需要发送的到的mail邮箱地址需要的是一个list
        s.sendmail(msg['from'],msg['to'], msg.as_string())
        print('%s----发送邮件成功' % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    except Exception as err:
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        print(err)
def new_report(testreport):
    dirs = os.listdir(testreport)
    dirs.sort()
    newreportname = dirs[-1]
    print('The new report name: {0}'.format(newreportname))
    file_new = os.path.join(testreport, newreportname)
    return file_new


