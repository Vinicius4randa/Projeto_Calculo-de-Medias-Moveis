class Data_Intercection:
    def __init__(self,Maxlen=3):
        self._dados = [None] * Maxlen
        self._tamanho = 0
        self._inicio = 0
        self._medias = []
        self._janela = Maxlen
        self._todos_dados = []

    def __len__(self):
        return self._tamanho
    def is_empty(self):
        return self._tamanho == 0
    
    def last(self):
        return self._dados[(self._inicio + self._tamanho-1) % len(self._dados)]
    def first(self):
        return self._dados[self._inicio]
    
    def next(self, e, recalculando=False):#Adiciona um valor na ultima posição do deque
        if self._tamanho == len(self._dados):
            self._dequeue()
            self._collection_step()#se estiver cheio deleta o item da primeira posição e chama collection step para reordenar o deque
        
        #COMANDOS PARA ADICIONAR UM NOVO ITEM AO DEQUE(ACHO QUE DA PRA MELHORAR ISSO)
        disponivel = (self._inicio + self._tamanho) %len(self._dados)
        self._dados[disponivel] = e
        self._tamanho += 1
        self._medias.append(self.media_movel())
        if not recalculando:
            self._todos_dados.append(e)
        
    def media_movel(self):#tira a media de todos os itens do deque se o deque possuir um valor none retorna none
        soma = 0
        for i in self._dados:
            if not i:
                return None
            soma += i
            
        return round(soma/self._janela, 1)

    def show_media_movel(self):
        return self._medias
    
    def _dequeue(self):#_privado: retira o valor da primeira posição do deque e põe none no lugar
        if self.is_empty():
            raise FilaVazia('A Fila está vazia')
        result = self._dados[self._inicio]
        self._dados[self._inicio] = None
        self._inicio = (self._inicio + 1) %len(self._dados)
        self._tamanho -= 1
        return result
    
    def _collection_step(self):#_privado: realoca valores das ultimas posições para as primeiras deixando um espaço vasio na ultima posição
        dados_antigos = self._dados 
        self._dados = [None] * self._janela
        posicao = self._inicio
        for k in range(self._tamanho): 
            self._dados[k] = dados_antigos[posicao]
            posicao = (1 + posicao) % len(dados_antigos)
        self._inicio = 0

    def set_janela(self, janela):
        self._janela = janela
        self._tamanho = 0
        self._inicio = 0
        self._medias = []
        self._dados = [None] * janela
        self.recalcular_medias_movel()

    def recalcular_medias_movel(self):
        for i in self._todos_dados:
            self.next(i, True)
            

#TAVA TESTANDO
teste = Data_Intercection()
dados = [10,15,12,5,2,3,1]
saida = []

for i in dados:
    teste.next(i)
    saida.append(teste.media_movel())

print(saida) 

