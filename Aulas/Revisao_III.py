'''
#conceito de lista
edificio = ['Souza','Totti', 'Brito', 'Tito']
print (edificio [0])
print (edificio [1])
print (edificio [3])

#Para eu adicionar mais uma palavra dentro desta msm array:
edificio.append('Oliveira')

#Posso iniciar uma lista vazia
lista = []

#ou com informacao
notas = [7.5, 8, 8.6]

#Para acessar a nota
print(notas[0])

#Posso mudar o conteudo
nota [0] = 8.7

# cont += é o mesmo que cont = cont + 1
notas = [6, 7, 8, 9, 9.5]
soma = 0
cont = 0
while cont < 5:
    soma += notas[cont]
    cont += 1
print('Média: %.2f' %(soma/cont))

#solicitando valor de lista para o usuário
notas = []
cont = 0
soma = 0
while cont < 5:
    x = int(input('Nota: '))
    notas.append(x)
    soma += x
    cont += 1
print('Média: %.2f' %(soma/cont))

notas = []
cont = 1
while cont < 5:
    x = int(input('Nota: '))
    notas.append(x)
    cont += 1
    
#ordem inversa
notas = []
cont = 1
while cont <= 10:
    x = float(input('Nota: '))
    notas.append(x)
    cont += 1
cont = 9
while cont >= 0:
    print(notas[cont])
    cont -= 1

#4 notas e a media na tela
notas = []
cont = 0
soma = 0
while cont < 5:
    x = float(input('Nota: '))
    notas.append(x)
    soma += x
    cont += 1
print('Notas:', notas)
print('Média:', soma/5)

#
letras = []
cont = 1
while cont <= 10:
    letras.append(input('Letra: '))
    cont += 1
cont = 0
i = 0
while cont <= 9:
    if letras[cont] not in 'aeiou':
        i += 1
    cont += 1
print ('Foram lidos %d consoantes' %i)

#Fatia do primeiro indice até o anterior do segundo
x = '0123456789'
print(x[0:2]) # Vai imprimir os números 0 e 1
print(x[1:2]) # Vai imprimir o 1
print(x[2:4]) # Vai imprimir o 2 e o 3
print(x[0:5]) # Vai imprimir: 01234
print(x[1:8]) # Vai imprimir o 1234567

print(x[:6]) # Vai imprimir o 012345
print(x[5:]) # Vai imprimir o 56789
print(x[4:-1]) # Vai imprimir o 45678
print(x[-4:-1]) # Vai imprimir o 678
print(x[:]) # Vai imprimir 0123456789

#posso usar um incremento ao fatiar a string
texto = "baatinha quando nasce"
texto[::2] #vai imprimir do inicio até o final, mas pulando de 2 em 2
texto[::-1]

#é palindrome?
palavra = input('Palavra: ')
if palavra == palavra[::-1]:
    print('%s é palíndrome!' %palavra)
else:
    print('%s não é palíndrome!' %palavra)

#Strings são imutáveis
texto = '@' + texto [1:]
print (texto)

#trocar vogal *
palavra = input('Digite uma palavra: ')
k = 0
troca = ''
while k < len(palavra):
    if palavra[k] in 'aeiou':
        troca += '*'
    else:
        troca += palavra[k]
    k += 1
print ('Nova palavra %s' %troca)

#verificação parcial de string
arquivo = 'program.py'
>>> arquivo.startswith ('p')
True
>>> arquivo.endswith ('py')
True
>>> arquivo.endswith ('y')
True
>>> arquivo.endswith ('p')
False
>>> resposta = 'Sim'
>>> resposta.lower()
'sim'
>>> resposta.upper()
'SIM'
>>> resposta.lower() in 'sim não yes no'
True
>>> resposta.lower() in 'não yes no'
False
>>> resposta.lower() in ' SIM não yes no'
False
>>>

#find and replace
>>> s = 'um tigre, dois tigres, três tigres'
>>> s.find('t')
3
>>> s.find('tigre')
3
>>> s.find('igre')
4
>>> s.find('dois')
10
>>> s.find('dois', 4)
10
>>> s.find('dois', 16)
-1
>>> s.find('dois', 11)
-1
>>> s.find('dois', 10)
10
>>> s.find('dois', 9)
10
>>> s
'um tigre, dois tigres, três tigres'
>>> s.replace('tigre', 'gato')
'um gato, dois gatos, três gatos'
>>> s
'um tigre, dois tigres, três tigres'
>>> s = s.replace('tigre', 'gato')
>>> s
'um gato, dois gatos, três gatos'
>>>

#split = separa
#join = gruda
>>> txt = 'batatinha quando nasce'
>>> txt.split()
['batatinha', 'quando', 'nasce']
>>> txt = 'batatinha/quando/nasce'
>>> txt.split()
['batatinha/quando/nasce']
>>> txt.split('/')
['batatinha', 'quando', 'nasce']
>>> txt
'batatinha/quando/nasce'
>>> txt = 'batatinha quando nasce'
>>> txt = txt.split()
>>> txt
['batatinha', 'quando', 'nasce']
>>> data = '28/03/1990'
>>> data.split(/)
SyntaxError: invalid syntax
>>> data.split('/')
['28', '03', '1990']
>>> data
'28/03/1990'
>>> 
#split = separa
#join = gruda
times = ['Palmeiras', 'São Paulo', 'Corintians']
>>> '/'.join(times)
'Palmeiras/São Paulo/Corintians'

data = int(print('Informe sua data de nacimento: '))
data.find('/')
data.replace('/', 'de março de')
print(data)
if mes == 01:
    mes.replace('/', 'de janeiro de')

dia, mes, ano = input('Data (dd/mm/aaaa): ').split('/')
meses = ['jan', 'fev', 'março', 'abr',
         'mai', 'jun', 'jul', 'ago',
         'set', 'out', 'nov', 'dez']
print('Você nasceu em: ')
print('%s de %s de %s' %(dia, meses[int(mes) -1], ano))

#1
nota = float(input('Entre com uma nota: '))
while nota < 0 or nota > 10:
    print('Nota Inválida!')
    nota = float(input('Entre com uma nota: '))
if nota >= 0 and nota <= 10:
    print('Nota: %.2f' %nota)

#2
nome = input('Usuário: ')
senha = input('Senha: ')
while senha == nome:
    print('Senha Inválida!')
    senha = input('Senha: ')
if senha != nome:
    print('Seja bem-vindo, %s' %nome)

#3
a = 80000
b = 200000
anos = 0
while a < b:
    a += a * 3/100
    b += b * 1.5/100
    anos += 1
print('Levará %d anos para terem a mesma quantidade de habitantes' %anos)


#4
n = int(input('Entre com um número: '))
a, b = 1, 1
cont = 1
while cont <= n - 2:
    a, b = b, a + b
    cont += 1 
print('Fibo(%d) = %d' %(n, b))
'''
#5
n1 = int(input('Entre com um número: '))
n2 = int(input('Entre com outro número: '))
while n1 % n2 != 0:
    n1, n2 = n2, n1 % n2
print('MDC = %d' %n2)







