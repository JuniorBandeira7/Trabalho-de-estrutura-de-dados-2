import os

class ProcessadorArquivos:
    def __init__(self):
        self.dicionario = {}

    def processar_arquivo(self, arquivo):
        with open(arquivo, 'r') as f:
            palavras_arquivo = f.read().split()
            palavras_unicas = set(palavras_arquivo)
            for palavra in palavras_unicas:
                chave = palavra
                quantidade = palavras_arquivo.count(palavra)
                if chave in self.dicionario:
                    self.dicionario[chave].append([palavra, arquivo, quantidade])
                else:
                    self.dicionario[chave] = [palavra, arquivo, quantidade]

    def ler_arquivos(self):
        quantidade = int(input("Digite a quantidade de arquivos a serem lidos (Até 4 arquivos): "))
        for i in range(quantidade):
            nome_arquivo = input(f"Digite o nome do arquivo {i+1}: ")
            if os.path.exists(nome_arquivo):
                self.processar_arquivo(nome_arquivo)
            else:
                print(f"O arquivo '{nome_arquivo}' não existe.")
                exit()

    #def pesquisar_palavra(self, palavra_pesquisada):
        #for palavra in self.dicionario:
            #if palavra == palavra_pesquisada:
                #print(f"Palavra encontrada: {palavra} | Arquivo: {self.dicionario[palavra][1]} | Quantidade: {self.dicionario[palavra][2]}", end='')
                #if len(self.dicionario[palavra]) > 2:
                    #print(f" | Arquivo: {self.dicionario[palavra][3][1]} | Quantidade: {self.dicionario[palavra][3][2]}", end='')
                #if len(self.dicionario[palavra]) > 3:
                    #print(f" | Arquivo: {self.dicionario[palavra][4][1]} | Quantidade: {self.dicionario[palavra][4][2]}", end='')
                #if len(self.dicionario[palavra]) > 4:
                    #print(f" | Arquivo: {self.dicionario[palavra][5][1]} | Quantidade: {self.dicionario[palavra][5][2]}", end='')
                #break
            #else:
                #continue
        #else:
            #print(f"A palavra '{palavra_pesquisada}' não foi encontrada.")


#processador = ProcessadorArquivos()
#processador.ler_arquivos()
#print(processador.dicionario)

#palavra_pesquisada = input("Digite a palavra que deseja pesquisar: ")
#processador.pesquisar_palavra(palavra_pesquisada)
