#quantidade = int(input("Qual é a quantidade de horários que você quer colocar? "))
#lista_horario = []
#
#for i in range(0, quantidade):
#	valor = input("Digite o "+str(i+1)+"º horário: ")
#	lista_horario.append(valor)
# USAR DEPOIS
# dados = open('dados.txt', 'r')

prof = input("Qual é o nome do professor?")

horarios = input("Quais são os horários que esse professor tem disponível?")

lista_horario = horarios.split()

print(lista_horario)


# disponiveis = []

# for c in range(2, 7):
#     if c == 2:
#         disponivel = str(input(f'Tem horário disponível na segunda-feira? [S/N]')).strip().lower()[0]
#         if disponivel == 'n':
#             break
#         else:
#             disponiveis.append(input('Quais os horários disponíveis? [1, 2, 3, 4, 5, 6]: '))
#     if c == 2:
#         disponivel = str(input(f'Tem horário disponível na terça-feira? [S/N]')).strip().lower()[0]
#         if disponivel == 'n':
#             break
#         else:
#             disponiveis.append(input('Quais os horários disponíveis? [1, 2, 3, 4, 5, 6]: '))
