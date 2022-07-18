from email.message import EmailMessage #this already comes from python so no need for downloading ;)
import ssl # work as a layer of security stands for Secure Sockets Layer. use : standard technology for keeping an internet connection secure 
import smtplib #we can use it to send the email and as long we write it right it will work :)

email_sender = 'testingpythonthing@gmail.com' #Sender the one who sends the Email thing
email_password = 'hkaihwxwjzgkydjr' #16 digit password
email_receiver = 'vpl.verena@gmail.com','arkan.parvaiz@gmail.com','nandanuruli16@gmail.com','angelinaapatrisiaa@gmail.com','verenalaurentius@gmail.com'
#Receiver send email to this person

subject = 'Hi' #Subject in Gmail
body = """"Hi, whats up""" #The thing we write here

em = EmailMessage()  #Em means Email message thing from top above
em['From'] = email_sender #basically in short it makes them all give what it means and make them all became 1 (if that makes anysense)
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context() #basically so we can use the sll thing and for context thing

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp: #The Most important part i thing from my research almost every code has this for it to send emails
    smtp.login(email_sender, email_password) #to log in and get in to the email
    smtp.sendmail(email_sender, email_receiver, em.as_string()) #Send the mail thing and as_string for proper format