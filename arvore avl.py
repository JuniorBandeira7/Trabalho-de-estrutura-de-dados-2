from processaArquivo import ProcessadorArquivos as p
import os

class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
        self.altura = 1


class ArvoreAVL:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):#a raiz recebe o valor que vai recebido da funçao inserir no
        self.raiz = self._inserir_no(self.raiz, valor)#passa como parametros a raiz anterior e o valor

    #vai percorrendo a arvore até achar um galho sem filhos. Quando acha, adiciona o valor no lugar vazio
    def _inserir_no(self, raiz, valor):
        if not raiz:#not raiz = lugar vazio
            return No(valor)
        elif len(valor[0]) < len(raiz.valor[0]):
            raiz.esquerda = self._inserir_no(raiz.esquerda, valor)#vai recebendo ate a raiz esquerda == none
        elif len(valor[0]) > len(raiz.valor[0]):
            raiz.direita = self._inserir_no(raiz.direita, valor)
        else:#normalmente a posição das subarvores é feita atraves do tamanho da string do primeiro elemento da lista, caso o tamanho da string for igual, é feita a analise lexografica
            if valor[0] < raiz.valor[0]:
                raiz.esquerda = self._inserir_no(raiz.esquerda, valor)
            else:
                raiz.direita = self._inserir_no(raiz.direita, valor)


        raiz.altura = 1 + max(self._obter_altura(raiz.esquerda), self._obter_altura(raiz.direita))#vai somando a altura nova com a altura da raiz anterior
        balanceamento = self._obter_balanceamento(raiz)

        #caso de rotação simples à esquerda
        if balanceamento > 1 and len(valor[0]) < len(raiz.esquerda.valor[0]):
            return self._rotacionar_direita(raiz)

        #caso de rotação simples à direita
        if balanceamento < -1 and len(valor[0]) > len(raiz.direita.valor[0]):
            return self._rotacionar_esquerda(raiz)

        #caso de rotação dupla à esquerda
        if balanceamento > 1 and len(valor[0]) > len(raiz.esquerda.valor[0]):
            raiz.esquerda = self._rotacionar_esquerda(raiz.esquerda)
            return self._rotacionar_direita(raiz)

        #caso de rotação dupla à direita
        if balanceamento < -1 and len(valor[0]) < len(raiz.direita.valor[0]):
            raiz.direita = self._rotacionar_direita(raiz.direita)
            return self._rotacionar_esquerda(raiz)

        return raiz

    def _obter_altura(self, no):
        if not no:
            return 0
        return no.altura

    def _obter_balanceamento(self, no):
        if not no:
            return 0
        return self._obter_altura(no.esquerda) - self._obter_altura(no.direita)

    def _rotacionar_esquerda(self, z):#troca uma posição pela outra
        y = z.direita

        if y is None:
            return z

        T2 = y.esquerda if y.esquerda is not None else None#verificação para corrigir erro caso o no nao tenha arvore a esquerda ou a direita

        y.esquerda = z
        z.direita = T2

        z.altura = 1 + max(self._obter_altura(z.esquerda), self._obter_altura(z.direita))
        y.altura = 1 + max(self._obter_altura(y.esquerda), self._obter_altura(y.direita))

        return y

    def _rotacionar_direita(self, z):
        y = z.esquerda
        
        if y is None:
            return z

        T3 = y.direita if y.direita is not None else None

        y.direita = z
        z.esquerda = T3

        z.altura = 1 + max(self._obter_altura(z.esquerda), self._obter_altura(z.direita))
        y.altura = 1 + max(self._obter_altura(y.esquerda), self._obter_altura(y.direita))

        return y

    def imprimir_arvore(self):
        if self.raiz:
            self._imprimir_inorder(self.raiz)

    def _imprimir_inorder(self, no):
        if no:
            self._imprimir_inorder(no.esquerda)
            print(no.valor, end=' ')
            self._imprimir_inorder(no.direita)

    def buscar_valor(self, valor1):
        return self._buscar(self.raiz, valor1)

    def _buscar(self, no, valor1):
        if not no or no.valor[0] == valor1:
            return no
        if len(valor1) < len(no.valor[0]):
            return self._buscar(no.esquerda, valor1)
        elif len(valor1) < len(no.valor[0]):
            self._buscar(no.direita, valor1)
        #se o tamanho das strings forem iguais, é comparado lexigraficamente
        else:
            if valor1 < no.valor[0]:
                return self._buscar(no.esquerda, valor1)
            else:
                return self._buscar(no.direita, valor1)




#um = 1
#dicionario = {
    #"oi": ["oi", "possui xablau", f"um {um}"],
    #"julioo": ["julioo"],
    #"luisa": ["luisa"],
    #"xau": ["xau"],
    #"domingo": ["domingo"],
    #"segundaa": ["segundaa"]
#}

arvore_avl = ArvoreAVL()

processador = p()
processador.ler_arquivos()
dicionario = processador.dicionario

for i in dicionario:
    arvore_avl.inserir(dicionario[i])
    

#arvore_avl.inserir(dicionario["oi"])
#arvore_avl.inserir(dicionario["julioo"])
#arvore_avl.inserir(dicionario["luisa"])
#arvore_avl.inserir(dicionario["xau"])
#arvore_avl.inserir(dicionario["domingo"])
#arvore_avl.inserir(dicionario["segundaa"])
#print(arvore_avl._obter_balanceamento(arvore_avl.raiz)) verifica se arvore está balanceada
palavra = input("Qual palavra quer buscar?: ")
busca = arvore_avl.buscar_valor(palavra)

if busca.valor[1] == None:
    print("palavra não encontrada")
print(f"Palavra encontrada: {busca.valor[0]}\n| Arquivo: {busca.valor[1]}  | Quantidade: {busca.valor[2]}")
if len(busca.valor) > 3:
    print(f"| Arquivo: {busca.valor[3][1]} | Quantidade: {busca.valor[3][2]}")
if len(busca.valor) > 4:
    print(f"| Arquivo: {busca.valor[4][1]} | Quantidade: {busca.valor[4][2]}")
if len(busca.valor) > 5:
    print(f"| Arquivo: {busca.valor[5][1]} | Quantidade: {busca.valor[5][2]}")


