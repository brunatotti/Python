def pot (x, n):
    if n <= 1:
        return x
    else:
        return x * pot(x, n-1)
        
print (pot (2,3))

