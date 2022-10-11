import smtplib
import socket
import csv
import re

sender = 'server@proton.me'
receivers = ['client@gmail.com']

def receive_mail(data):
  try:
    smtpserver = smtplib.SMTP('localhost', 1025)
    message = check_data()
    if check_data.count > 5:
      print("Not found Spam")
      smtpserver.sendmail(sender, receivers, str(message))
  except smtplib.SMTPException:
    return print("Can't send email")
  
def check_data():
  with open("mail_data.csv", 'r') as file:
    csv_reader = csv.reader(file)
    count = 0
    for row in csv_reader:
      for item in row:
        pattern = 'spam'
        count += len(re.findall(pattern, item))
    return count

host = "127.0.0.1"
port = 12500
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))
server.listen()
conn, addr = server.accept()
with conn:
  print(f"Connected by {addr}")
  while True:
    data = conn.recv(1024)
    if data:
      print(f"Data to send by mail: {data.decode()}")
      # receive_mail(data.decode())
    conn.sendall(data)
