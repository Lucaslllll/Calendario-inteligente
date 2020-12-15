from prettytable import PrettyTable

seg = ['Livre', 'Livre', 'Livre', 'Livre', 'Livre', 'Livre']
ter = ['Livre', 'Livre', 'Livre', 'Livre', 'Livre', 'Livre']
qua = ['Livre', 'Livre', 'Livre', 'Livre', 'Livre', 'Livre']
qui = ['Livre', 'Livre', 'Livre', 'Livre', 'Livre', 'Livre']
sex = ['Livre', 'Livre', 'Livre', 'Livre', 'Livre', 'Livre']

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

def adicionar_na_tabela(LISTA):
    prioridade = criar_lista_prioridade(LISTA)
    for a in range(0, len(LISTA)):
        lista = LISTA[a]
        for i in range(0, len(prioridade)):
            prioridadesDia = prioridade[i]
            if prioridadesDia[a] == lista[0] and prioridade[i] == 0:
                organizar_coluna(seg, lista[0], valor)
            if prioridadesDia[a] == lista[0] and prioridade[i] == 1:
                organizar_coluna(ter, lista[0], valor)
            if prioridadesDia[a] == lista[0] and prioridade[i] == 2:
                organizar_coluna(qua, lista[0], valor)
            if prioridadesDia[a] == lista[0] and prioridade[i] == 3:
                organizar_coluna(qui, lista[0], valor)
            if prioridadesDia[a] == lista[0] and prioridade[i] == 4:
                organizar_coluna(sex, lista[0], valor)
            else:
                continue

def ordem_crescente(LISTA):
    for y in range(0, len(LISTA)):
        lista = LISTA[y]
        lista.sort()
        LISTA[y] = lista

def tem_valor_dobro(LISTA):
    for a in range(0, len(LISTA)):
        lista = LISTA[a]
        i = -1 
        y = -1 
        while (i + 1 < len(lista)):
            i += 1
            y = -1
            contador = 0
            while (y + 1 < len(lista)):
                y += 1
                if lista[i] == lista[y]:
                    contador += 1
                if contador == 2:
                    del lista[y]
                    LISTA[a] = lista
                    i -= 1
    return LISTA

def contar_horarios(hor):
    numHorarios = 0
    for i in range(2, len(hor)):
        if hor[i] != '0':
            numHorarios += 1
        elif i == len(hor):
            break
        else:
            numHorarios = 'N'
    return numHorarios

def criar_lista_horarios(LISTA):
    horarios = [[], [], [], [], []]
    for i in range(0, len(LISTA)):
        dadosUsuario = LISTA[i]
        for y in range(1, len(dadosUsuario)):
            if contar_horarios(dadosUsuario[y]) != 0:
                horariosDoDia = contar_horarios(dadosUsuario[y])
                parte = horarios[y - 1]
                parte.append(horariosDoDia)
            else:
                continue
    tem_valor_dobro(horarios)
    ordem_crescente(horarios)
    print('Os horarios são', horarios)
    return horarios

def verificar_tem_menor_quantidade_horario(horarioUsuario, horariosTabela, tamanho, tamanho2):
    if len(horariosTabela) != 0 and str(horarioUsuario) == str(min(horariosTabela)):
        horariosTabela.remove(min(horariosTabela))
        return True
    elif len(horariosTabela) == 0 and tamanho2 != tamanho: #and horarioUsuario == 'N':
        return True
    #elif len(horariosTabela) == 0 and horarioUsuario != 'N':
    #    return True
    else:
        return False

def verificar_se_todos_adicionados(lista, tamanho):
    for i in range(0, len(lista)):
        parte = lista[i]
        if len(parte) != tamanho:
            condicao = False
        else:
            condicao = True

    return condicao

def criar_lista_prioridade(LISTA):
    horarios = criar_lista_horarios(LISTA)
    usuarioPrioridade = [[], [], [], [], []]
    i = 0
    y = 1
    condicao = False
    while condicao == False:
        while i < len(LISTA):
                lista = LISTA[i]
                y = 1
                while y < len(lista):
                    parte = usuarioPrioridade[y - 1]
                    if verificar_tem_menor_quantidade_horario(contar_horarios(lista[y]), horarios[y - 1], len(parte), len(LISTA)) == True:
                        parte = usuarioPrioridade[y - 1]
                        parte.append(lista[0])
                        y += 1
                    else:
                        y += 1
                i += 1
        if verificar_se_todos_adicionados(usuarioPrioridade, len(LISTA)) == False: #and i == len(LISTA):
            i = 0
        else:
            condicao = True
            
    print(usuarioPrioridade)
    return usuarioPrioridade

def printar_tabela(LISTA):
    adicionar_na_tabela(LISTA)
    x = PrettyTable()
    x.add_column('Horários', ["6", "5", "4", "3", "2", "1"])
    x.add_column('Segunda-feira', [seg[5], seg[4], seg[3], seg[2], seg[1], seg[0]])
    x.add_column('Terça-feira', [ter[5], ter[4], ter[3], ter[2], ter[1], ter[0]])
    x.add_column('Quarta-feira', [qua[5], qua[4], qua[3], qua[2], qua[1], qua[0]])
    x.add_column('Quinta-feira', [qui[5], qui[4], qui[3], qui[2], qui[1], qui[0]])
    x.add_column('Sexta-feira', [sex[5], sex[4], sex[3], sex[2], sex[1], sex[0]])
    print(x)
