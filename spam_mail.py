import smtplib

sender = "nulldoot2k@proton.me"
rec = "familyninhbinh@gmail.com"

message = "hello this is my spam mail"

server = smtplib.SMTP("localhost:1025")
print("Login ok")
i = 0
while i < 5:
  server.sendmail(sender, rec, message)
  print("abc : ", rec)
