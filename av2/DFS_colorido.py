#a ordem de deslocamento é a seguinte: direita, esquerda, mudar de dimensão e (subir ou descer)
#no dicionario "grafo" os nós são dispostos na ordem inversa da ordem de deslocamento
grafo = [ [3, 4, 8, 1],#0    
          [14 ,13, 0, 12],#1
          [1, 6, 3, 14],#2
          [0, 7, 10, 2],#3
          [7, 0, 9, 5],#4
          [6, 1, 4, 13],#5
          [5, 2, 7, 15],#6  
          [4, 3, 11, 6],#7      
          [10, 9, 0],#8
          [11, 8, 4],#9
          [8, 11, 3],#10
          [9, 10, 7],#11
          [14, 1, 13],#12
          [15 ,12, 5],#13
          [12, 15, 2],#14
          [13, 14, 6]#15
        ]
grafoColorido = [ 
    ["semCor", "semCor", "semCor", "semCor"],#0
    ["semCor", "semCor", "semCor", "semCor"],#1
    ["semCor", "semCor", "semCor", "semCor"],#2
    ["semCor", "semCor", "semCor", "semCor"],#3
    ["semCor", "semCor", "semCor", "semCor"],#4
    ["semCor", "semCor", "semCor", "semCor"],#5
    ["semCor", "semCor", "semCor", "semCor"],#6
    ["semCor", "semCor", "semCor", "semCor"],#7
    ["semCor", "semCor", "semCor"],#8
    ["semCor", "semCor", "semCor"],#9
    ["semCor", "semCor", "semCor"],#10
    ["semCor", "semCor", "semCor"],#11
    ["semCor", "semCor", "semCor"],#12
    ["semCor", "semCor", "semCor"],#13
    ["semCor", "semCor", "semCor"],#14
    ["semCor", "semCor", "semCor"]#15
    ]

listaDeCores = ["azul", "amarelo", "verde", "vermelho", "preto", "rosa", "branco", "roxo", "violeta"]
corAtual = None
pilhaDeAbertos = [8]
listaDeFechados = []
listaDeFechadosCopy = []

while pilhaDeAbertos != []:
    noCandidato = pilhaDeAbertos.pop()
    #garantia de que não vai repetir caminho
    if noCandidato in listaDeFechados:
        break

    listaDeFechados.append(noCandidato)#adiciona o no candidato no final da lista de fechados
    indexListaDeFechadosDoNoCandidato = listaDeFechados.index(noCandidato)
    listaDeFechadosCopy.append(noCandidato)
    listaDeCoresCopy = listaDeCores.copy()

    #ver quais cores os vizinhos tem e as remove
    for i in grafoColorido[noCandidato]:
        if i in listaDeCoresCopy:
            listaDeCoresCopy.remove(i)
    for lista in grafo:
        if noCandidato in grafo[grafo.index(lista)]:
            for i in grafoColorido[grafo.index(lista)]:
                if i in listaDeCoresCopy:
                    listaDeCoresCopy.remove(i)

    #define a cor que o no vai ser pintado
    corAtual = listaDeCoresCopy[0]#o fato de escolher a cor de menor indice garante que o algoritimo ira usar o menor numero de cores possiveis
    
    #pinta todas as ocorrencias do no na lista grafo com a cor atual
    for lista in grafo:
        for i in range(len(lista)):
            if lista[i] == noCandidato:
                listaPintar = (grafo.index(lista))#em qual lista
                posicaListaPintar = (lista.index(noCandidato))#em qual posição da lista
                grafoColorido[listaPintar][posicaListaPintar] = corAtual

    #pinta na lista do caminho percorrido  
    listaDeFechadosCopy[indexListaDeFechadosDoNoCandidato] = corAtual

    #percorre o no candidato
    for i in grafo[noCandidato]:
            if i not in listaDeFechados:#se i não estiver na lista de fechados. A lista de fechados é usada para saber o caminho percorrido
                pilhaDeAbertos.append(i)#adiciona ele na lista de abertos. Essa lógica é usada para saber o caminho que o algoritmo esta percorrendo.
print("")
print("")
print("")
print(grafoColorido)#mostra a estrutura tridimensional em forma de grafo 
#print("caminho percorrido com o numero dos nós: ", listaDeFechados) #descomente caso queira ver o caminho percorrido
print("")
print("")
print("")
print(listaDeFechadosCopy)#mostra as cores dos grafos de acordo com a sequencia com que foram pintados 
