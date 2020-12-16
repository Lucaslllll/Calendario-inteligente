# lista = ['thiago', '2?456', '3?0', '4?123', '5?456', '6?345']

# seg = ['', '', '', '', '', '']
# ter = ['thiago', 'thiago', 'thiago', '', '', '']
# qua = ['thiago', 'thiago', 'thiago', '', '', '']
# qui = ['thiago', 'thiago', 'thiago', '', '', '']
# sex = ['thiago', 'thiago', 'thiago', '', '', '']

# contador = 1
# usuario = lista[0]

# for elemento in range(1, len(lista)):
#     valor = lista[elemento]
#     if valor[0] == '2' and valor[2] != '0':
#         for i in range(2, len(valor)):
#             print("len(: ", len(valor))
#             print('i: ', i)
#             while contador <= 6:
#                 print('contador', contador)
#                 print('valor[i] e contador: ', valor[i], contador)
#                 if valor[i] == str(contador):
#                         print('valor[i] e contador: ', valor[i], contador)
#                         seg[contador - 1] = usuario
#                         contador += 1
#                 else:
#                     #print('hello')
#                     #seg[contador - 1] = ''
#                     contador += 1
#             contador = 1
#             continue
# print(seg)



# ÁREA DE IMPLEMENTAÇÃO DE TESTES


# testando a possibilidade de colocar uma listagem com todos os professores já salvos anteriormente

from __future__ import unicode_literals
from prettytable import PrettyTable
import prompt_toolkit
from prompt_toolkit import prompt
from time import sleep
import os

seg = ['--', '--', '--', '--', '--', '--']
ter = ['--', '--', '--', '--', '--', '--']
qua = ['--', '--', '--', '--', '--', '--']
qui = ['--', '--', '--', '--', '--', '--']
sex = ['--', '--', '--', '--', '--', '--']

def dia_da_semana(valor):

    if valor == '2':
        return 'Segunda-feira'
    elif valor == '3':
        return 'Terça-feira'
    elif valor == '4':
        return 'Quarta-feira'
    elif valor == '5':
        return 'Quinta-feira'
    elif valor == '6':
        return 'Sexta-feira'

def organizar_coluna(lista, usuario, valor):
    contador = 1
    for i in range(2, len(valor)):
        while contador <= 6:
            # "Livre" ou "--" por isso deve ter o or, caso contrário nunca irá entrar em outras condições
            if valor[i] == str(contador) and (lista[contador - 1] == 'Livre' or lista[contador - 1] == '--'):
                    lista[contador - 1] = usuario
                    contador += 1
            elif valor[i] == str(contador) and lista[contador - 1] != 'Livre':
                print('Erro com {0}: o horário {1} na {2} já foi reservado para {3}.'.format(usuario, contador, dia_da_semana(valor[0]), lista[contador - 1]))
                contador += 1
            else:
                contador += 1
        contador = 1
    return lista

def adicionar_na_tabela(lista):

    for i in range(1, len(lista)):
        valor = lista[i]
        if valor[0] == '2' and valor[2] != '0':
           organizar_coluna(seg, lista[0], valor)
        if valor[0] == '3' and valor[2] != '0':
           organizar_coluna(ter, lista[0], valor)
        if valor[0] == '4' and valor[2] != '0':
           organizar_coluna(qua, lista[0], valor)
        if valor[0] == '5' and valor[2] != '0':
           organizar_coluna(qui, lista[0], valor)
        if valor[0] == '6' and valor[2] != '0':
           organizar_coluna(sex, lista[0], valor)


ver_todos = input('Você quer ver todos os dados salvo no arquivo? [s/n] ').lower()[0]

if ver_todos == 's':
    print("a")

a_file = open("dados.txt", "r")
lines = a_file.readlines()
a_file.close()

contador = 0
for x in lines:
    contador += 1

for i in range(0, contador):
    line = lines[i].split()
    adicionar_na_tabela(line)
    

print(lines)


x = PrettyTable()
x.add_column('Horários',["1: 07:30h - 8:40h", "2: 08:55h - 10:35h", "3: 10:50h - 12:30h", "4: 13:00h - 14:40h", 
"5: 14:55h - 16:35h", "6: 16:50h - 18:30h"])
x.add_column('Segunda-feira', [seg[0], seg[1], seg[2], seg[3], seg[4], seg[5]])
x.add_column('Terça-feira', [ter[0], ter[1], ter[2], ter[3], ter[4], ter[5]])
x.add_column('Quarta-feira', [qua[0], qua[1], qua[2], qua[3], qua[4], qua[5]])
x.add_column('Quinta-feira', [qui[0], qui[1], qui[2], qui[3], qui[4], qui[5]])
x.add_column('Sexta-feira', [sex[0], sex[1], sex[2], sex[3], sex[4], sex[5]])

print(x)