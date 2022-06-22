#6) Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe
#também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

p_frase = str(input('Digite uma frase: ').upper())
s_frase = str(input('Digitee outra frase: ').upper())
resp = []
difer_n1 = []
difer_n2 = []


if len(p_frase) != len(s_frase):
    print(f'Primeira frase: "{p_frase}"')
    print(f'Segunda frase: "{s_frase}"')
    print(f'{p_frase}: tamanho: {len(p_frase)} caractere')
    print(f'{s_frase}: tamanho: {len(s_frase)} caractere')
    print('As duas frases são diferentes em tamanho.')
    print('As duas frases possuem conteúdos diferentes')

else:

 
    for i in range(len(p_frase)):
        resp.append(p_frase[i] in s_frase[i])

    
        if False in resp:
            difer_n1.append(p_frase[i])
            difer_n2.append(s_frase[i])
            resp[i] = True


    print(f'Primeira frase: {p_frase}')
    print(f'segunda frase: {s_frase}')
    print(f'{p_frase}: tamanho: {len(p_frase)} caractere')
    print(f'{s_frase}: tamanho: {len(s_frase)} caractere')
    print('As duas frases tem o mesmo tamanho.')
    for i in range(len(p_frase)):
        resp.append(p_frase[i] in s_frase[i])
    if False in resp:
        print(f'As frases são diferentes:{difer_n1} != {difer_n2} '.replace("[", '').replace(']', '').replace("'", '').replace(
            "'", ''))
    else:
        print(f'As frases são iguais:')
