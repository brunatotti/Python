minutos = int(input('Quantos minutos você usou?: '))
if minutos < 200:
    preco = 0.20
elif minutos < 400:
    preco = 0.18
elif minutos < 800:
    preco = 0.155
else:
    preco = 0.08

print(f'Conta: R$ {preco*minutos: .2f}')
    

