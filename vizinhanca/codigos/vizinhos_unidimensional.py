def vizinhos_unidimensional(no, mapa_neuronios, R):
    
    vizinhanca = []
    
    if R < 0:
        R = 0

    while R >= len(mapa_neuronios):
        R -= 1

    colunaInicial = no - R 
    colunaFinal = no + R + 1

    if colunaInicial < 0:
        colunaInicial = 0

    while colunaFinal > len(mapa_neuronios):
        colunaFinal -= 1

    for i in range(colunaInicial, colunaFinal):
        #print(mapa_neuronios[i])
        if R != 0 and mapa_neuronios[i] != mapa_neuronios[no]:
            vizinhanca.append(mapa_neuronios[i])
            #vizinhos.append(mapa_neuronios[i])
    
    if R == 0:
        vizinhanca.append(mapa_neuronios[no])

    return vizinhanca

def mostrar_vizinhos(mapa_neuronios, R):

    for i in range(0, len(mapa)):
        aux = vizinhos_unidimensional(i, mapa_neuronios, R)
        print('\n### Vizinhos do nó: ', i, '###\n', aux)

############################
########## TESTES ##########
############################

mapa = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

R = 2

mostrar_vizinhos(mapa, R)
