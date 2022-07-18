from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'testingpythonthing@gmail.com' 
email_password = 'hkaihwxwjzgkydjr'
email_receiver = 'vpl.verena@gmail.com','arkan.parvaiz@gmail.com','nandanuruli16@gmail.com','angelinaapatrisiaa@gmail.com','verenalaurentius@gmail.com'

subject = 'HELLO'
body = """"Hi, Im just testing this out"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())