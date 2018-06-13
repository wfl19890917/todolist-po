# coding:utf-8
__author__ = 'Helen'
'''
description:配置全局参数
'''
import time,os
report_dir="E:\\test\\todolist_po\\Result\\"
#获取系统当前时间
now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
#定义单个测试报告的存放路径，支持相对路径
tdresult = report_dir + day
#os.mkdir(tdresult)
filename = tdresult + "\\" + now + "_result.html"
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