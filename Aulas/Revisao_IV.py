'''
#no shell
#primeiro chama a funcao
import random
#depois
random.randint(1,100)
#para sortear numeros entre 1 e 100

def embaralha(s):
    import random
    lista = list(s)
    random.shuffle(lista)
    return''.join(lista)
#no sheel colocar:
embaralha('bruna')
#irá embaralhar a palavra


#para sortear 15 numeros entre 10 e 100
import random
lista = []
for k in range (15):

    lista.append(random.randint(10,100))
print (lista)

#para sortear 15 numeros DIFERENTES entre 10 e 100
import random
lista = []
while len(lista) < 15:
    x = random.randint(10,100)
    if x not in lista:
        lista.append(x)
    lista.sort()
    print(lista)

#tradutor com criptografia de cesar
def esconde (msg):
    s = ''
    for c in msg: s += chr(ord(c) + 30000)
    return s
def mostra (msg):
    s = ''
    for c in msg: s += chr(ord(c) - 30000)
    return s
#aperto o f5 e digito:
esconde('Bruna')
#vai aparecer:
'畲疢疥疞疑'
#faço:
mostra('畲疢疥疞疑')
#vai aparecer:
'Bruna'

#arquivos servem para vc fazer armazenamento permanente
arquivo = open('numero.txt', 'w')
for linha in range(1,101):
    arquivo.write('%d\n' % linha)
arquivo.close()
#nao vai aparecer nada na tela, mas no diretorio
#onde esta meu programa irá aparecer um arquivo numero.txt

arquivo = open('numero.txt', 'r')
for linha in arquivo.readlines():
    print(linha)
arquivo.close()

#readlines gera uma lista onde cada elemento é uma linha lida
#mesma coisa mais sem pular linha:
with open('numero.txt') as f:
    print(f.read())
#o with é inteligente. Ele abre e fecha o arquivo

#ler mensagem.txt e grave cripto.txt com todas as vogais trocadas por '*'
texto = open('mensagem.txt')
saida = open('cripto.txt', 'w')
for linha in texto.readline():
    for linha in linha:
        if letra in 'aeiou':
            saida.write('*')
        else:
            saida.write('*')
texto.close()
saida.close()
'''

#validacao de endereço IP
def ip_ok (ip):
    ip = ip.split('.')
    for byte in ip:
        if int(byte) > 255:
            return False
    return True
arq = open ('IPS.txt')
validos = open ('Validos.txt', 'w')
invalidos = open('Invalidos.txt', 'w')
for linha in arq.readlines():
    if ip_ok (linha):
        validos.write(linha)
    else:
        invalidos.write(linha)
arq.close()
validos.close()
invalidos.close()

'''
arquivo = open('ola.html', 'w', encoding='utf-8')
arquivo.write(<!DOCTYPE html>
<html lang='pt-BR'>
<head>
<meta charset='utf-8'>
<title>Titulo da Pagina</title>
</head>
<body>
Olá!
</body>
</html>)
arquivo.close()
'''










