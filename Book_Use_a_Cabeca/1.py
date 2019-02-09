#1
a = int(input('Digite um número: '))
if a == 5:
    print('You are good!')
else:
    print ('Maybe next time!')

#2
a = int(input('Digite um número: '))
if a == 5:
    print('You are good!')
elif a > 5:
    print('É menor que este número!')
else:
    print('É maior que este número!')  
    
#2b
a = int(input('Digite um número: '))
if a == 5:
    print('You are good!')
else:
    if a > 5:
        print('É menor que este número!')
    else:
        print('É maior que este número!')
print('The end!')

#3
a = 0
while a != 5:
    a = int(input('Digite um número: '))
    if a == 5:
        print('You are good!')
    else:
        if a > 5:
            print('É menor que este número!')
        else:
            print('É maior que este número!')
print('The end!')

#4
from random import randint
a = 0
b = randint(1,10)
while a != b:
    a = int(input('Digite um número: '))
    if a == b:
        print('You are good!')
    else:
        print('Try again!')
print('The end!')







