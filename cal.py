"""def calculate(a, b):
    return a*b"""
l = [["f", "g", "h"], ["i", "j", "k"], ]
l.j = 'J'
print(l)


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
# --------------------------------------------------------------------------------------
