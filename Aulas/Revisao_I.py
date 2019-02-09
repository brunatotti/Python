'''
#Sei que é texto quando coloco aspas no início e no final
#print sempre com caixa baixa
print('Olá Mundo!')
#matemática
2 + 3
2 * 4
#para elevar um número
2 ** 10
#tipo numero inteiro
42
#tipo numero flutuante
3.14
#tipo texto
'Hey'
#para declarar variáveis
a = 234
b = 'bruna'
c = 3.14
#Posso manipular variáveis
a = 5 * a
#ou atribuir uma nova variável
c = 45 + a

#EXEMPLO#
a = 3
b = 10
print(a + b)

#poderia ser com texto tbm
a = 'abacate'
b = ' e banana'
print(a + b)
#para saber o que vc pode fazer com alguma coisa
dir('abacate')
#para saber o que aquele método faz
help('abacate'.upper)
#comparar duas variáveis
a = 4
b = 3
a > 4
#No caso de cima irá retornar True or False
#um igual é uma atribuição. Dois igual é uma comparacao

#EXEMPLO#
nota = 7
faltas = 30
nota >= 6 and faltas <= 20
#Retornará True ou False

#Para imprimir texto com número
a = 28
print('Faço', a, 'anos este mês')
#ou
print('Faço %d anos este mês' %a)
#%d decimais
#%s string
#%f flutuante
#%.2f o 2 representa quantas casas depois da vírgula eu quero

#variável fortemente tipada
a = 42
a = 'abacate'
a = 56
a + 'mamão'
#Não consigo somar um texto com um número.
#Preciso transformar o número em string para isso.
str(42) + ' mamão'

#para trocar o valor de variaveis
a, b = b, a

#ou atribuir variáveis
a, b, c = 3, 6, 9

#ou com texto
a, b, c = 'HEY'
#neste caso, a = 'H', b = 'E', c = 'Y'


#Exemplo#
divida = 0
compra = 42
divida = divida + compra
compra = 300
divida = divida + compra
compra = 34
divida = divida + compra
print (divida)


#Para ler texto
nome = input('Digite seu nome')
#o input é natualmente texto. Pra transformar para numero decimal:
n1 = int(input('Digite um número: '))
#para numero flutuante
n1 = float(input('Digite um número: '))

#EXEMPLO#
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
print(n1 + n2)

#para calcular digitos, usar len
nome = 'bruna'
print(len(nome))
#len só conta texto. Para contar numero, tem que transformar
a = str(2 ** 100)

#EXERCICIOS#
a = str(2 ** 100)
print(len(a))

#1
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
print(n1 + n2)

#2
metros = int(input('Quantos metros?: '))
milimetros = metros * 1000
print(milimetros)

#3
d = int(input('Dia:'))
h = int(input('Hora:'))
m = int(input('Mês:'))
s = int(input('Segundo:'))
segundos = d * 60 * 60 * 24 + h * 60 * 60 + m * 60 + s
print(segundos)

#4
salario = float(input('Qual é seu salário?: '))
aumento = float(input('Qual foi a porcentagem do aumento?: '))
print(salario * aumento/100)
print(salario + (salario * aumento/100))

#5
mercadoria = float(input('Preço: '))
desconto = int(input('Porcentagem de desconto: '))
print(mercadoria * desconto/100)
print(mercadoria - (mercadoria * desconto/100))

#6
distancia = int(input('Distancia em km: '))
velocidademedia = int(input('Velocidade média: '))
tempoviagem = distancia / velocidademedia
print('Levará em média %d horas' %tempoviagem)

#7
c = float(input('Celsius: '))
f = c * 1.8 + 32
print('São %.2f Fahrenheit' %f)

#8
f = float(input('Fahrenheit: '))
c = (f - 32) / 1.8
print('São %.2f Celsius' %c)

#9
km = int(input('Km percorridos: '))
dias = int(input('Quantidade de diárias: '))
total = (km * 0.15) + (dias * 60)
print('Valor a pagar: ', total)


#10
cigarros = int(input('Quantos cigarros por dia? '))
anos = int(input('Quantos anos você fuma? '))
diasperdidos = (cigarros * 365) * anos / 144
print('Por fumar, vc deixará de viver %.2f dias de vida' %diasperdidos)
'''
#11
print('Estamos calculando quantos caractéres existem em dois elevado a um milhão.')
print('AGUARDE...')
a = str(2 ** 1000000)
print('Existem', len(a), 'caractéres')
























