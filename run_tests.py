# -*- coding:utf-8 -*-

import time
import sys
import os
from HTMLTestRunner import HTMLTestRunner
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import unittest

sys.path.append("./interface")
# 指定测试用例为当前文件夹下的interface目录


def send_mail(file_new):
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    smtpserver = 'smtp.exmail.qq.com'
    user = 'qujinliang@uknower.com'
    password = '5H84rhfYaXsLEFyP'
    sender = 'qujinliang@uknower.com'
    receiver = ['qujinliang@uknower.com','liupingjun@uknower.com','kai.wang@huilianyi.com','yueyue.chen@huilianyi.com']
    subject = '各省发票查验接口监控报告'
    msg = MIMEMultipart('mixed')
    msg_html1 = MIMEText(mail_body, 'html', 'utf-8')
    msg.attach(msg_html1)

    msg_html = MIMEText(mail_body, 'html', 'utf-8')
    msg_html["Content-Disposition"] = 'attachment; filename = "TestReport.html"'
    msg.attach(msg_html)

    msg['From'] = 'qujinliang@uknower.com <qujinliang@uknower.com>'
    msg['To'] = ";".join(receiver)
    msg['Subject'] = Header(subject,'utf-8')



    smtp = smtplib.SMTP_SSL()
    smtp.connect(smtpserver,'465')
    smtp.login(user, password)
    smtp.sendmail(sender, receiver, msg.as_string())

    smtp.quit()
    print('email has send out !')


def new_file(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getatime(testreport + "/" + fn))
    file_new = os.path.join(testreport, lists[-1])
    print(file_new)
    return file_new

if __name__ == '__main__':
    print('======AutoTest Start======')


    test_dir = "./interface"
    test_report_dir =  "./report"
    # discover = unittest.defaultTestLoader.discover(test_dir, pattern='xdj_invoice_interface_test.py')
    discover = unittest.defaultTestLoader.discover(test_dir, pattern="*_test.py")
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = test_report_dir + "//" + now + 'EKP_project.html'

    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='发票查验接口监控邮件',
                                           description='详情请下载附件查看：')
    runner.run(discover)
    fp.close()

    new_report = new_file(test_report_dir)

    send_mail(new_report)
    print('=======AutoTest Over======')