#1
print('Entre com sua nota:')
nota = float(input('Insira a nota: '))
while nota < 0 or nota > 10:
    print('Nota inválida!')
    nota = float(input('Digite a nota (entre 0 e 10): '))
print('Nota: %.2f' %nota)

#2
print('Usuário e Senha:')
nome = input('Usuário: ')
senha = input('Digite sua senha (diferente do usuário): ')
while senha == nome:
    print('Senha inválida')
    senha = input('Digite sua senha: ')
print('Seja bem-vindo(a), %s' %nome)

#3
print('País A X País B:')
a = 80000
b = 200000
anos = 0
while a < b:
    a += a * 3/100
    b += b * 1.5/100
    anos += 1
print('Levará %d anos para terem a mesma quantidade de habitantes' %anos)

#4
print('Sequencia de Fibonacci')
n = int(input('Digite um número: '))
a = 1
b = 1
cont = 1
while cont <= n - 2:
    a, b = b, a + b
    cont += 1
print('Fib(%d) = %d' %(n, b))

#5
print('Calcule o MDC')
n1 = int(input('Entre com um número: '))
n2 = int(input('Entre com outro número: '))
while n1 % n2 != 0:
    n1, n2 = n2, n1 % n2
print('MDC = %d' %n2)

