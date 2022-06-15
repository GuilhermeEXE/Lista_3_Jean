#3) Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu
#respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

idades = []
alturas = []

for valor in range(0, 5):
    idades.append(int(input("Digite a idade:")))
    alturas.append(float(input("Digite a altura:")))

print("Idades na ordem inversa:")
for valor in range(0, 5):
    print(idades[len(idades)-1-valor])

print("Alturas na ordem inversa:")
for valor in range(0, 5):
    print(alturas[len(alturas)-1-valor])