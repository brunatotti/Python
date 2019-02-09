'''
#
nome = input('Qual seu nome?: ')
print('Seja bem-vindo(a), %s! Prazer em te conhecer!' %nome)

#
dia = int(input('Dia do nascimento: '))
mês = input('Mês do nascimento: ')
ano = int(input('Ano do nascimento: '))
print('Data do nascimentto: %d de %s de %d' %(dia, mês, ano))

#
n1 = int(input('Número 1: '))
n2 = int(input('Número 2: '))
soma = n1 + n2
print('A soma entre {0} e {1} é: {2}'.format(n1, n2, soma))
'''
# 004
n = input('Entre com um número: ')
print(type(n))
print(n.isnumeric())
print(n.isupper())
print(n.isalnum())
print(n.isalpha())