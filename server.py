import smtplib
import socket
import csv
import re

sender = 'server@proton.me'
receivers = ['client@gmail.com']

def send_mail(sender, receivers, message) -> bool:
  try:
    smtpserver = smtplib.SMTP('localhost', 1025)
    smtpserver.sendmail(sender, receivers, str(message))
    return True
  except smtplib.SMTPException:
    return False

host = "127.0.0.1"
port = 12500
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host,port))
sock.listen()
print(f"Listening on {host}:{port}")
conn, addr = sock.accept()
with conn:
  print(f"Connection received from {addr}")
  while True:
    data = conn.recv(1024)
    if data:
      data = data.decode().splitlines()
      source = data[0].split("From: ")[1]
      print(f"From: {source}") # You can remove this line
      destination = data[1].split("To: ")[1]
      print(f"To: {destination}") # You can remove this line
      subject = data[2].split("Subject: ")[1]
      print(f"Subject: {subject}") # You can remove this line
      message = "\n".join(data[4:])
      print(f"Message: \n{message}") # You can remove this line
      if send_mail(source, destination, message):
        conn.send(b"Email sent.")
      else:
        conn.send(b"Cannot send email.")

