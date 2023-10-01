'''import smtplib

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()

server.login("srinudarpally@gmail.com","@srinu...123#")
msg = "Hello world how are you!"

server.sendmail("srinudarpally@gmail.com","cnu444345@gmail.com",msg)
print('emailsent')
server.quit()
''
import smtplib

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()

server.login('srinudarpally@gmail.com','@srinu...123#')
msg = 'Anna this message sent from by writing python program'

server.sendmail('srinudarpally@gmail.com','balachandhar787@gmail.com',msg)
print('sentemil')
server.quit()'''

import smtplib
from email.mime.text import MIMEText

title = 'My title'
msg_content = '<h2>(title) > <font color = "green"> OK </font></h2>\n'.format(title=title)
message = MIMEText(msg_content,'html')

message['From'] = 'srinudarpally@gmail.com'
message['To']   = 'cnu444345@gmail.com'
message['Cc']   = 'balachandhar787@gmail.com'
message['Subject'] = 'This is a test....hello world how are you'

msg_full = message.as_string()

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login('srinudarpally@gmail.com','@srinu...123#')
server.sendmail('srinudarpally@gmail.com',['cnu444345@gmail.com','balachandhar787@gmail.com'],msg_full)
print('sendemail')
server.quit()
