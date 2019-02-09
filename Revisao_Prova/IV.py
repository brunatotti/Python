#1 Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra
#o maior e o menor valor, sem usar as funções max e min.
import random
lista = []
for x in range(1,11):
    x = random.randint(1,100)
    if x not in lista:
        lista.append(x)
    lista.sort()
menor = lista[0]
maior = lista[8]
print (lista)
print('Menor: {0}'.format(menor))
print('Maior: {0}'.format(maior))

#2 Sorteie 20 inteiros entre 1 e 100 numa lista. Armazene os números
# pares na lista PAR e os números ímpares na lista IMPAR. Imprima
# as três listas.
import random
par = []
impar = []
for x in range(1,21):
    x = random.randint(1,100)
    if x not in lista:
        if x % 2 == 0:
            par.append(x)
        else:
            impar.append(x)
lista = par + impar
lista.sort()
par.sort()
impar.sort()
print(lista)
print(par)
print(impar)

#3 Faça um programa que crie dois vetores com 10 elementos aleatórios
# entre 1 e 100. Gere um terceiro vetor de 20 elementos,
# cujos valores deverão ser compostos pelos elementos intercalados
# dos dois outros vetores. Imprima os três vetores.
print('#3')
import random
v1 = []
v2 = []
lista = []
for x in range(1,11):
    x = random.randint(1,100)
    v1.append(x)
for x in range(1,11):
    x = random.randint(1,100)
    v2.append(x)
print(v1)
print(v2)
for x in zip(v1, v2):
    lista.extend(list(x))
print(lista)

#4 Seja o statement sobre diversidade:
# “The Python Software Foundation and the global Python community
# welcome and encourage participation by everyone. Our community is
# based on mutual respect, tolerance, and encouragement, and we are
# working to help each other live up to these principles. We want our
# community to be more diverse: whoever you are, and whatever your
# background, we welcome you.”.
# Gere uma lista de palavras deste texto
# com split(), a seguir crie uma lista com as palavras que começam ou
# terminam com uma das letras “python”. Imprima a lista resultante.
# Não se esqueça de remover antes os caracteres especiais e cuidado
# com maiúsculas e minúsculas.
texto = '''The Python Software Foundation and the global
   Python community  welcome and encourage participation
   by everyone. Our community is based on mutual respect,
   tolerance, and encouragement, and we are working to
   help each other live up to these principles. We want
   our community to be more diverse: whoever you are, and
   whatever your background, we welcome you.'''.lower()
import string
for x in string.punctuation:
    texto = texto.replace(x, ' ')
lista = []
for z in texto.split():
  if z[0] in 'python' or z[-1] in 'python':
    lista.append(z)
print(lista)

#5 Seja o mesmo texto acima “splitado”. Calcule quantas palavras
# possuem uma das letras “python” e que tenham mais de 4 caracteres.
# Não se esqueça de transformar maiúsculas para minúsculas e de remover
# antes os caracteres especiais.
texto = '''The Python Software Foundation and the global
   Python community  welcome and encourage participation
   by everyone. Our community is based on mutual respect,
   tolerance, and encouragement, and we are working to
   help each other live up to these principles. We want
   our community to be more diverse: whoever you are, and
   whatever your background, we welcome you.'''.lower()
import string
for x in string.punctuation:
    texto = texto.replace(x, ' ')
def letras(x):
  for c in x:
    if c in 'python':
      return True
  return False

lista = [p for p in texto.split() if letras(p) and len(p) > 4]
print (lista)
print (len(lista))






