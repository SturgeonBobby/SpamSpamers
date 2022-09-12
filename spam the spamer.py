#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def spam_the_spamer(stmp_addr,number_of_emails,time_interval):
    from_email = input("From Email: ")
    password = input("Password: ")
    to_email = input("To Email: ")
    subject = input("Subject: ") # The subject line
    message = input("Massage: ")

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    server = smtplib.SMTP(stmp_addr, 587)
    server.starttls()
    server.login(from_email, password)
    
    # Attach the message to the MIMEMultipart object
    msg.attach(MIMEText(message, 'plain'))
    text = msg.as_string() # You now need to convert the MIMEMultipart object to a string to send

    for i in range(int(number_of_emails)):
        print(i)
        try:
            server.sendmail(from_email, to_email, text)
        except:
            print('Trying again!')
            server.sendmail(from_email, to_email, text)
        time.sleep(int(time_interval))
    server.quit()    

spam_the_spamer("smtp-mail.outlook.com",1000,1)

