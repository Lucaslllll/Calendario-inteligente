# BEGINLUCAS

# essa função tem o objetivo de organizar os dados para assim melhorar o trabalho da análise
def organizar_dados(prof, lista):
    contador = 0
    for x in lista:
        contador += 1

    dic = {'professor': prof, 'dias': [None]*contador}
    contador = 0 
    for x in lista:
        print(x)
        
        # x[4:] assim corto nome do dia da semana (ex: seg = segunda) e o espaço em branco
        somente_horario = x[4:]
        dic['dias'][contador] = {x.split()[0] : somente_horario.split()}
        contador += 1

    print(dic)

# ENDLUCAS



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
            disponiveis.append('seg ' + input('Quais os horários disponíveis? [1, 2, 3, 4, 5, 6]: '))
    if c == 3:
        disponivel = str(input(f'Tem horário disponível na terça-feira? [S/N] ')).strip().lower()[0]
        if disponivel == 'n':
            continue
        else:
            print('Digite o número e dê espaço para cada novo número, exemplo: 1 2. O primeiro e o segundo horário.')
            disponiveis.append('ter ' +input( 'Quais os horários disponíveis? [1, 2, 3, 4, 5, 6]: '))
    if c == 4:
        disponivel = str(input(f'Tem horário disponível na quarta-feira? [S/N] ')).strip().lower()[0]
        if disponivel == 'n':
            continue
        else:
            print('Digite o número e dê espaço para cada novo número, exemplo: 1 2. O primeiro e o segundo horário.')
            disponiveis.append('qua ' + input('Quais os horários disponíveis? [1, 2, 3, 4, 5, 6]: '))
    if c == 5:
        disponivel = str(input(f'Tem horário disponível na quinta-feira? [S/N] ')).strip().lower()[0]
        if disponivel == 'n':
            continue
        else:
            print('Digite o número e dê espaço para cada novo número, exemplo: 1 2. O primeiro e o segundo horário.')
            disponiveis.append('qui ' + input('Quais os horários disponíveis? [1, 2, 3, 4, 5, 6]: '))
    if c == 6:
        disponivel = str(input(f'Tem horário disponível na sexta-feira? [S/N] ')).strip().lower()[0]
        if disponivel == 'n':
            continue
        else:
            print('Digite o número e dê espaço para cada novo número, exemplo: 1 2. O primeiro e o segundo horário.')
            disponiveis.append('sex ' + input('Quais os horários disponíveis? [1, 2, 3, 4, 5, 6]: '))
print(disponiveis)

organizar_dados(prof, disponiveis)

#THIAGO

