import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

host = 'smtp.gmail.com'
port = 587
username = ''
password = ''

from_user = username
to_list = [username]
msg = MIMEMultipart('alternative')
msg['Subject'] = 'About the test'
msg['From'] = from_user

plain_text = 'for test!'
html_text = '''
<html>
    <head></head>
    <body>
        <h1> This is header1</h1>
        <p>Some paragraph wanna be <strong>STRONG</strong>...</p>
        <a href='#'>Hey</a>
    </body>
</html>
'''
mime1 = MIMEText(plain_text, 'plain')
mime2 = MIMEText(html_text, 'html')
msg.attach(mime1)
msg.attach(mime2)
#print (msg.as_string())
#######################################
try:
    email_conn = smtplib.SMTP(host, port)
    email_conn.ehlo()
    email_conn.starttls()
    email_conn.login(username, password)
    email_conn.sendmail(from_user, to_list, msg.as_string())
    email_conn.quit()
    print ('\n\n<---Email Sended Successfully--->')
except smtplib.SMTPException:
    print ('SMTP error')