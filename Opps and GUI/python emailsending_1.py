import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

COMMASPACE = ', '

def main():
    sender = 'srinudarpally@gmail.com'
    password = '@srinu...123#'
    receipants = ['cnu444345@gmail.com','balachandhar787@gmail.com']


    #Create the enclosing(outer) message
    outer = MIMEMultipart()
    outer['Subject'] = 'an attachment for you'
    outer['To']  = COMMASPACE.join(receipants)
    outer['From'] = sender
    outer.preamble = 'You will not see this in a MIME-aware mail reader.\n'

    #List of attachments
    attachments = ['C:\pakages in python.txt']

    #Add the attachments to the message
    for file in attachments:
        try:
            with open(file,'rb') as fp:
                msg = MIMEBase('application', "octet-stream")
                msg.set_payload(fp.read())
            encoders.encode_base64(msg)
            msg.add_header('Content-Disposition','attachment',filename=os.path.basename(file))
            outer.attach(msg)   
        except:
            print('Unable to open one of the attachments. Error: ')
            raise
    composed = outer.as_string()
    
    try:
        with smtplib.SMTP('smtp.gmail.com',587) as s:
            s.ehlo()
            s.starttls()
            s.ehlo()
            s.login(sender,password)
            s.sendmail(sender,receipants,composed)
        print('Email sent')
    except:
        print('Unable to sed the email. Error : ')
        raise

if __name__ == '__main__':
    main()
    
