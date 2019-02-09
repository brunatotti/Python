print ('Bem vindo!')
g = input ('Chute um número: ')
chute = int(g)
if chute == 42:
    print ('Você venceu!')
else:
    print ('Você perdeu!')
print ('Fim do jogo!')

# roxo: é uma funcao que eu nao preciso definir
# verde: texto (nao é comando)
# laranja: diretivas da linguagem
# preto: são variáveis
# == é uma pergunta
# = atribuição

#TIPOS DE ERRO
#erro de sintaxe (identação e etc)... será resolvido com mta atencao e prática
#tempo de execução (colocar string em numero ou o contrário)
#semântico:

print ('Bem vindo!')
g = input ('Chute um número: ')
chute = int(g)
#erro semântico, pois 42 é uma string 
if chute == "42":
    print ('Você venceu!')
else:
    print ('Você perdeu!')
print ('Fim do jogo!')


#usar cliclo pomodoros (tomatinho) - 25 min 

#adivinhando numero 02

print ('Bem vindo!')
g = input ('Chute um número: ')
chute = int(g)
if chute == 42:
    print ('Você venceu!')
else:
    if chute > 42:
        print ('Alto')
    else:
        print ('Baixo')
print ('Fim do jogo!')


#adivinhando numero 03
#toda repeticao tem antes a inicializacao de uma variavel
#ex: chute = 0
#while chute != 42:














