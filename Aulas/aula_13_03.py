'''
#1
import re
p = re.compile(r'\d+')
d, m, a = p.findall('09-03-2018')

#2 - String = textos - Vários tipos
#aspas simples ou dupla ou tripla
#posso ter string com várias linhas

#colocar no shell:
x = '0123456789'
x[0]
x[4]
#vai do primeiro até o anterior ao segundo
x[2:6]
x[0:9]
x[4:5]
x[-2]
x[:3]
x[3:]
x
#contar qtos caracteres tem meu texto
len(x)
#encontrar texto
x.find('4')
#se eu colocar um texto que não existe, ele devolve -1
x.find('@')
#do 1 ao 8 de 2 em 2
x[1:9:2]
#do inicio ao final de 2 em 2
x[::2]
#ou de 3 em 3
x[::3]

#vai trazer o valor de x ao contrário
x[::-1]
#funciona do texto tbm
s= 'batatinha quando nasce'
s[::-1]

#1 - Soemnte palavra
palavra = input('Entre com uma palavra: ')
if palavra == palavra[::-1]:
    print(palavra, 'é palíndrome!')
else:
    print(palavra, 'não é palíndrome')

#2 - com frase. É um exemplo, mas aprenderemos melhor isso mais pra frente  
s = input('Frase: ')
palavras = s.lower().split()
frase = s
s = ''.join(palavras)
if s == s[::-1]:
    print(frase, 'é palíndrome!')
else:
    print(palavra, 'não é palíndrome')

#colocar no shell:
texto = 'Alô Mundo!'
#terá um novo texto:
texto = '@' + texto[1:]

#no shell
s = 'batatinha quando nasce'
len(s)
#para ler as letras:
s[0]
s[1]

#concatenação
palavra = input("Palavra: ")
k = 0
troca = ""
while k < len(palavra):
    if palavra[k] in "aeiou":
        troca = troca + "*"
    else:
        troca = troca + palavra[k]
    k += 1
print("Nova palavra %s" %troca)

'''


#modo interativo
arquivo = 'prog.py'
arquivo.startswith ('p')
arquivo.endswith ('py')
resposta = 'sim'
resposta.lower()
resposta.upper()
resposta.lower() in 'sim na yes no'


s = 'um tigre, dois tigres, trê tigres'
s.find('tigre', 0)
s.find('tigre', 4)
s.find('tigre', 16)
s.find('tigre', 28)
s.find('tigre', 29)
#trocar palavra por outra palavra
s.replace('tigre', 'gato')
#mas ainda nao gravou
s
#para gravar:
s = s.replace('tigre', 'gato')
#ai sim:
s

#split é uma forma de pegar coisa para depois tratar separadamente
d, m, a = '13/03/2018'.split('/')

#
d, m, a = input('dd/mm/aaaa: ').split('/')
print (f'{d}' de {meses [int(m)-1]}de (a) )


meses = '''janeiro fevereiro arço abril maio junho julho agosto setembro outubro novembro dezembro'''.split()































