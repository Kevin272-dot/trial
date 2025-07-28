from collections import deque
"""def calculate_diameter_circle(radius: float) -> float:

    diameter = radius*2
    if diameter >= 0:
        return diameter

    else:
        return -1


print(calculate_diameter_circle(7))
print(calculate_diameter_circle(2.5))
print(calculate_diameter_circle(0))
print(calculate_diameter_circle(-3))
print(calculate_diameter_circle(1000000))"""
# -----------------------------------------------------------------------------------


"""def celsius_to_fahrenheit(celsius: float) -> float:
    c_fahrenheit = (celsius * 9/5) + 32
    return c_fahrenheit


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    f_celsius = (fahrenheit - 32) * 5/9
    return f_celsius


def convert_temperature(temperature, unit):
    if unit == 'C':
        return celsius_to_fahrenheit(temperature)
    else:
        return fahrenheit_to_celsius(temperature)


temperature_c = 25.0
temperature_f = 77.0

converted_f = convert_temperature(temperature_c, 'C')
converted_c = convert_temperature(temperature_f, 'F')

print(f"{temperature_c}°C is equal to {converted_f}°F")
print(f"{temperature_f}°F is equal to {converted_c}°C")"""
# -----------------------------------------------------------------------------------


"""def make_sandwich(bread_type, filling, cheese=None, toasted=False):
    if toasted == True and cheese != None:
        l = f"Making a toasted {bread_type} sandwich with {filling} and {cheese} cheese."
        return l
    if toasted == False and cheese == None:
        i = f"Making a {bread_type} sandwich with {filling}."
        return i


t = make_sandwich("wheat", "turkey", "cheddar", True)
d = make_sandwich("rye", "ham")
print(t)
print(d)"""
# ------------------------------------------------------------------------------------


""""product_catalog = {"SKU123": {"name": "Widget A", "price": 19.99, "quantity": 50}, "SKU456":
                   {"name": "Gadget B",
                    "price": 34.95,
                    "quantity": 25}, "SKU789":
                   {"name": "Gizmo C",
                    "price": 9.99,
                    "quantity": 100}}

# Look up this SKU in your code.
sku_to_find = "SKU123"
print(
    f"The price of {product_catalog[sku_to_find]['name']} is ${product_catalog[sku_to_find]['price']}")"""
# -----------------------------------------------------------------------------------


"""def check(data, target):
    # Binary search to find the index of target in sorted data.
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            low = mid + 1
        elif data[mid] > target:
            high = mid - 1
    return -1


data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15,
        16, 17, 18, 19, 20, 56, 89, 45, 67, 78, 90, 100]
target = 1
print(f"Index of {target}: {check(data, target)}")"""
# -----------------------------------------------------------------------------------


"""import bisect
dat = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15]
bisect.insort(dat, 16)
print(dat)"""
# -----------------------------------------------------------------------------------


"""def quicksort(cards):
    if len(cards) < 2:
        return cards  # Base case: Already sorted if 0 or 1 element
    else:
        pivot = cards[0]  # Choose first card as pivot
        less = [i for i in cards[1:] if i <= pivot]
        greater = [i for i in cards[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


cards = [4, 2, 7, 1, 3, 6, 5, 89, 45, 67, 78, 90, 100]
print(quicksort(cards))"""
# -----------------------------------------------------------------------------------


"""from collections import deque, Counter

# Deque example
queue = deque()
queue.append("task1")
queue.append("task2")
print(queue.popleft())  # Output: task1

# Counter example
text = "This is a sample text with some repeated words words"
word_counts = Counter(text.split())
print(word_counts)"""
# -----------------------------------------------------------------------------------


"""import logging
logging.basicConfig(filename='app.log', level=logging.DEBUG)
logging.debug('This is a debug message')
logging.info('This is an informational   message')
logging.warning('This is a warning message')
logging.error('This is an error message')"""
# -----------------------------------------------------------------------------------


"""def calculate_area(length, width):
    assert length > 0, "Length must be positive"
    assert width > 0, "Width must be positive"
    return length * width

print(calculate_area(5, 10))"""
# -----------------------------------------------------------------------------------


"""try:
    import logging
    result = 10 / 0

except Exception as e:
    logging.error(f"An error occurred: {e}")"""
# -----------------------------------------------------------------------------------
"""def read_file_contents(file_path):
   
    try:
        with open(file_path,"r") as file:
            file.read()

    except FileNotFoundError:

        print("Error: File not found -",file_path)
read_file_contents("/Users/Example/Documents/my_file.txt")"""
# -----------------------------------------------------------------------------------
"""def bubble_sort(scores):
    if len(scores)<2:
        return scores
    while True:
        pivot = scores[0]
        lower = [i for i in scores if i<=pivot]
        high = [i for i in scores if i>pivot]
        return bubble_sort(lower) + [pivot] + bubble_sort(high)

    return -1"""
# -------------------------------------------------------------------------------------

# Sample data
"""import pandas as pd
data = {'age': [25, 30, 35, 40], 
        'gender': ['male', 'female', 'male', 'female'],
        'income': [50000, 60000, 75000, 55000]}

# Create a DataFrame
df = pd.DataFrame(data)

# Convert 'gender' to a categorical variable
df['gender'] = df['gender'].astype('category')

# Calculate average income
average_income = df['income'].mean()

# Count the number of males and females
gender_counts = df['gender'].value_counts()

print(average_income)
print(gender_counts)"""
# -------------------------------------------------------------------------------------
"""import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 3*np.pi, 500)
plt.plot(x, np.sin(x**2))
plt.title('A simple sine wave')
plt.show()"""
# -------------------------------------------------------------------------------------

# Boolean indexing with pandas
"""df[(df['membership_level'] == 'Platinum') & (df['number_of_purchases'] > 10)]"""
# -------------------------------------------------------------------------------------
"""customer_info = df.loc[df['Name'] == 'John Doe', ['Email', 'Phone']]"""
# -------------------------------------------------------------------------------------


"""import panda as pd
import random
import string

# Set a seed for reproducibility
random.seed(42)

# Generate sample data
data = {
    "ID": [i for i in range(1, 51)],
    "Name": [''.join(random.choices(string.ascii_uppercase, k=5)) for _ in range(50)],
    "Age": [random.randint(18, 65) for _ in range(50)],
    "Department": [random.choice(['HR', 'Finance', 'IT', 'Marketing', 'Sales']) for _ in range(50)],
    "Salary": [round(random.uniform(30000, 100000), 2) for _ in range(50)]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv("sample_data.csv", index=False)"""
# --------------------------------------------------------------------------------------
"""import matplotlib.pyplot as plt
fig, ax = plt.subplots(2, 2)
ax[0, 1].plot([1, 2, 3], [4, 5, 6])
ax[1, 1].bar(["A", "B", "C"], [7, 8, 9])
ax[0, 0].scatter([1, 2, 3], [4, 5, 6])
ax[1, 0].hist([1, 2, 1, 4, 5, 4, 7, 5, 7])
plt.show()"""

"""from bs4 import BeautifulSoup
html_content = """"""
from collections import deque
<div class="product">
  <h1>Awesome Headphones</h1>
  <p class="price">$99.99</p>
  <p class="description">These headphones offer amazing sound quality!</p>
</div>
""""""

soup = BeautifulSoup(html_content, 'html.parser')
h = soup.find('h1')
product_name = h.get_text()
p1 = soup.find('p', class_="price")
p2 = soup.find('p', class_="description")
price = p1.get_text()
description = p2.get_text()

# Use soup.find() to locate the <h1> tag and store the extracted text in a variable called 'product_name'.
### YOUR CODE HERE ###

# Use soup.find() to locate <p> tags with class_='price' and store the extracted text in a variable called 'price'.
### YOUR CODE HERE ###

# Use soup.find() to locate <p> tags with class_='description' and store the extracted text in a variable called 'description'.
### YOUR CODE HERE ###

# Print the extracted data in the format:
print(f"Product name: {product_name}")
print(f"Price: {price}")
print(f"Description: {description}")"""
# ---------------------------------------------------------------------------------------
"""import os
from bs4 import BeautifulSoup
import requests
url = "https://scikit-learn.org/stable/"
try:
    response = requests.get(url)
    response.raise_for_status  # checks for https errors
except Exception as e:
    print(f"Unable to fetch data {e}")
else:
    soup = BeautifulSoup(response.content, 'html.parser')

ch = soup.find_all('img')
image_urls = []
for img in ch:
    img_src = img.get('src')
    if img_src:
        absolute_img_url = requests.compat.urljoin(url, img_src)
        image_urls.append(absolute_img_url)
if not os.path.exists("downloaded_images"):
    os.makedirs("downloaded_images")

for img_url in image_urls:
    try:
        img_data = requests.get(img_url).content
        img_name = os.path.join("downloaded_images", os.path.basename(img_url))
        with open(img_name, 'wb') as handler:
            handler.write(img_data)
        print(f"Downloaded: {img_name}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {img_url}: {e}")"""
# -------------------------------------------------------------------------------------
"""n = int(input("enter the line to be deleted:"))
try:
    with open("input1.txt", "r") as f:
        r = f.readlines()
except Exception as e:
    print(f"an error occured {e}")
else:
    if 0 < n <= len(r):
        r.pop(n-1)
        with open("input1.txt", "w") as f:
            f.writelines(r)
        for i in r:
            print(i, end='')
    else:
        print("Invalid line number.")"""
# -------------------------------------------------------------------------------------
"""queue = deque()
for i in range(5):
    n = int(input("Enter a number:"))
    queue.append(n)
for i in queue:
    print(i, end=' ')
print("\n")
for i in range(2):
    n = queue.popleft()
    queue.append(n)
for i in queue:
    print(i, end=' ')"""
# -------------------------------------------------------------------------------------
