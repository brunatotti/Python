import requests
from bs4 import BeautifulSoup as bs
import string
alfabeto = string.ascii_uppercase
main_url = 'https://www.bayerpet.com.br'

for pets in ("Caes", "Gatos"):
    print('\n' + pets + '\n')
    for letras in alfabeto:
        for paginas in range(1,4):
            url = main_url + f'/{pets}/lista-nomes/{letras}/{paginas}'
            html = requests.get(url)
            sopa = bs(html.content, 'html.parser')

            lista = sopa.find('ul', {'class':'listNames'})
            
            lis = lista.findAll('li')
            for li in lis:
                print(li.string)
            
