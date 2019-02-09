import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.vagalume.com.br/top100/musicas/'
html = requests.get(url)
sopa = bs(html.content, 'html.parser')
musicas = sopa.findAll('li',
		{'class': 'vArtH'})
for m in musicas:
  spans = m.a.findAll('span')
  pos = spans[0].string
  print (pos, end = ' ')
  nome = spans[1].string
  print (nome, end = ' - ')
  print (m.a.b.string)
