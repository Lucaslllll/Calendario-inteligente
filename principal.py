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
