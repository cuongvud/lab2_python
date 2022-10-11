import smtplib
import socket

sender = 'client@gmail.com'
receivers = ['server@gmail.com']

message = """From: From Person {sender}
To: To Person <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
<b>This is HTML message.</b>
<h1>This is headline.</h1>
"""

def send_mail(message):
  try:
    print(message)
    smtpObj = smtplib.SMTP('localhost', 1025)
    smtpObj.sendmail(sender, receivers, message)         
    print("Successfully sent email")
  except smtplib.SMTPException:
    print("Error: unable to send email")

HOST = "127.0.0.1"
PORT = 12500
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST,PORT))
send_mail(message)
