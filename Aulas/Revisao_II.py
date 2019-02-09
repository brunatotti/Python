'''
#Condição
#faço a pergunta usando o IF
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
if a > b:
    print('O primeiro número é maior.')
if b > a:
    print('O segundo número é maior.')


#Sempre lembrar dos : e da identação
#irá imprimir a condição que for verdade
idade = int(input('Idade do carro: '))
if idade > 3:
    print('O carro é velho!')
else:
    print('O carro é novo!')

velocidade = int(input('Qual a velocidade? '))
if velocidade > 110:
    print('Você foi multado!')
    multa = (velocidade - 110) * 5
    print('Valor da multa: R$%.2f' %multa)
else:
    print('Velocidade dentro do limite permitido!')

#toda vez que vc for programar é interessante que antes vc
#pegue um papel e tente colocar a lógica básica de programacao
#antes de codificar.
#É importante SEMPRE testar
#if ou else... é como se uma fosse true e a outra false
minutos = int(input('Quantos minutos você usou este mês? '))
if minutos < 200:
    preco = minutos * 0.20
elif minutos >= 200 and minutos <= 400:
    preco = minutos * 0.18
elif minutos > 400 and minutos < 800:
    preco = minutos * 0.15
elif minutos >= 800:
    preco = minutos * 0.08
    
print('Valor da conta: R$%.2f' %preco)

#REPETIÇÕES#
#Looping
x = 1
print(x)
x = x + 1
print(x)
x = x + 1
print(x)

#melhor forma:
x = 1
while x <= 3:
    print(x)
    x = x + 1

#EXEMPLO#
numero = int(input('Entre com um número: '))
x = 1
while x <= numero:
    print(x)
    x = x + 1

#EXEMPLO com WHILE#
numero = int(input('Entre com um número: '))
x = 0
while x <= numero:
    print(x)
    x = x + 2    

#EXEMPLO com IF#
numero = int(input('Entre com um número: '))
x = 0
while x <= numero:
    if x % 2 == 0:
        print(x)
    x = x + 2    

#
numero = int(input('Entre com um número: '))
x = 1
while x <= numero:
    print(x)
    x = x + 2 

#Contador é uma variavel que eu somo valores constante
#Nos acumuladores os valores sao variaveis. 

#
numero = 1
soma = 0
while numero <= 10:
    x = int(input('Digite o %d numero: ' %numero))
    soma = soma + x
    numero = numero + 1
print('Soma: %d' %soma)

#Soma
cont = 1
soma = 0
while cont <= 5:
    valor = int(input('Valor %d: ' %cont))
    cont = cont + 1
    soma = soma + valor
print('Soma: %d' %soma)

#media
cont = 1
media = 0
while cont <= 5:
    nota = int(input('Valor %d: ' %cont))
    media = media + nota
    cont = cont + 1
print('Média: %.2f' %(media/5))

cont = 1
fat = 1
while cont <= 10:
    fat = fat * cont
    cont = cont + 1
print('Fat(10) = %d' %fat)

#Fatorial
n = int(input('Entre com um número: '))
cont = 1
fat = 1
while cont <= n:
    fat = fat * cont
    cont = cont + 1
print('Fat(%d) = %d' %(n, fat))


#EXEMPLO#
soma = 0
while True:
    x = int(input('Digite um número(0 sai): '))
    if x == 0:
        break
    soma = soma + x
print('Soma: %d' %soma)

#Tabuada
tabuada = 1
while tabuada <= 10:
    n = 1
    print('Tabuada %d' %tabuada)
    while n <= 10:
        print('%d X %d = %d' %(tabuada, n, tabuada * n))
        n = n + 1
    tabuada = tabuada + 1

#1
a = int(input('Entre com um dos lados do triângulo: '))
b = int(input('Outro lado: '))
c = int(input('Outro lado: '))
if a > b + c or b > a + c or c > a + b: 
    print('Não é um triângulo!')
elif a == b == c:
    print('É um triângulo equilátero!')
elif a != b != c:
    print('É um triângulo escaleno!')
elif a == b or b == c or c == a:
    print('É um triângulo isósceles!')


#2
ano = int(input('Entre com o ano: '))
if ano % 100 != 0 and ano % 4 == 0 or ano % 400 == 0:
    print('É bissexto!')
else:
    print('Não é bissexto!')

#3
peso = int(input('Quantos quilos você pescou?: '))
if peso <= 50:
    print('Peso ok!')
if peso > 50:
    multa = (peso - 50) * 4
    peso = peso - 50
    print('Peso excedente: %d kilos' %peso)
    print('Multa: R$ %.2f' %multa)

#4
n1 = int(input('Entre com um número: '))
n2 = int(input('Outro número: '))
n3 = int(input('Outro número: '))
if n1 > n2 and n1 > n3:
    print('%d foi o maior número digitado!' %n1)
elif n2 > n1 and n2 > n3:
    print('%d foi o maior número digitado!' %n2)
else:
    print('%d foi o maior número digitado!' %n3)

#5
n1 = int(input('Entre com um número: '))
n2 = int(input('Outro número: '))
n3 = int(input('Outro número: '))
if n1 > n2 and n1 > n3:
    print('%d foi o maior número digitado!' %n1)
elif n2 > n1 and n2 > n3:
    print('%d foi o maior número digitado!' %n2)
else:
    print('%d foi o maior número digitado!' %n3)
if n1 < n2 and n1 < n3:
    print('%d foi o menor número digitado!' %n1)
elif n2 < n1 and n2 < n3:
    print('%d foi o menor número digitado!' %n2)
else:
    print('%d foi o menor número digitado!' %n3)

#6
hora = float(input('Salário hora: '))
trabalhadas = int(input('Horas trabalhados no mês: '))
bruto = hora * trabalhadas
ir = bruto * 11/100
inss = bruto * 8/100
sindicato = bruto * 5/100
liquido = bruto - ir - inss - sindicato
print('+Salário Bruto: %.2f' %bruto)
print('-IR: %.2f' %ir)
print('-INSS: %.2f' %inss)
print('-Sindicato: %.2f' %sindicato)
print('=Salário Líquido: %.2f' %liquido)
'''
#7
metros = float(input('Área a ser pintada: '))
litros = metros / 3
latas = round(litros / 18)
print('Serão usadas %d latas para pintar %.2f metros2' %(latas, metros))
print('Valor gasto:', (latas * 80))








            
    
    
