import datetime
import shutil
import os
import logging
import logging.config
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import parseaddr, formataddr
from openpyxl import load_workbook

EMAIL_HOST = 'outlook.office365.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'yanchu1990@hotmail.com'
EMAIL_HOST_PASSWORD = 'Ilove199011'


def send_stub():
      try:
        server = smtplib.SMTP_SSL(EMAIL_HOST, EMAIL_PORT)  # 配置邮件服务器信息
        server.ehlo()
        server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
        try:
            html_message = 'ceshi'
            receiver = 'wangyangyang@guinianggroup.com'
            print(html_message)
            print(receiver)
            msg = MIMEMultipart()
            msg['Subject'] = 'CESHI'
            msg['To'] = receiver
            msg_text = MIMEText('CESHI001', 'html', 'utf-8')
            msg.attach(msg_text)
            server.sendmail(EMAIL_HOST_USER, receiver, msg.as_string())
            print('发送成功')
        except Exception as e:
            print(e)
            print('发送失败')
        finally:
            try:
                if server:
                    server.quit()
            except Exception as e1:
                print(e1)