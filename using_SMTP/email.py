import smtplib

host = 'smtp.gmail.com'
port = 587
username = ''
password = ''

from_user = username
to_list = [username, username]

email_conn = smtplib.SMTP(host, port)
email_conn.ehlo()
email_conn.starttls()
email_conn.login(username, password)
email_conn.sendmail(from_user, tolist, 'hello stmp <3')
#email_conn.quit()
