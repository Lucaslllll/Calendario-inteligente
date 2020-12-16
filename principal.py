from prettytable import PrettyTable

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
            if valor[i] == str(contador) and lista[contador - 1] == 'Livre':
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

    for i in range(0, len(lista)):
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

lista2 = ['Thiago', '2|456', '3|1', '4|0', '5|6', '6|345']

lista = ['Tales', '2|123', '3|3', '4|2', '5|6', '6|126']

seg = ['Livre', 'Livre', 'Livre', 'Livre', 'Livre', 'Livre']
ter = ['Livre', 'Livre', 'Livre', 'Livre', 'Livre', 'Livre']
qua = ['Livre', 'Livre', 'Livre', 'Livre', 'Livre', 'Livre']
qui = ['Livre', 'Livre', 'Livre', 'Livre', 'Livre', 'Livre']
sex = ['Livre', 'Livre', 'Livre', 'Livre', 'Livre', 'Livre']

prof = []

arquivo = open('dados.txt') 

numProf = int(input("Quantos professores você quer adicionar? "))

for i in range(0, numProf):
    prof.append(input("Qual é o nome do {0}° professor? ".format(i + 1)))

    for c in range(2, 7):
        if c == 2:
            disponivel = str(input('Tem horário disponível na segunda-feira? [S/N] '))
            if disponivel == 'n' or disponivel == 'N':
                horario1 = '0'
                continue
            else:
                horario1 = input('Quais os horários disponíveis? [1, 2, 3, 4, 5, 6]:')
        if c == 3:
            disponivel = str(input('Tem horário disponível na terça-feira? [S/N] '))
            if disponivel == 'n' or disponivel == 'N':
                horario2 = '0'
                continue
            else:
                horario2 = input('Quais os horários disponíveis? [1, 2, 3, 4, 5, 6]:')
        if c == 4:
            disponivel = str(input('Tem horário disponível na quarta-feira? [S/N] '))
            if disponivel == 'n' or disponivel == 'N':
                horario3 = '0'
                continue
            else:
                horario3 = input('Quais os horários disponíveis? [1, 2, 3, 4, 5, 6]:')
        if c == 5:
            disponivel = str(input('Tem horário disponível na quinta-feira? [S/N] '))
            if disponivel == 'n' or disponivel == 'N':
                horario4 = '0'
                continue
            else:
                horario4 = input('Quais os horários disponíveis? [1, 2, 3, 4, 5, 6]:')
        if c == 6:
            disponivel = str(input('Tem horário disponível na sexta-feira? [S/N] '))
            if disponivel == 'n' or disponivel == 'N':
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
