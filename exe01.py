#1) Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a
# média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.


m = [ ]
a_m = 0
for x in range (0, 10, 1):
    soma = 0
    for y in range (0, 4, 1):
        print('Digite a', y + 1, 'nota do', x + 1 ,'aluno:')
        s =+ float(input())
    m.append (s)
    if m [ x ] >= 7.0:
        a_m += 1
print('As médias são:', m)
print('O numero de alunos acima da média é:', a_m)