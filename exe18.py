#18) Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no
#formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data
#seja inválida.

def dE(dia, mes, ano):
    mE = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", 'Setembro', "Outubro",
               'Novembro', 'Dezembro']


    if mes or dia > 12 or dia or mes < 1:
        return print("NULL")
    else:
        return print(f'Data: Dia {dia}, de {mE[mes]} de {ano} ')


print(dE(int(input('Dia: ')), int(input('Mês: ')), int(input('Ano: '))), end='')
