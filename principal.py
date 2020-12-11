#quantidade = int(input("Qual é a quantidade de horários que você quer colocar? "))
#lista_horario = []
#
#for i in range(0, quantidade):
#	valor = input("Digite o "+str(i+1)+"º horário: ")
#	lista_horario.append(valor)
# USAR DEPOIS
# dados = open('dados.txt', 'r')

prof = input("Qual é o nome do professor? ")
#THIAGO
disponiveis = []
horarios = [[], [], [], [], []]

for c in range(2, 7):
    if c == 2:
        disponivel = str(input(f'Tem horário disponível na segunda-feira? [S/N] ')).strip().lower()[0]
        if disponivel == 'n':
            continue
        else:
            print('Digite o número e dê espaço para cada novo número, exemplo: 1 2. O primeiro e o segundo horário.')
            disponiveis.append('s' + input('Quais os horários disponíveis? [1, 2, 3, 4, 5, 6]: '))
    if c == 3:
        disponivel = str(input(f'Tem horário disponível na terça-feira? [S/N] ')).strip().lower()[0]
        if disponivel == 'n':
            continue
        else:
            print('Digite o número e dê espaço para cada novo número, exemplo: 1 2. O primeiro e o segundo horário.')
            disponiveis.append(input('t' + 'Quais os horários disponíveis? [1, 2, 3, 4, 5, 6]: '))
    if c == 4:
        disponivel = str(input(f'Tem horário disponível na quarta-feira? [S/N] ')).strip().lower()[0]
        if disponivel == 'n':
            continue
        else:
            print('Digite o número e dê espaço para cada novo número, exemplo: 1 2. O primeiro e o segundo horário.')
            disponiveis.append('qua' + input('Quais os horários disponíveis? [1, 2, 3, 4, 5, 6]: '))
    if c == 5:
        disponivel = str(input(f'Tem horário disponível na quinta-feira? [S/N] ')).strip().lower()[0]
        if disponivel == 'n':
            continue
        else:
            print('Digite o número e dê espaço para cada novo número, exemplo: 1 2. O primeiro e o segundo horário.')
            disponiveis.append('qui' + input('Quais os horários disponíveis? [1, 2, 3, 4, 5, 6]: '))
    if c == 6:
        disponivel = str(input(f'Tem horário disponível na sexta-feira? [S/N] ')).strip().lower()[0]
        if disponivel == 'n':
            continue
        else:
            print('Digite o número e dê espaço para cada novo número, exemplo: 1 2. O primeiro e o segundo horário.')
            disponiveis.append(input('sex' + 'Quais os horários disponíveis? [1, 2, 3, 4, 5, 6]: '))
print(disponiveis)
#THIAGO
