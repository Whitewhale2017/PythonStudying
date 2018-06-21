from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders
import smtplib
import time

def send_mail(subject):
    email_host = ''  # 服务器地址
    sender = ''  # 发件人
    password = ''  # 密码，如果是授权码就填授权码
    receiver = ''  # 收件人

    msg = MIMEMultipart()
    msg['Subject'] = subject  # 标题
    msg['From'] = ''  # 发件人昵称
    msg['To'] = ''  # 收件人昵称

    signature = '''
\n\t this is auto test report!
\n\t you don't need to follow
'''
    # text = MIMEText(signature, 'plain')  # 签名
    # msg.attach(text)

    # 正文-图片 只能通过html格式来放图片，所以要注释25，26行
    mail_msg = '''
<p>\n\t this is auto test report!</p>
<p>\n\t you don't need to follow</p>
<p><a href="http://blog.csdn.net/wjoxoxoxxx">我的博客：</a></p>
<p>截图如下：</p>
<p><img src="cid:image1"></p>
'''
    msg.attach(MIMEText(mail_msg, 'html', 'utf-8'))
    # 指定图片为当前目录
    fp = open(r'111.jpg', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    # 定义图片 ID，在 HTML 文本中引用
    msgImage.add_header('Content-ID', '<image1>')
    msg.attach(msgImage)

    ctype = 'application/octet-stream'
    maintype, subtype = ctype.split('/', 1)
    # 附件-图片
    image = MIMEImage(open(r'111.jpg', 'rb').read(), _subtype=subtype)
    image.add_header('Content-Disposition', 'attachment', filename='img.jpg')
    msg.attach(image)
    # 附件-文件
    file = MIMEBase(maintype, subtype)
    file.set_payload(open(r'320k.txt', 'rb').read())
    file.add_header('Content-Disposition', 'attachment', filename='test.txt')
    encoders.encode_base64(file)
    msg.attach(file)

    # 发送
    smtp = smtplib.SMTP()
    smtp.connect(email_host, 25)
    smtp.login(sender, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print('success')


if __name_ - == '__main__':
    now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    subject = now + '自动化测试报告'
    send_mail(subject)
