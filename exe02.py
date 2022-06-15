#2) Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma,
# a multiplicação e os números.

lista = []
mult = 1

print()
for numeros in range(1, 6):
    num = int(input('Digite o {}º número: '.format(numeros)))
    lista.append(num)
    mult = mult * num
soma = sum(lista)

print('\nOs vetores são: {}\nA soma dos vetores é: {}\nA multiplicação dos vetores é: {}'.format(lista, soma, mult))

