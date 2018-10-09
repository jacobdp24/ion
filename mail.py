from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import requests
from config import *
from addresses import emails, sourceAddress
from login import USERNAME, PASSWORD

#set up server
s = smtplib.SMTP(host='smtp.ucsd.edu',port=587)
s.starttls()
s.login(USERNAME, PASSWORD)
fromaddr = sourceAddress
destinations = emails

for address in destinations:
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['to'] = address
    msg['Subject'] = subject
    body = message
    msg.attach(MIMEText(body, 'plain'))

    s.ehlo()
    s.ehlo()
    s.login(USERNAME, PASSWORD)
    text = msg.as_string()
    s.sendmail(fromaddr, address, text)

s.quit()