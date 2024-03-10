class Data_Intercection:
    def __init__(self,Maxlen=3):
        self._dados = [None] * Maxlen
        self._tamanho = 0
        self._inicio = 0
        
        self.janela = Maxlen

    def __len__(self):
        return self._tamanho
    def is_empty(self):
        return self._tamanho == 0
    
    def last(self):
        return self._dados[(self._inicio + self._tamanho-1) % len(self._dados)]
    def first(self):
        return self._dados[self._inicio]
    
    def next(self, e):
        if self._tamanho == len(self._dados):
            self._dequeue()
            self._collection_step()
        disponivel = (self._inicio + self._tamanho) %len(self._dados)
        self._dados[disponivel] = e
        self._tamanho += 1
    def media_movel(self):
        soma = 0
        for i in self._dados:
            if not i:
                return None
            soma += i
            
        return round(soma/self.janela)

    
    def _dequeue(self):
        if self.is_empty():
            raise FilaVazia('A Fila está vazia')
        result = self._dados[self._inicio]
        self._dados[self._inicio] = None
        self._inicio = (self._inicio + 1) %len(self._dados)
        self._tamanho -= 1
        return result
    
    def _collection_step(self):
        dados_antigos = self._dados 
        self._dados = [None] * self.janela
        posicao = self._inicio
        for k in range(self._tamanho): 
            self._dados[k] = dados_antigos[posicao]
            posicao = (1 + posicao) % len(dados_antigos)
        self._inicio = 0

teste = Data_Intercection()
dados = [10,15,12,5,2,3,1]
saida = []

for i in dados:
    teste.next(i)
    saida.append(teste.media_movel())

print(saida) 

