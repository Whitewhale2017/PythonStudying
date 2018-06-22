# coding=utf-8
#
# Created on 2018/2/


# from exchangelib import DELEGATE, Account, Credentials, Configuration, NTLM, Message, Mailbox, HTMLBody
# from exchangelib.protocol import BaseProtocol, NoVerifyHTTPAdapter
import exchangelib
# 此句用来消除ssl证书错误，exchange使用自签证书需加上
BaseProtocol.HTTP_ADAPTER_CLS = NoVerifyHTTPAdapter

# 输入你的域账号如example\leo
cred = exchangelib.Credentials(r'hywingroup\gjxx', 'hywin666')

config = exchangelib.Configuration(server='https://mail.hywingroup.com', credentials=cred, auth_type=exchangelib.NTLM)
a = exchangelib.Account(
    primary_smtp_address='gjxx@hywingroup.com', config=config, autodiscover=False, access_type=exchangelib.DELEGATE
)

# 此处为用来发送html格式邮件的文件路径
# with open(r'D:\1.html') as f:
#     msg = f.read().decode('utf-8')

m = exchangelib.Message(
    account=a,
    folder=a.sent,
    subject=u'测试邮件',
    body='ceshiyoujian',
    to_recipients=[Mailbox(email_address='wangyangyang@guinianggroup.com')]
)
m.send_and_save()
