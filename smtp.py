import smtplib 
import os
import sys
from configparser import ConfigParser

def readFile(path):
  file = open(path)
  str = file.read()
  return str

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

if __name__ == "__main__":
  to_addr = 'familyninhbinh@gmail.com'
  subject = "Test mail"
  body_text = readFile("mail_data.csv")
  send_mail(subject, to_addr, body_text)
