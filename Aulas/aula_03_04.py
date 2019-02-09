import 
texto = texto.replace('.', ' ')
texto = texto.replace(',', ' ')
texto = texto.replace(':', ' ')
texto = texto.lower()

def alguma_letra_em_python(s):
    for x in s:
        if x in 'python':
            return True
        return False 
texto = texto.split()
cont = 0
python = []
for p in texto:
    if alguma_letra_em_python(p) and len(p) > 4:
        cont += 1
        python.append(p)
    python.sort()
    print(python)
    print(cont)
