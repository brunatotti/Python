#1 Faça um programa que peça dois números inteiros e
#imprima a soma desses dois números
n1 = int(input('n1: '))
n2 = int(input('n2: '))
soma = n1 + n2
print('A soma é: ', soma )

#2 Escreva um programa que leia um valor em metros e
#o exiba convertido em milímetros
metros = float(input('Metros: '))
milimetros = metros * 1000
print(milimetros)

#3 Escreva um programa que leia a quantidade de dias,
#horas, minutos e segundos do usuário.
#Calcule o total em segundos.
dias = int(input('Dias: '))
horas = int(input('Horas: '))
minutos = int(input('Minutos: '))
segundos = int(input('Segundos: '))
total = dias * (60 * 60 * 24) + horas * (60 * 60) +  minutos * 60 + segundos
print(total)

#4 Faça um programa que calcule o aumento de um salário.
#Ele deve solicitar o valor do salário e a porcentagem
#do aumento. Exiba o valor do aumento e do novo salário.
atual = float(input('Salário Atual: '))
porcentagem = float(input('Porcentagem do Aumento: '))
aumento = atual + (atual / 100 * porcentagem)
print(aumento)

#5 Solicite o preço de uma mercadoria e o percentual de desconto.
#Exiba o valor do desconto e o preço a pagar.
mercadoria = float(input('Mercadoria: '))
desconto = float(input('Porcentagem do desconto: '))
desconto = mercadoria/100 * desconto
mercadoria = mercadoria - (mercadoria/100 * desconto)
print('Desconto: 'desconto)
print('Preço Final: 'mercadoria)

#6 Calcule o tempo de uma viagem de carro. Pergunte a distância
#a percorrer e a velocidade média esperada para a viagem.
distancia = float(input('Distancia (km): '))
velocidade = int(input('Velocidade média: '))
tempo = distancia / velocidade
print('Tempo médio: ', tempo)

#7 Converta uma temperatura digitada em Celsius para Fahrenheit.
#F = 9*C/5 + 32
c = float(input('Celsius: '))
f = 9 * c / 5 + 32
print('Fahrenheit: ', f)

#8 Faça agora o contrário, de Fahrenheit para Celsius.
# 9 * 36 / 5 + 32
# f / 9    * 5 + 32
f = float(input('Fahrenheit: '))
c = (f - 32) / 1.8
print('Celsius: ', c)

#9 Escreva um programa que pergunte a quantidade de km percorridos
#por um carro alugado pelo usuário, assim como a quantidade de dias
#pelos quais o carro foi alugado. Calcule o preço a pagar,
#sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.
km = float(input('Km percorrido: '))
dias = int(input('Diárias: '))
total = km * 0.15 + dias * 60
print('Total a pagar: ', total)

#10 Escreva um programa para calcular a redução do tempo de vida de
#um fumante. Pergunte a quantidade de cigarros fumados por dia e
#quantos anos ele já fumou. Considere que um fumante perde 10 minutos
#de vida a cada cigarro, calcule quantos dias de vida um fumante perderá.
#Exiba o total de dias.
cigarros = int(input('Quantidade de Cigarros por dia: '))
anos = float(input('Quantos anos já fumou? '))
perdeu = (anos * 365 * cigarros) / 144
print('Já perdeu: %.2f dias de vida.' %perdeu)

#11 Sabendo que str( ) converte valores numéricos para string,
#calcule quantos dígitos há em 2 elevado a um milhão.
elevado = str(2 ** 1000000)
print(len(elevado))
















