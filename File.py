import requests
from bs4 import BeautifulSoup


response = requests.get("https://www.imdb.com/list/ls041677842/")
soup = BeautifulSoup(response.content)
print(soup)
print("---------------")
