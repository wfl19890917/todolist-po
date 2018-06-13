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
def send_email(new_report):
    f=open(new_report,'rb')
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
    msg_file["Content-Disposition"] = 'attachment;filename="TestReport.html"'
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
#2.定义：取最新测试报告
def get_NewReport(report_dir):
    #列举test_dir目录下的所有文件，结果以列表形式返回。
    lists=os.listdir(report_dir)
    #sort按key的关键字进行排序，lambda的入参fn为lists列表的元素，获取文件的最后修改时间
    #最后对lists元素，按文件修改时间大小从小到大排序。
    lists.sort(key=lambda fn:os.path.getmtime(report_dir+'\\'+fn))
    #获取最新文件的绝对路径
    file_path=os.path.join(report_dir,lists[-1])
#    L=file_path.split('\\')
#    file_path='\\\\'.join(L)
    return file_path


