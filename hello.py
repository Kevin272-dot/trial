

"""class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def introduce(self):
        print(f"Hi I am {self.name} and I am a {self.colour} {self.species}")


dog = Pet("Buddy", "Dog")
cat = Pet("Whiskers", "Cat")
cat.colour = "White"
cat.introduce()
dog.name = "Max"
dog.colour = "Brown"
dog.introduce()"""
# -----------------------------------------------------------
import smtplib
from email.mime.text import MIMEText
smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_email = "lrkevindaniel@gmail.com"
sender_password = "jmfe crkv xcbe rtvn"
receiver_email = "lrlauracynthia@gmail.com"

message = MIMEText("Hi Donkey")
message['Subject'] = "Hello from Kevin"
message["From"] = sender_email
message["To"] = receiver_email

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Secure the connection
    server.login(sender_email, sender_password)
    server.send_message(message)
    print("Email sent successfully!")
except Exception as e:
    print(f"Error sending email: {e}")
finally:
    server.quit()
