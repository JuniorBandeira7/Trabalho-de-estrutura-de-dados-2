#vou considerar a entrada "A" como nó "0" e a saida "B" como nó 64
#a ordem de deslocamento é a seguinte: baixo, esquerda, cima e direita
#no dicionario "grafo" os nós são dispostos na ordem inversa da ordem de deslocamento
grafo = [ [1, 4],       #0    
          [0, 6],  #1
          [3, 7], #2
          [2],  #3
          [5, 0, 9], #4
          [4, 19],  #5
          [7, 1], #6  
          [8, 2, 6],   #7      
          [7, 15], #8
          [10, 4, 29], #9
          [9, 16], #10
          [12], #11
          [13, 11, 17],#12
          [12],#13
          [15],#14
          [14, 21],#15
          [17, 10],#16
          [12, 16],#17
          [19, 24],#18
          [20, 5, 18],#19
          [19, 27],#20
          [15],#21
          [23],#22
          [22, 32],#23
          [25, 18],#24
          [24, 34],#25
          [27, 40],#26
          [28, 20, 26],#27
          [27, 46],#28
          [30, 9],#29
          [29, 51],#30
          [32, 47],#31
          [23, 31],#32
          [34, 38],#33
          [25, 33],#34
          [45],#35
          [57],#36
          [38, 41],#37
          [33, 37],#38
          [40, 43],#39
          [26, 39],#40
          [42, 37],#41
          [41],#42
          [44, 39],#43
          [43, 49],#44
          [35, 46],#45
          [28, 45],#46
          [48, 31, 52],#47
          [47, 54],#48
          [50, 44],#49
          [49, 64],#50
          [52, 30, 58],#51
          [47, 51, 59],#52
          [54, 60],#53
          [48, 53],#54
          [56, 61],#55
          [55],#56
          [58, 36],#57
          [51, 57],#58
          [52],#59
          [61, 53],#60
          [55, 60],#61
          [63],#62
          [64, 62],#63
          [50, 63],#64
        ]

resposta = None
pilhaDeAbertos = [0]
listaDeFechados = []
sucesso = False
while sucesso == False and pilhaDeAbertos != []:#o loop é feito enquanto o sucesso for falso e a pilha de abertos não vazia
    noCandidato = pilhaDeAbertos.pop()#tira o nó candidato da pilha de abertos. É uma pilha, portanto tira o ultimo
    listaDeFechados.append(noCandidato)#adiciona o no candidato no final da lista de fechados
    for i in grafo[noCandidato]:#percorre o grafo no candidato
        if i == 64:#se o i(que é o filho do no candidato que está sendo verificado) for a resposta
            sucesso = True
            resposta = 64
            listaDeFechados.append(resposta)
            break#se achar a resposta para o for, e consequentemente o while, pois sucesso vai ser verdadeiro e a pilha de abertos nao vai estar vazia
        else:
            if i not in listaDeFechados:#se i não estiver na lista de fechados. A lista de fechados é usada para saber o caminho percorrido
                pilhaDeAbertos.append(i)#adiciona ele na lista de abertos. Essa lógica é usada para saber o caminho que o algoritmo esta percorrendo.  
if sucesso == False:
    print("Não achou")
else:
    print(listaDeFechados)#mostra o caminho ate a saida sem contar as voltas ao bater num galho