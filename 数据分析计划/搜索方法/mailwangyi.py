#decoding=gbk
from email.headerregistry import ContentDispositionHeader
import smtplib
from email.mime.text import MIMEText
def youjian(res,subject='��֤��',contents='<p>����һ������Ķ���</p><p><a href="https://www.baidu.com">����һ���������ӵĶ���</a></p>'):
    mail_host = 'smtp.163.com'  
#163�û���
    mail_user = 'm13355340437'  

    mail_pass = 'OKCZWJWYWGCRIFGT'   

    sender = 'm13355340437@163.com'   
    receivers = [res]
    content=''''''
    for i in contents:
          content=content+f'''<p>{i}</p>'''
    message = MIMEText(content,'html','utf-8')
#�ʼ�����       
    message['Subject'] = subject
#���ͷ���Ϣ
    message['From'] = sender 
#���ܷ���Ϣ     
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