import smtplib 
import os
import sys
import csv
from configparser import ConfigParser
import re
import socket

def send_mail(subject, to_addr, body_text):
  """
  Send an email
  """
  base_path = os.path.dirname(os.path.abspath(__file__))
  config_path = os.path.join(base_path, "email.init")

  if os.path.exists(config_path):
    cfg = ConfigParser()
    cfg.read(config_path)
    print("Send Successfull!!!")
  else:
    print("Config not found! Exiting!")
    sys.exit(1)
  host = cfg.get("smtp", "server")
  from_addr = cfg.get("smtp", "from_addr")
  BODY = "\r\n".join((
    "From: %s" % from_addr,
    "To: %s" % to_addr,
    "Subject: %s" % subject ,
    "",
    body_text
    ))
  server = smtplib.SMTP(host, 1025)
  server.sendmail(from_addr, [to_addr], BODY.encode('utf-8'))
  server.close()

readFile = open("mail_data.csv", "r")

HOST = "localhost"  # The server's hostname or IP address
PORT = 12500  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect((HOST, PORT))
  to_addr = 'familyninhbinh@gmail.com'
  subject = "Test mail"
  body_text = readFile.read()
  s.send(send_mail(subject, to_addr, body_text))

