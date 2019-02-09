#1 Faça um Programa que peça os três lados de um triângulo.
#O programa deverá informar se os valores podem ser um triângulo.
#Indique, caso os lados formem um triângulo, se o mesmo é:
#equilátero, isósceles ou escaleno.
l1 = int(input('L1: '))
l2 = int(input('L2: '))
l3 = int(input('L3: '))
if l1 > l2 + l3 or l2 > l1 + l3 or l3 > l2 + l1:
    print('Não é um triângulo!')
elif l1 == l2 == l3:
    print('Triângulo Equilátero')
elif l1 == l2 != l3 or l2 == l3 != l1 or l1 == l3 != l2:
    print('Triângulo Isósceles')
else:
    print('Triângulo Escaleno')

#2 Determine se um ano é bissexto. Verifique no Google como fazer isso.
ano = int(input('Entre com o ano: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Ano Bissexto')
else:
    print('Não é bissexto!')

#3 João Papo-de-Pescador, homem de bem, comprou um microcomputador
#para controlar o rendimento diário de seu trabalho.
#Toda vez que ele traz um peso de peixes maior que o estabelecido
#pelo regulamento de pesca do estado de São Paulo (50 quilos)
#deve pagar uma multa de R$ 4,00 por quilo excedente.
#João precisa que você faça um programa que leia a variável peso
#(peso de peixes) e verifique se há excesso.
#Se houver, gravar na variável excesso e na variável multa o valor
#da multa que João deverá pagar. Caso contrário mostrar tais
#variáveis com o conteúdo ZERO.
pesca = float(input('Qtos kilos pescou? '))
if pesca > 50:
    pesca = pesca - 50
    multa = pesca * 4
    print('A multa é de: R$', multa)
else:
    print('Não paga multa!')

#4 Faça um Programa que leia três números e mostre o maior deles.
n1 = int(input('n1: '))
n2 = int(input('n2: '))
n3 = int(input('n3: '))
if n1 == n2 == n3:
    print('Todos são iguas!')
elif n1 > n2 and n1 > n3:
    print('%d é maior' %n1)
elif n2 > n1 and n2 > n3:
    print('%d é maior' %n2)
else:
    print('%d é maior' %n3)

#5 Faça um Programa que leia três números e mostre o maior e o menor deles.
n1 = int(input('n1: '))
n2 = int(input('n2: '))
n3 = int(input('n3: '))
if n1 == n2 == n3:
    print('Todos são iguas!')
elif n1 > n2 and n1 > n3:
    print('%d é maior' %n1)
elif n2 > n1 and n2 > n3:
    print('%d é maior' %n2)
else:
    print('%d é maior' %n3)
if n1 == n2 == n3:
    print('Todos são iguas!')    
elif n1 < n2 and n1 < n3:
    print('%d é menor' %n1)
elif n2 < n1 and n2 < n3:
    print('%d é menor' %n2)
else:
    print('%d é menor' %n3)

#6 Faça um Programa que pergunte quanto você ganha por hora e o
#número de horas trabalhadas no mês. Calcule e mostre o total do
#seu salário no referido mês, sabendo-se que são descontados 11%
#para o Imposto de Renda, 8% para o INSS e 5% para o sindicato,
#faça um programa que nos dê o salário bruto, quanto pagou ao INSS,
#quanto pagou ao sindicato e o salário líquido. Observe que
#Salário Bruto - Descontos = Salário Líquido. Calcule os descontos
#e o salário líquido, conforme a tabela abaixo:
#a. + Salário Bruto : R$
#b. - IR (11%) : R$
#c. - INSS (8%) : R$
#d. - Sindicato ( 5%) : R$
#e. = Salário Liquido : R$
hora = float(input('Quanto vc ganha por hora? '))
mes = int(input('Quantas horas vc tarabalha por mes? '))
bruto = hora * 8 * mes
print(bruto)
ir = bruto / 100 * 11
print(ir)
inss = bruto / 100 * 8
print(inss)
sind = bruto / 100 * 5
print(sind)
liquido = bruto - ir - inss - sind
print(liquido)

#Faça um programa para uma loja de tintas. O programa deverá
#pedir o tamanho em metros quadrados da área a ser pintada.
#Considere que a cobertura da tinta é de 1 litro para cada
#3 metros quadrados e que a tinta é vendida em latas de 18 litros,
#que custam R$ 80,00. Informe ao usuário a quantidades de latas de
#tinta a serem compradas e o preço total. Obs. : somente são vendidos
#um número inteiro de latas.
import math
metros = float(input('Quantos metros quadrados irá pintar? '))
litros = metros / 3
latas = math.ceil(litros / 18)
preco = latas * 80
print('Latas: ', latas)
print('Preco: ', preco)











