import requests
# response =requests.get("https://www.facebook.com/aksa.oshin")
# print(response.text)

url= "https://www.codewithharry.com/blogpost/django-cheatsheet/"
r= requests.get(url)
# print(r.text)
from bs4 import BeautifulSoup
soup= BeautifulSoup(r.text,'html.parser')
print(soup.prettify())
for heading in soup.find_all("h2"):
  print(heading.text)