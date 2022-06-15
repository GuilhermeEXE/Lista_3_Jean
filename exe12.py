#12) Faça um programa que leia as dimensões de duas matrizes A e B, e depois leia as duas matrizes (os
#elementos devem ser inteiros). Se as matrizes forem de tamanhos compatíveis para multiplicação,
#multiplique as matrizes. Imprima as matrizes A, B e a matriz resultante da multiplicação.

matriz1 = []
l=int(input('Numero de linhas:'))
c=int(input('Numero de colunas:') )
print('\n')
for i in range(l):
    linha = []
    for j in range(c):
        linha.append(int(input('Digite  o valor de [' + str(i) + ','  + str(j) + ']:')))
        matriz1.append(linha)
        print('\n')
        matriz2 = []
        l2=int(input('Numero de linhas: '))
        c2=int(input('Numero de colunas: ' ))
        print('\n')
        for k in range(l2):
            linha2 = []
            for p in range(c2):
                linha2.append(int(input('Digite o valor de ['+ str(k) +',' + str(p) + ']:')))
                matriz2.append(linha2)
                print('\n')
                print(matriz1)
                print(matriz2)
                print('\n')
                C=[]
                for k in range(l):
                    C.append([0]*l)
                    for i in range(l):
                        C[k][i] = 0
                        if   l==c2:
                            for i in range (l):
                                for j in range (l):
                                    for k in  range (c):
                                        C[i][j]  =  C[i][j] + (matriz1[i][k] * matriz2[k][j])
                                        print(' resultado é ', C)
                                    else:
                                        print("Impossível a multiplicaçã o de matriz")