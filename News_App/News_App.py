import requests
import json
query= input("What type of news ypu are inetrersted in?")
url= f"https://newsapi.org/v2/everything?q={query}&from=2023-02-10&sortBy=publishedAt&apiKey=36da0d5786ea44a188e00a0727127e69"
r = requests.get(url)
news = json.loads(r.text)
#print(r.text)
# print(news,type(news))
for article in news["articles"]:
  print(article["title"])
  print(article["description"])
  print("--------------------")