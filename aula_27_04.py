import requests
from bs4 import BeautifulSoup as bs
url = 'http://beans.itcarlow.ie/prices.html'
p = requests.get(url)
s = bs(p.content, 'html.parser')
print (s.strong)
print (s.strong.string)
