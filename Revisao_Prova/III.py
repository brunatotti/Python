#1 Faça um programa que peça uma nota, entre zero e dez.
#Mostre uma mensagem caso o valor seja inválido e continue
#pedindo até que o usuário informe um valor válido.
nota = int(input('Entre com uma nota: '))
while nota < 0 or nota > 10:
    print('Nota inválida!')
    nota = int(input('Entre com uma nota: '))
print('OK!')

#2 Faça um programa que leia um nome de usuário e a sua
#senha e não aceite a senha igual ao nome do usuário,
#mostrando uma mensagem de erro e voltando a pedir as informações.
nome = input('Seu nome: ')
senha = input('Senha: ')
if senha == nome:
    print('Senha inválida!')
    senha = input('Senha: ')
print('Seja bem-vindo(a)!')

#3 Supondo que a população de um país A seja da ordem de 80000
#habitantes com uma taxa anual de crescimento de 3% e que a
#população de B seja 200000 habitantes com uma taxa de
#crescimento de 1.5%. Faça um programa que calcule e escreva
#o número de anos necessários para que a população do país A
#ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento
a = 80000
b = 200000
anos = 0
while a < b:
    a = a + (a/100*3)
    b = b + (b/100*1.5)
    anos = anos +1
print('A: %.2f e B: %.2f' %(a, b))
print('Levará %.2f anos' %anos)

#4 A seqüência de Fibonacci é a seguinte:
#1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
#Sua regra de formação é simples: os dois primeiros
#elementos são 1; a partir de então, cada elemento é a
#soma dos dois anteriores. Faça um algoritmo que leia
#um número inteiro calcule o seu número de Fibonacci.
#F1 = 1, F2 = 1, F3 = 2, etc.
n = int(input('Posição Fibonacci: '))
a = 1
b = 1
cont = 1
while cont <= n - 2:
    a, b = b, a + b
    cont = cont + 1
print('F(%d) = %d'%(n, b))

#5 Dados dois números inteiros positivos, determinar
#o máximo divisor comum entre eles usando o algoritmo de Euclides.
n1 = int(input('n1: '))
n2 = int(input('n2: '))
while n1 % n2 != 0:
    n1, n2 = n2, n1 % n2
print('MDC: ', n2)

