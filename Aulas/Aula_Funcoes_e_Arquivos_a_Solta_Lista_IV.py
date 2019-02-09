'''
#1 com WHILE
texto = 'aeiou'
k = 0
while k < len(texto):
    letra = texto[k]
    print(letra)
    k += 1

#1 com FOR (mesma coisa)
for letra in 'aeiou':
    print(letra)

#2 com WHILE
lista = list(range(5))
k = 0
while k < len(lista):
    i = lista[k]
    print(i)
    k += 1

#2 com FOR
for i in range(5):
    print(i)

#3 com WHILE
lista = ['bruna', 42, 3.14]
k = 0
while k < len(lista):
    x = lista[k]
    print(x)
    k += 1
#3 com FOR
for x in ['bruna', 42, 3.14]:
    print(x)

#para não repitir codigo eu uso funcoes
#funcoes sao pequenos blocos de cod que eu tenho uma entrada e uma said
#algumas funcoes:
#len entrada o texto e saida o tamamho do texto
#int texto 42 e saida numero 42
#print entrada alguma coisa que e imprimo e nao tem saida    
#input entra o prompt e saida o que a pessoa digitou

#para definir minhas propriar funcoes eu utilizo o DEF
#para devolver uso o RETURN

#existe funcao que nao retorna nada (print)
   
def épar(x):
    return x%2 == 0
#preciso chamar pra executar
#com as funcoes nao preciso ficar dando f5 toda hora/ Só chamar a funcao

def fat(n):
    f = 1
    while n > 0:
        f = f * n
        n = n - 1
    return f
#colocar no shell:
for i in range(5):
    print(fat(i))
'''
#dois zé diferente
a = 5
def muda_e_imprime():
    a = 7
    print('a dentro da funcao: %d' %a)
print('a antes de mudar: %d' %a)
muda_e_imprime()
print('a depois de mudar: %d' %a)

# com global eles serao o mesmo zé
a = 5
def muda_e_imprime():
    global a
    a = 7
    print('a dentro da funcao: %d' %a)
print('a antes de mudar: %d' %a)
muda_e_imprime()
print('a depois de mudar: %d' %a)

