#1 - Triângulo
print('Verifique se é um triângulo e qual triângulo é:')
a = int(input('Insira a medida de um dos lados do triângulo: '))
b = int(input('Do outro lado: '))
c = int(input('Do outro lado: '))
if a > b + c or b > a + c or c > a + b:
    print('Isso não é um triângulo! Um dos lados é maior que a soma dos outros dois lados.')
elif a == b == c:
    print('É um triângulo equilátero!')
elif (a == b or a == c or b == c) and (a != b or a!= c or b != c):
    print('É um triângulo isósceles')
elif a != b and a != c and b != a:
    print ('É um triângulo escaleno')


#2 - Ano Bissexto
print('Verifique se é um ano bissexto:')    
a = int(input('Informe o ano: '))
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print ('É bissexto!')
else:
    print('Este ano não é bissexto!')


#3 - Multa Pescador
print('Verifique se pagará multa:')    
pesca = float(input('Quantos kilos você pescou? '))
if pesca > 50:
    excesso = pesca - 50
    print('Multa de: ', (pesca - 50) * 4)
    print('O Excesso é de: %.2f kilo(s)' %excesso)
else:
    print('Não pagará multa!')


#4 - Maior Número
print('Insira os números abaixo')
a = int(input('Número 1: '))
b = int(input('Número 2: '))
c = int(input('Número 3: '))
if a >= b and a >= c:
    print('O maior é %d' %a)
elif b >= a and b >= c:
    print('O maior é %d' %b)
else:
    print('O maior é %d' %c)


#5 - Menor e Maior Número
print('Insira os números abaixo:') 
a= int(input('Número 1: '))
b = int(input('Número 2: '))
c = int(input('Número 3: '))
if a >= b and a >= c:
    print('O maior é %d' %a)
elif b >= a and b >= c:
    print('O maior é %d' %b)
else:
    print('O maior é %d' %c)
    
if a <= b and a <= c:
    print('O menor é %d' %a)
elif b <= a and b <= c:
    print('O menor é %d' %b) 
else:
    print('O menor é %d' %c)


#6 - Salário Líquido
print('Consulte seu salário final:')
ganha = float(input('Quanto você ganha por hora? '))
horas = int(input('Quantas horas você trabalha por dia? '))
trabalha = int(input('Quantos dias você trabalha por mês? '))
bruto = ganha * horas * trabalha
print('+Salário Bruto:\t\t R$ %.2f' %bruto)
ir = bruto * 11/100
print('-IR:\t\t\t R$ %.2f' %ir)
inss = bruto * 8/100
print('-INSS:\t\t\t R$ %.2f' %inss)
sindicato = bruto * 5/100
print('-Sindicato:\t\t R$ %.2f' %sindicato)
liquido = bruto - ir - inss - sindicato
print('=Salário Líquido:\t R$ %.2f' %liquido)



#7 - Latas de Tinta
print('Verifique quantas latas de tinta serão necessárias:')
area = float(input('Quantos metros quadrados serão pintados? '))
litros = area / 3
print('Serão necessários: %.2f litros de tinta' %litros)
latas = round(litros / 18)
print('Serão necessárias: %.2f latas de tinta' %latas)

