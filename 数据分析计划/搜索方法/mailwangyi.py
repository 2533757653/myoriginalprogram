#decoding=gbk
from email.headerregistry import ContentDispositionHeader
import smtplib
from email.mime.text import MIMEText
def youjian(res,subject='验证码',contents='<p>这是一个常规的段落</p><p><a href="https://www.baidu.com">这是一个包含链接的段落</a></p>'):
    mail_host = 'smtp.163.com'  
#163用户名
    mail_user = 'm13355340437'  

    mail_pass = 'OKCZWJWYWGCRIFGT'   

    sender = 'm13355340437@163.com'   
    receivers = [res]
    content=''''''
    for i in contents:
          content=content+f'''<p>{i}</p>'''
    message = MIMEText(content,'html','utf-8')
#邮件主题       
    message['Subject'] = subject
#发送方信息
    message['From'] = sender 
#接受方信息     
    message['To'] = receivers[0]  
    try:
        smtpObj = smtplib.SMTP() 
        smtpObj.connect(mail_host,25)
        smtpObj.login(mail_user,mail_pass) 
        smtpObj.sendmail(
            sender,receivers,message.as_string()) 
        smtpObj.quit() 
        print('success')
    except smtplib.SMTPException as e:
        print('error',e) 