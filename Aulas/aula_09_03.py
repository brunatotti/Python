'''
#int - 
#float
#bool
#str
#coloca dir('texto')para ver todo o PODER do texto
#help('texto'.lower) - para buscar o que este comando faz
#'Texto'.lower()

#lista
edificio = ['Família Totti',
            'Família Oliveira',
            'Família Tito',
            'Família Alves']
print(edificio [0])
print(edificio [1])
print(edificio [2])
print(edificio [3])


#'Família Totti' in edificio
#edificio.sort()
#edificio

notas = [6, 7 , 5, 8, 9]
soma = 0
x = 0
while x < 5:
    soma += notas[x]
    x += 1
print('Média: %.2f' %(soma/x))
#x += 1 é o mesmo que x = x + 1

vetor = []
i = 1
while i <= 5:
    n = int(input('Digite um número: '))
    vetor.append(n)
    i = i + 1
print ('Vetor lido:', vetor)
'''
#append inclui no final
notas = []
i = 1
while i <= 4:
    n = float(input('Nota: '))
    notas.append(n)
    i += 1
soma = 0
i = 0
while i <=3:
    soma += notas[i]
    i += 1
print ('Notas: ', notas)
print ('Média: %.2f' %(soma /4))
