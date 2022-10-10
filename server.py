import smtplib
import socket
import csv
import re

sender = 'familyninhbinh@gmail.com'
receivers = ['nulldoot2k@proton.me']

def sendemail(message):
  try:
    smtpObj = smtplib.SMTP('localhost', 1025)
    message = read_csv()
    smtpObj.sendmail(sender, receivers, str(message))
    print("send")
  except:
    print("Can't send email")

def read_csv():
  with open("./mail_data.csv", 'r') as file:
    csv_reader = csv.reader(file)
    count = 0
    for row in csv_reader:
        for item in row:
          pattern = '(fuck)|(spam)'
          count += len(re.findall(pattern, item))
    check_is_spam = True if count > 5 else  False
    print(count)  
    print(check_is_spam)

host = 'localhost'
port = 12500
size = 1024
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.bind((host, port))
  s.listen()
  print(f"Listening on {host}:{port}")
  client, addr = s.accept()
  print(f"Received connection")
  while 1:
    data = client.recv(size)
    if data:
      print(f"Data to send by mail: {data.decode()}")
      sendemail(data.decode())
client.close()
