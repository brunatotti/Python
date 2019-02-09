cont = 0
for b in range(18644, 33088):
  if '2' in str(b) and '7' not in str(b):
    cont += 1
print (cont)

cont = 0
for i in range(1,10):
    if i != 3:
        for j in range(1,7):
            print('oi')
            cont += 1
print(cont)
