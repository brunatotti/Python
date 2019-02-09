import requests
import json
url = "http://educacao.dadosabertosbr.com/api/escolas?nome=poliedro"

p = requests.get(url)
dados = json.loads(p.content.decode("utf-8"))

n = dados[0]
for escola in dados [1]:
    print(escola['nome'])

