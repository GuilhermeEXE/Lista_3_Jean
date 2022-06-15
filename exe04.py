#4) Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos
#quadrados dos elementos do vetor.

vetorA = [ ]
s = 0
for numero in range(0, 10):
    vetorA.append(int(input("Digite um numero:")))
    s = s + (vetorA[len(vetorA)-1]**2)
print("A soma dos quadrados dos elementos do vetor é:" + str(s))