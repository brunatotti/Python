import requests
import json
url = "http://educacao.dadosabertosbr.com/api/escolas/buscaavancada?situacaoFuncionamento=1&energiaInexistente=on&aguaInexistente=on&esgotoInexistente=on"

p = requests.get(url)
dados = json.loads(p.content.decode("utf-8"))

n = dados[0]
print(f'Existem (n) escolas, em funcionamento')
print('Sem água, sem esgoto e sem luz')

for escola in dados [1]:
    print(escola['nome'] + " - " +  escola['cidade'], escola['estado'])

