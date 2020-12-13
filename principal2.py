from __future__ import unicode_literals
from prettytable import PrettyTable
import prompt_toolkit
from prompt_toolkit import prompt


# BEGINLUCAS

# essa função tem o objetivo de organizar os dados para assim melhorar o trabalho da análise
#def organizar_dados(prof, lista):
#    contador = 0
#    for x in lista:
#        contador += 1
#
#    dic = {'professor': prof, 'dias': [None]*contador}
#    contador = 0 
#    for x in lista:
#        print(x)
#        
#        # x[4:] assim corto nome do dia da semana (ex: seg = segunda) e o espaço em branco
#        somente_horario = x[4:]
#        dic['dias'][contador] = {x.split()[0] : somente_horario.split()}
#        contador += 1
#
#    print(dic)

# ENDLUCAS

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
            disponivel = str(input('Tem horário disponível na segunda-feira? [S/N] '))
            if disponivel == 'n':
                horario2 = '0'
                continue
            else:
                horario2 = input('Quais os horários disponíveis? [1, 2, 3, 4, 5, 6]:')
        if c == 4:
            disponivel = str(input('Tem horário disponível na segunda-feira? [S/N] '))
            if disponivel == 'n':
                horario3 = '0'
                continue
            else:
                horario3 = input('Quais os horários disponíveis? [1, 2, 3, 4, 5, 6]:')
        if c == 5:
            disponivel = str(input('Tem horário disponível na segunda-feira? [S/N] '))
            if disponivel == 'n':
                horario4 = '0'
                continue
            else:
                horario4 = input('Quais os horários disponíveis? [1, 2, 3, 4, 5, 6]:')
        if c == 6:
            disponivel = str(input('Tem horário disponível na segunda-feira? [S/N] '))
            if disponivel == 'n':
                horario5 = '0' 
            else:
                horario5 = input('Quais os horários disponíveis? [1, 2, 3, 4, 5, 6]:')

            #Envia todas as variáveis para uma linha no arquivo dados.txt
            L = (prof[i] + ' ', 'seg/' + horario1 + ' ', 'ter/' + horario2 + ' ',
                    'qua/' + horario3 + ' ', 'qui/' + horario4 + ' ', 'sex/' + horario5 + '\n') 
            print('A string adicionada foi', L)

            arquivo = open('dados.txt', 'a') 
            arquivo.writelines(L)

#cria a lista lines com base em todas a string em dados.txt, remove um linha e reescreve tudo no arquivo dados.txt
a_file = open("dados.txt", "r")
lines = a_file.readlines()
a_file.close()

#Para trabalhar com a string
objeto = lines[0]
partes = objeto.split()

print('Todas as strings são:', lines)
print('A string um é:', objeto)

print('Printando as partes da string um:', partes)

with open("dados.txt", "r") as file:

    #first_line = file.readline()

    for last_line in file:
        pass

partes2 = last_line.split()

print('Printando as partes da string adicionada', partes2)

#Ideia de implementação da tabela
#if numProf == 1:
#    x = PrettyTable()
#    x.add_column('Horários', ["6", "5", "4", "3", "2", "1"])
#    x.add_column('Segunda', [profs[0], profs[1], profs[2], profs[3], profs[4], profs[5]])
#    print(x)

print('Uma amostra não implementada da tabela')
x = PrettyTable()
x.add_column('Horários', ["6", "5", "4", "3", "2", "1"])
x.add_column('Segunda', ['tales', 'lucas', 'tales', 'thiago', 'null', 'null'])
x.add_column('Terça', ['tales', 'lucas', 'tales', 'thiago', 'null', 'null'])
x.add_column('Quarta', ['tales', 'lucas', 'tales', 'thiago', 'null', 'null'])
x.add_column('Quinta', ['tales', 'lucas', 'tales', 'thiago', 'null', 'null'])
x.add_column('Sexta', ['tales', 'lucas', 'tales', 'thiago', 'null', 'null'])
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
    new_file.close()
