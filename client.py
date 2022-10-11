import smtplib
import socket

sender = 'client@gmail.com'
receivers = ['server@gmail.com']
data = open("content.txt", "r").read()
message = f"""From: From Person {sender}
To: To Person {receivers}
Subject: SMTP e-mail test

This is a test e-mail message.
{data}
"""

HOST = "127.0.0.1"
PORT = 12500
try:
  print(f"Found: {HOST}:{PORT}")
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client.connect((HOST,PORT))
  client.send(message.encode())
  message = client.recv(1024)
  print(message.decode())
except:
  print("Not found port")
