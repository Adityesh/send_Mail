import smtplib
from getpass import getpass

s = smtplib.SMTP('smtp.gmail.com',587)

s.starttls()

email_input = input("Enter your email id: \n")
email_password = getpass("Enter your email password: \n")

s.login(email_input,email_password)

message = input("Enter the message you want to send: \n")
receiver = input("Enter the email of the person you want to send the message: \n")

s.sendmail(email_input,receiver,message)

s.quit()