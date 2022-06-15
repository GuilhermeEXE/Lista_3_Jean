#15) Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de
#caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

def pn(n):
    if n > 0:
        print('positivo')
    elif n == 0:
        print('nulo')
    else:
        print('negativo')
n = int(input('digite um número: '))
print('O número é', end=' ')
pn(n)