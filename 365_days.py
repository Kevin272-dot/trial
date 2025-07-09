import smtplib
from email.mime.text import MIMEText
# 1
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_sender = "lrkevindaniel@gmail.com"
smtp_password = "jmfe crkv xcbe rtvn"
smtp_receiver = "lrlauracynthia@gmail.com"
message = MIMEText("Hi Laura")
message["Subject"] = "This is a text email from python"
message["From"] = smtp_sender
message["To"] = smtp_receiver

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
except Exception as e:
    print(f"Error connecting to SMTP server: {e}")
else:
    server.login(smtp_sender, smtp_password)
    server.send_message(message)
    print("Email sent successfully!")
finally:
    server.quit()
