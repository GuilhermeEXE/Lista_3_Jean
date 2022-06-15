#9) Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato
#de escada.

nome = input('Digite seu nome:')
s = nome
while s != '':
    print(s)
    s = s[:-1]
