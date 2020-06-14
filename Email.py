import smtplib
from email.mime.text import MIMEText

body = "This is a test email.How are you"

msg = MIMEText(body)
msg['From'] = "arjuunajith@gmail.com"
msg['To'] = "arjun_b160140ec@nitc.ac.in"
msg['Subject'] = "Sample Mail"

server = smtplib.SMTP('localhost')

server.starttls()

server.login("arjuunajith@gmail.com","")

server.send_message(msg)

print("Mail Sent")

server.quit()