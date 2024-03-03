#Definindo a função
import math


def fatorial(n):

    if n == 0:
        return 1
    else:
        return n*fatorial(n-1)
    
valor = 4

print(f" O fatorial de {valor} e = {fatorial(valor)}")