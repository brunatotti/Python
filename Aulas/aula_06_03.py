'''
#1
x = 1
n = int(input('Insira um número: '))
while x <= n:
    print(x)
    x = x + 1
    
#2
a = int(input('Insira um número: '))
b = int(input('Insira um número maior do que o anterior: '))
while a <= b:
    print(a)
    a = a + 1

#3
x = 0
n = int(input('Insira um número: '))
while x <= n:
    print (x)
    x = x + 2

#4
x = 1
n = int(input('Insira um número: '))
while x <= n:
    print (x)
    x = x + 2

#4 outra forma
x = 1
n = int(input('Insira um número: '))
while x <= n:
    if x % 2 != 0:
        print (x)
    x = x + 1

#5
nota = int(input('Insira um número: '))
if nota > 10:
   while nota < 0 or nota > 10:
       print('Número inválido!')
       nota = int(input('Insira um número: '))
if nota <= 10:
    print('Nota:', nota)


#6
nome = input('Qual seu nome? ')
senha = input('Qual sua senha? ')
while senha == nome:
    print('Senha inválida!')
    senha = input('Digite uma nova senha? ')
if senha != nome:
    print('Senha criada com sucesso!')


#7 %d = numero inteiro
n = 1
soma = 0
while n <= 10:
    x = int(input('Digite o %d número: ' %n))
    soma = soma + x
    n = n + 1
print('Soma: %d' %soma)


#8
n = 1
soma = 0
while n <= 10:
    x = int(input('Digite o %d número: ' %n))
    soma = soma + x
    n = n + 1
print('Média: %.1f' %(soma/10))


#9
x = 1
f = 1
while x <= 10:
    f = f * x
    x = x + 1
print('Fat(10) = %d' %f)


#10
x = 1
f = 1
n = int(input('Digite o número: '))
while x <= n :
    f = f * x
    x = x + 1
print('Fat(%d) = %d' %(n, f))

#11
soma = 0
while True:
    x = int(input('Digite o número (0 sai)'))
    if x == 0:
        break
    soma = soma + x
    print ('Soma: %d' %soma)

#12
soma = 0
n = 0
while True:
    x = int(input('Digite o número (0 sai)'))
    if x == 0:
        break
    else:
        n = n + 1
    soma = soma + x
    print ('Média: %5.2f' %(soma/n))


#13
tabuada = 1
while tabuada <= 10:
    n = 1
    print ('Tabuada %d' %tabuada)
    while n <= 10:
        print('%d x %d = %d'
              %(tabuada, n, tabuada * n))
        n = n + 1
    tabuada = tabuada + 1
    
'''














