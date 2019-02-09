#1
print('EXERCÍCIO 1')
import random
lista = []
for x in range(1,11):
    x = random.randint(1,100)
    if x not in lista:
        lista.append(x)
lista.sort()
menor = lista[0]
maior = lista[9]
print(lista)
print('Menor: {0}'.format(menor))
print('Maior: {0}'.format(maior))

#2
print('EXERCÍCIO 2')
import random
lista = []
even = []
odd = []
for x in range(1,21):
    x = random.randint(1,100)
    lista.append(x)
    if x % 2 == 0:
        even.append(x)
    else:
        odd.append(x)
lista.sort()
even.sort()
odd.sort()
print('Números das duas listas: {0}'.format(lista))
print('Lista com os números pares: {0}'.format(even))
print('Lista com os números ímpares: {0}'.format(odd))

#3
print('EXERCÍCIO 3')
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

#4
print('EXERCÍCIO 4')
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


#5
print('EXERCÍCIO 5')
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
