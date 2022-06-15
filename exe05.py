#5) Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20
#elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

listaA = [ ]
listaB = [ ]
listaC = [ ]

for i in range(10):
    print ('lista A:')
    listaA.append(input('Elemento:' + str(i+1) + '\n'))
for j in range(10):
    print ('lista B:')
    listaB.append(input('Elemento:' + str(i+1) + '\n'))
for m in range(10):
    listaC.append(listaA[m])
    listaC.append(listaB[m])

print(listaA)
print(listaB)
print(listaC)