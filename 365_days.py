import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import schedule
import time
from plyer import notification
import random
import smtplib
from email.mime.text import MIMEText
import imaplib
import pandas as pd
import numpy as np
# 1 sending an email
"""smtp_server = "smtp.gmail.com"
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
    server.quit()"""
# 2 counting emails from a specific sender
"""email_provider = "imap.gmail.com"
port = 993
user = "lrkevindaniel@gmail.com"
user_password = "jmfe crkv xcbe rtvn"
sender_email = "noreply.cc1@vit.ac.in"
count = 0
try:
    mail = imaplib.IMAP4_SSL(email_provider, port)
    mail.login(user, user_password)
except Exception as e:
    print(f"Error connecting to IMAP server: {e}")
else:
    mail.select("Inbox")
    status, response = mail.search(None, f'(FROM {sender_email})')
    if status == "OK":
        message_ids = response[0].decode().split()
        count = len(message_ids)
    else:
        print(f"Error searching for emails: {status}")
    print(f"Number of emails from {sender_email}: {count}")"""
# 3 Send a notification to remind me to code daily


"""def send_notification():
    reminder = "never give up even when all seems lost"
    notification.notify(title="Reminder to code daily",
                        message=reminder,
                        app_icon="C:\\Users\\lrkev\\Downloads\\code_reminder_icon.ico",
                        timeout=10)


schedule.every(2).minutes.do(send_notification)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)"""
# 4.1 binary search only works for sorted data structures


"""def binary_search(l, target):
    low = 0
    high = len(l)-1
    while low <= high:
        mid = (low+high)//2
        if l[mid] == target:
            return mid
        elif l[mid] < target:
            low = mid + 1
        else:
            high = mid-1


unique_numbers = [6567, 8488, 7819, 6890, 1887, 8253, 3763, 1406, 3679, 1979, 9527, 3738, 1818, 1370, 5047, 5106, 5130, 2087, 5943, 1834, 6812, 8678, 8817, 3294, 593, 8397, 5537, 9184, 1786, 4272, 7633, 3356, 8539, 773, 7182, 8990, 1037, 5645, 4663,
                  7958, 9701, 9466, 4125, 3913, 2073, 9434, 679, 1685, 779, 1107, 3425, 9935, 6955, 6459, 5227, 6792, 9249, 2467, 834, 9721, 7889, 1153, 7390, 9207, 4710, 9094, 9885, 3177, 5423, 609, 8449, 668, 2543, 3531, 4419, 9713, 249, 5952, 8058, 3811, 1803, 9553, 436, 7750, 4797]

print(binary_search(sorted(unique_numbers), 436))"""
# 5 Quick sort()


"""def quick_sort(l):
    if len(l) <= 2:
        return l
    else:
        pivot = l[0]
        lower = [i for i in l[1:] if i <= pivot]
        higher = [i for i in l[1:] if i > pivot]
        return quick_sort(lower) + [pivot] + quick_sort(higher)


l = unique_numbers = [6567, 8488, 7819, 6890, 1887, 8253, 3763, 1406, 3679, 1979, 9527, 3738, 1818, 1370, 5047, 5106, 5130, 2087, 5943, 1834, 6812, 8678, 8817, 3294, 593, 8397, 5537, 9184, 1786, 4272, 7633, 3356, 8539, 773, 7182, 8990, 1037, 5645, 4663,
                      7958, 9701, 9466, 4125, 3913, 2073, 9434, 679, 1685, 779, 1107, 3425, 9935, 6955, 6459, 5227, 6792, 9249, 2467, 834, 9721, 7889, 1153, 7390, 9207, 4710, 9094, 9885, 3177, 5423, 609, 8449, 668, 2543, 3531, 4419, 9713, 249, 5952, 8058, 3811, 1803, 9553, 436, 7750, 4797]
print(quick_sort(l))"""

# 5 scrapping with beautifulsoup
"""url = "https://scikit-learn.org/stable"
l = []
try:
    response = requests.get(url)
    response.raise_for_status()
except Exception as e:
    print(f"error {e}")
else:
    soup = BeautifulSoup(response.content, 'html.parser')
    ch = soup.find_all('img')
    for i in ch:
        l.append(i.get_text)
finally:
    print(l)"""
# 6 a simple graph plot
"""fig = plt.figure(figsize=(10, 20))
fig, ax = plt.subplots(2, 2)
ax[0, 0].plot([2, 4, 5, 6], [4, 6, 7, 8], color="red", linestyle="dashed")
ax[0, 1].scatter([5, 6, 7, 8, 9], [9, 8, 6, 4, 3])
ax[1, 0].bar(["A", "B", "C"], [9, 8, 6], color=["blue", "orange", "red"])
ax[1, 1].hist([2, 4, 4, 4, 3, 3, 3, 5, 5, 5, 6, 6, 8, 8],
              edgecolor="black", color="green")
plt.legend()
plt.show()"""
# 7.1 pandas and matplotlib

"""df = pd.read_csv("simple_car_sales_data.csv")
df.head()
df.tail()
dff = df.groupby("Region")["Units_Sold"].sum()
print(dff)
plt.pie(dff, labels=dff.index, autopct="%1.1f%%")
plt.legend(dff.index)
plt.title("a simple pie chart")
plt.show()"""
# 7.2 numpy and matplotlib
"""x = np.linspace(1, 50, 200)
y = np.sin(x)
plt.plot(x, y, linestyle="dashed")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("A simple sine way")
plt.legend("Wave")
plt.show()"""
# 7.3 pandas
"""df = pd.read_csv("sample_data.csv")
df["Salary"].fillna(df.query('Department == "IT"')[
                    "Salary"].mean(), inplace=True)
print(df)"""
# 7.4
"""df = pd.read_csv("sample_data.csv")
df["Salary"].fillna(df.loc[df["Department"] == "HR", "Salary"]).mean()"""
# 7.5
"""df = pd.read_csv("sample_data.csv")
print(df.agg({"Salary": ['mean', 'max',  'min'],
              "Age": ['mean', 'max',  'min']}))"""
# 8.1 pandas
"""df = pd.read_csv("sample_data.csv")
df["Salary"].fillna(df.query('Department == "HR"')["Salary"].mean(),inplace = True)"""

# 8.2 matplotlib and pandas
"""df = pd.read_csv("sample_data.csv")
df.groupby("Department")["Salary"].sum().plot(kind="bar")
dff = df["Department"]
plt.legend()
plt.show()"""
# 8.3 beautifilsoup
"""url = "https://scikit-learn.org/stable"
links = []
try:
    response = requests.get(url)
    response.raise_for_status()
except Exception as e:
    print(f"error in fetching data {e}")
else:
    soup = BeautifulSoup(response.content, "html.parser")
    ch = soup.find_all("img")
    for i in ch:
        lin = i.get("src")
        if lin:
            absolute_img_url = requests.compat.urljoin(url, lin)
            links.append(absolute_img_url)
finally:
    print(links)"""
# 9 Decorater

"""
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(
            f"Function {func.__name__} Exceution time {execution_time: .5f} seconds")
        return result

    return wrapper


@timer
def calculate_area(length, breadth):
    time.sleep(1)
    area = length*breadth
    return area


length = 7
breadth = 5
print(calculate_area(length, breadth))"""
# 10
"""x = np.random.randn(10)
y1 = np.random.randn(10)
y2 = np.random.randn(10)
plt.plot(x, y1)
plt.plot(x, y2)
plt.legend(["first", "second"])
plt.show()
"""
# 11
"""x = [2, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 8, 5, 4]
y = [5, 7, 8, 9, 4, 4, 3, 3, 5, 6, 6, 6, 9, 8]
plt.hist2d(x, y, edgecolor="black")
plt.title("Simple Histogram")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
plt.legend()"""
# 12.1


"""def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b


finbannoci = fib()
n = int(input("enter a number:"))
for i in range(n):
    print(i)"""
# 13
"""
smtp_mail = "smtp.gmail.com"
smtp_port = 587
smtp_sender = "lrkevindaniel@gmail.com"
smtp_password = "jmfe crkv xcbe rtvn"
smtp_reciver = "lrlauracynthis@gmail.com"
message = MIMEText("Hi Laura")
message["Subject"] = "This is a text email from python"
message["From"] = smtp_sender
message["To"] = smtp_reciver

try:
    sender = smtplib.SMTP(smtp_mail, smtp_port)
    sender.starttls()
except Exception as e:
    print(f"Error in starting TLS: {e}")
else:
    sender.login(smtp_sender, smtp_password)
    sender.send_message(message)
"""

# Example of a simple progress indicator
for i in range(11):
    print(f"Progress: {i*10}% \r", end="")
    time.sleep(0.5)
print("\nTask complete!")  # Print a newline at the end
