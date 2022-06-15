#10) Faça um programa que leia uma matriz 3x3 de inteiros e multiplique os elementos da diagonal principal
#da matriz por um número k. Imprima a matriz na tela antes e depois da multiplicação.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(3):
    for j in range(3): matriz[i][j] = int(input(' Digite o elemento [' + str(i) + '] [' + str(j) + ']:'))
    print(matriz)
    print('\n')
    v = int(input('Digite um número para  multiplicar os elementos na diagonal principal:'))
    for i in range(3):
        for j in range(3):
            if i == j:
                matriz[i][j] = v * matriz[i][j]
                print(matriz)