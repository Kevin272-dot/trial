"""from bs4 import BeautifulSoup
html_content = #add 3 quotes for html when you execute
<html>
<body>
    <h1>This is a sample heading</h1>
    <p>This is a sample paragraph</p>
    <p class = "special">This is a sample paragraph</p>
</body> 
</html>
soup = BeautifulSoup(html_content, 'html.parser')
find_one = soup.find('p')
print(find_one)
all = soup.find_all('p')
for i in all:
    print(i)
withclass = soup.find('p', class_="special")
print(withclass)
print(withclass.get_text())"""
# --------------------------------------------------------------------------------------
"""from bs4 import BeautifulSoup
html_content =
<html>
<body>
    <div id = "main-content">
        <h1>This is a heading</h1>
        <p class = "important">This is a important paragraph</p>
        <a href="https://www.example.com">visit example</a>
    </div>
</body>
</html>
soup = BeautifulSoup(html_content, "html.parser")
main = soup.select_one('#main-content')
imp = main.select_one('.important')
no_tags = imp.get_text()
print(no_tags)
lin = main.select_one("a")
hyperlink = lin['href']
print(hyperlink)"""
# -----------------------------------------------------------------------------------
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

ch = soup.find_all('div')
l = []
for i in ch:
    l.append(i.get_text())
print(l)
# ------------------------------------------------------------------------------------
