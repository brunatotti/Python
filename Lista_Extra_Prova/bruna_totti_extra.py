'''
a = 12.75
print (a - int(a), end = ' ')
a = int(a - int(a))*100
print (a)

a = 3
b = 4
a = a + b
b = a - b
a = a - b
print (a, b)

a = 'abacate'
print ('e' in a, 'x' in a, end = ' ')
print ('ate' in a, end = ' ')
print ('' in a, end = ' ')
print ('eta' in a, end = ' ')
print ('eta' not in a)



a = 11
if a > 10 and a % 6 == 3:
    print ('A', end = ' ')
elif a > 10 and a < 20:
    print ('B', end = ' ')
else:
    print ('C', end = ' ')
'''
repete = True
a=0
b=0
while repete:
    print ('O', end = ' ')
    if a + b > 24:
        repete = False
    a=a+5
    b=b+7
