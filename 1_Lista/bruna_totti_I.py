#1 - Somar Dois Números
print('Para somar dois números...')
primeiro = int(input('Digite o primeiro: '))
segundo = int(input('Digite o segundo: '))
print ('A soma dos dois números é:', (primeiro + segundo))


#2 - Metros para Milímetros
print('Converta METROS para MILÍMETROS: ')
metros = int(input('Quantos metros?: '))
milimetros = (metros * 1000)
print(metros, 'metro(s) tem', milimetros, 'milímetros.')


#3 - Quantos Segundos
print('Verifique quantos segundos há em...')
dias = int(input('Quantos Dias?: ' ))
horas = int(input('Quantas Horas?: ' ))
minutos = int(input('Quantos Minutos?: ' ))
segundos = int(input('Quantos Segundos: ' ))
total = (dias * 24 * 60 * 60) + (horas * 60 * 60) + (minutos * 60) + segundos
print(total)


#4 - Aumento de Salário
print('Teve um aumento? Veja qual será seu salário:')
salario = float(input('Salário atual?: '))
aumento = int(input('Qual é a porcentagem do aumento?: '))
salarioatual = salario + (salario * aumento/100)
print('O salário atual é:', salarioatual)


#5 - Valor do Desconto
print('Verifique o valor do desconto que você recebeu e o preço final do produto:')
mercadoria = float(input('Insira o valor do produto:' ))
desconto = float(input('Insira a porcentagem do desconto recebido:' ))
desconto = mercadoria * desconto/100
mercadoria = mercadoria - desconto
print('Seu desconto R$', desconto)
print('O valor do produto R$', mercadoria)


#6 - Tempo da Viagem
print('Veja quanto tempo em média durará sua viagem:')
distancia = float(input('Quantos kilometros irá percorrer? '))
velocidade = float(input('Qual é a velocidade esperada? (km/h) '))
tempo = distancia / velocidade
print('Você irá gastar %.1f hora(s) para essa viagem' %tempo)


#7 - Celsius 
print('Converta CELSIUS para FAHRENHEIT: ')
celsius = float(input('Digite a temperatura em Celsius: '))
fahrenheit = 9 * celsius / 5 + 32
print(celsius, 'é', fahrenheit, 'em Fahrenheit')


#8 - Fahrenheit
print('Converta FAHRENHEIT para CELSIUS: ')
fahrenheit = float(input('Digite a temperatura em Fahrenheit: '))
celsius = (fahrenheit - 32) * 5 / 9
print(fahrenheit, 'é', celsius, 'em Celsius')


#9 - Carro Alugado
print('Preencha as informações refente ao carro alugado:')
kilometros = float(input('Quantos kilometros foram rodados? '))
dias = int(input('Você ficou com o carro por quantos dias? '))
total = (kilometros * 0.15) + (dias *60)
print('O total a pagar é R$ %.2f' %total)


#10 - Cigarro
print('Veja quantos dias você já perdeu da vida por fumar:')
cigarros = int(input('Quantos cigarros você fuma por dia? '))
anos = float(input('Faz quantos anos que você fuma? '))
total = cigarros * (anos * 365)
perde = total / 144
print('Você já perde %.2f dias de vida' %perde)


#11 - Quantos digitos
print('Vamos verificar quantos digitos possuem em dois elevado a um milhão. Aguarde...')
a = str(2 ** 1000000)
print('Dois elevado a um milhão possue ', len(a), 'digitos')
