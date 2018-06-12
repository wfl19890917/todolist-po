# coding:utf-8
__author__ = 'Helen'
'''
description:配置全局参数
'''
import time,os

# 获取项目路径
# project_path = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)[0]), '.'))
project_path ="E:\\test\\todolist_po"
# 测试用例代码存放路径（用于构建suite,注意该文件夹下的文件都应该以test开头命名）
test_case_path = "E:\\test\\todolist_po\\TestCase"
# print u'日志路径：'+log_path
# 测试报告存储路径，并以当前时间作为报告名称前缀
report_path = "D:\\report"
report_name = report_path+'report.html'
# 设置发送测试报告的公共邮箱、用户名和密码
smtp_sever = 'smtp.qq.com'  # 邮箱SMTP服务，各大运营商的smtp服务可以在网上找，然后可以在foxmail这些工具中验正
email_name = "2855806083@qq.com"  # 发件人名称
email_password = "8191831819"  # 发件人登录密码
email_To = "1126865919@qq.com"  # 收件人