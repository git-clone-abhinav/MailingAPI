import smtplib
import os
import logger
import time
logpath = os.getenv('logs')
lists = os.getenv('lists')
from email.message import EmailMessage

def mail(uid,pwd,tolist,sub,body):
    try:
        server = smtplib.SMTP_SSL('mail.pichavaram.in', 465)
        server.ehlo()
        #server.starttls()
        server.ehlo()
        server.login(uid,pwd)
        mails = open(f"{lists}{tolist}.csv","r")
        mail_to = mails.read()
        mail_to = mail_to.split(',')
        print(mail_to)
        mails.close()
        for i in mail_to:
            msg = EmailMessage()
            msg['Subject'] = sub
            msg['From'] = uid
            msg.set_content(body)
            cc= i.lstrip("\n")
            msg['To'] = cc
            server.send_message(msg)
            print(f"Mail sent to {cc}".format())
            logger.log_it(f"Mail sent to {cc}, Sub: {sub}, Body: {body})")
            time.sleep(5)
        server.quit()
    except Exception as e:
        #error_code =  e.smtp_code
        #error_message = e.smtp_error
        logger.log_it(f"Mail Sending Error {e} ")