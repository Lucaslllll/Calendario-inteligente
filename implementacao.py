lista = ['thiago', '2?456', '3?0', '4?123', '5?456', '6?345']

seg = ['', '', '', '', '', '']
ter = ['thiago', 'thiago', 'thiago', '', '', '']
qua = ['thiago', 'thiago', 'thiago', '', '', '']
qui = ['thiago', 'thiago', 'thiago', '', '', '']
sex = ['thiago', 'thiago', 'thiago', '', '', '']

contador = 1
usuario = lista[0]

for elemento in range(1, len(lista)):
    valor = lista[elemento]
    if valor[0] == '2' and valor[2] != '0':
        for i in range(2, len(valor)):
            print("len(: ", len(valor))
            print('i: ', i)
            while contador <= 6:
                print('contador', contador)
                print('valor[i] e contador: ', valor[i], contador)
                if valor[i] == str(contador):
                        print('valor[i] e contador: ', valor[i], contador)
                        seg[contador - 1] = usuario
                        contador += 1
                else:
                    #print('hello')
                    #seg[contador - 1] = ''
                    contador += 1
            contador = 1
            continue

print(seg)
