'''
f = open('teste.txt', 'w')
f = open('teste.txt', 'w')
>>> f.write('Olá Mundo!')
10
>>> f.close()
>>> f = open('teste.txt', 'r')
>>> linha = f.read()
>>> print(linha)
Olá Mundo!
>>> f.close()
>>> print(linha)
Olá Mundo!


f = open('linha.txt', 'w')
for k in range (1, 101):
    f.write(str(k)+'\n')
f.close()

f = open('linha.txt', 'r')
for linha in f:
    print(linha.strip())
    #antes pulava duas vezes, pois era
    #um \n do arquivo e outro pula linha do print
f.close()

with open ('linhas.txt') as f:
    print (f.read())
'''
