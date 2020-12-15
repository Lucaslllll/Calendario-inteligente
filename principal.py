from __future__ import unicode_literals
from prettytable import PrettyTable
import prompt_toolkit
from prompt_toolkit import prompt
import tabela_modulos

seg = ['Livre', 'Livre', 'Livre', 'Livre', 'Livre', 'Livre']
ter = ['Livre', 'Livre', 'Livre', 'Livre', 'Livre', 'Livre']
qua = ['Livre', 'Livre', 'Livre', 'Livre', 'Livre', 'Livre']
qui = ['Livre', 'Livre', 'Livre', 'Livre', 'Livre', 'Livre']
sex = ['Livre', 'Livre', 'Livre', 'Livre', 'Livre', 'Livre']

LISTA = []

lista = ['Tales', '2|1', '3|23', '4|2', '5|6', '6|1234']

lista2 = ['Thiago', '2|23', '3|1', '4|N', '5|6', '6|345']

lista3 = ['Lucas', '2|456', '3|23', '4|2', '5|6', '6|26']

print('A lista 1 é:', lista)
print('A lista 2 é:', lista2)
print('A lista 3 é:', lista3)

LISTA.append(lista)
LISTA.append(lista2)
LISTA.append(lista3)

tabela_modulos.criar_lista_horarios(LISTA)
tabela_modulos.criar_lista_prioridade(LISTA)

prof = []

arquivo = open('dados.txt') 

numProf = int(input("Quantos professores você quer adicionar? "))

for i in range(0, numProf):
    prof.append(input("Qual é o nome do {0}° professor? ".format(i + 1)))

    for c in range(2, 7):
        if c == 2:
            disponivel = str(input('Tem horário disponível na segunda-feira? [S/N] '))
            if disponivel == 'n':
                horario1 = '0'
                continue
            else:
                horario1 = input('Quais os horários disponíveis? [1, 2, 3, 4, 5, 6]:')
        if c == 3:
            disponivel = str(input('Tem horário disponível na terça-feira? [S/N] '))
            if disponivel == 'n':
                horario2 = '0'
                continue
            else:
                horario2 = input('Quais os horários disponíveis? [1, 2, 3, 4, 5, 6]:')
        if c == 4:
            disponivel = str(input('Tem horário disponível na quarta-feira? [S/N] '))
            if disponivel == 'n':
                horario3 = '0'
                continue
            else:
                horario3 = input('Quais os horários disponíveis? [1, 2, 3, 4, 5, 6]:')
        if c == 5:
            disponivel = str(input('Tem horário disponível na quinta-feira? [S/N] '))
            if disponivel == 'n':
                horario4 = '0'
                continue
            else:
                horario4 = input('Quais os horários disponíveis? [1, 2, 3, 4, 5, 6]:')
        if c == 6:
            disponivel = str(input('Tem horário disponível na sexta-feira? [S/N] '))
            if disponivel == 'n':
                horario5 = '0' 
            else:
                horario5 = input('Quais os horários disponíveis? [1, 2, 3, 4, 5, 6]:')

            #Envia todas as variáveis para uma linha no arquivo dados.txt
            L = (prof[i] + ' ', '2|' + horario1 + ' ', '3|' + horario2 + ' ',
                    '4|' + horario3 + ' ', '5|' + horario4 + ' ', '6|' + horario5 + '\n') 

            #Adiciona as variáveis em L no arquivo dados.py
            arquivo = open('dados.txt', 'a') 
            arquivo.writelines(L)
            arquivo.close()

#cria a lista lines com base em todas as strings em dados.txt, remove um linha e reescreve tudo no arquivo dados.txt
a_file = open("dados.txt", "r")
lines = a_file.readlines()
a_file.close()

#Adicionar os últimos professores colocados no banco de memoria
i = numProf - 1
while i >= 0:
    print(i)
    l = lines[-1 - i].split()
    adicionar_na_tabela(l)
    print('Foi adicionado à tabela: ', lines[-1 - i])
    i -= 1

print('Uma amostra bem mais implementada da tabela')
x = PrettyTable()
x.add_column('Horários', ["6", "5", "4", "3", "2", "1"])
x.add_column('Segunda-feira', [seg[5], seg[4], seg[3], seg[2], seg[1], seg[0]])
x.add_column('Terça-feira', [ter[5], ter[4], ter[3], ter[2], ter[1], ter[0]])
x.add_column('Quarta-feira', [qua[5], qua[4], qua[3], qua[2], qua[1], qua[0]])
x.add_column('Quinta-feira', [qui[5], qui[4], qui[3], qui[2], qui[1], qui[0]])
x.add_column('Sexta-feira', [sex[5], sex[4], sex[3], sex[2], sex[1], sex[0]])
print(x)

deletar = input('Quer deletar todos os dados? [s/n]')
if deletar == 's':
    a_file = open("dados.txt", "r")
    lines = a_file.readlines()
    a_file.close()

    lines = ''

    new_file = open("dados.txt", "w+")
    for line in lines:
        new_file.write(line)
