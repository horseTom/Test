import smtplib
from email.mime.text import MIMEText
from email.header import Header

smtpserver = 'smtp.gmail.com'
smtport = 587
user = 'chigwone@gmail.com'
password = '!top123456'

sender = 'chigwone@gmail.com'
receiver = 'zrguo@topxgun.com'

subject = 'Python send email test!'

msg = MIMEText('<html><h1>Hello!</h1><h2>Hello!</h2></html>','html','utf-8')
msg['Subject'] = Header(subject,'utf-8')

smtp = smtplib.SMTP(smtpserver, smtport)
# smtp.connect(smtpserver, smtport)
smtp.ehlo()
smtp.starttls()
smtp.login(user,password)
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()
