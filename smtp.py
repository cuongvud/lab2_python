import smtplib 
import os
import sys
import csv
from configparser import ConfigParser
import re

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


read_csv()

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

#if __name__ == "__main__":
 # to_addr = 'familyninhbinh@gmail.com'
  #subject = "Test mail"
  #body_text = readFile("mail_data.csv")
  #send_mail(subject, to_addr, body_text)
