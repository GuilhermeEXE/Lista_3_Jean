#13) Faça um programa para imprimir:
#1
#1 2
#1 2 3
#.....
# 2 3 ... n
#para um n informado pelo usuário. Use uma função que receba um valor n inteiro
#imprima até a nésima linha.

def num(n):
    for i in range(n):
        i += 1
        print(str(i) * i)

n = int(input('Digite um número: '))
num(n)