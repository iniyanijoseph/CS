import requests
from bs4 import BeautifulSoup
wordlist = ["compassion", "mindfulness", "empathy", "kindness", "inspiration", "random acts of kindness", "hope", "caring", "human kindness", "goodwill", "considerate", "unselfish", "good-hearted", "kind-hearted", "altrusim", "goodness", "good-natured", "generosity", "generous", "forgiveness" ]
result = requests.get("https://themindunleashed.com/good-news")
src = result.content
src = BeautifulSoup(src, 'lxml')
text = src.get_text()

for element in wordlist:
    if element in text:
        for subheading in src.find_all('h3'):
            link = subheading.a
            print(link)
            link = link.get("href")
            print(link)
