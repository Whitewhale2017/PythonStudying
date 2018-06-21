# coding=utf-8
#
# Created on 2018/2/


from exchangelib import DELEGATE, Account, Credentials, Configuration, NTLM, Message, Mailbox, HTMLBody
from exchangelib.protocol import BaseProtocol, NoVerifyHTTPAdapter


#此句用来消除ssl证书错误，exchange使用自签证书需加上
BaseProtocol.HTTP_ADAPTER_CLS = NoVerifyHTTPAdapter


# 输入你的域账号如example\leo
cred = Credentials(r'EXAMPLE\leo', '输入你的密码')

config = Configuration(server='输入邮箱服务器网页地址', credentials=cred, auth_type=NTLM)
a = Account(
    primary_smtp_address='输入你要绑定的邮箱名（leo@example.com)', config=config, autodiscover=False, access_type=DELEGATE
)

# 此处为用来发送html格式邮件的文件路径
with open(r'C:\Users\leo\Desktop\1.html') as f:
    msg = f.read().decode('utf-8')

m = Message(
    account=a,
    folder=a.sent,
    subject=u'测试邮件',
    body=HTMLBody(msg),
    to_recipients=[Mailbox(email_address='输入你要绑定的邮箱名（leo@example.com)')]
)
m.send_and_save()