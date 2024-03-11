class Data_Intercection:

    JANELA_PADRAO = 7

    def __init__(self):
        self._dados = [None] * Data_Intercection.JANELA_PADRAO
        self._tamanho = 0
        self._inicio = 0
        self._medias = []
        self._janela = Data_Intercection.JANELA_PADRAO
        self._todos_dados = []
        self._soma_media_movel = 0

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
            primeiro_valor = self._dequeue()
            self._soma_media_movel -= primeiro_valor
        
        #COMANDOS PARA ADICIONAR UM NOVO ITEM AO DEQUE(ACHO QUE DA PRA MELHORAR ISSO)
        disponivel = (self._inicio + self._tamanho) %len(self._dados)
        self._dados[disponivel] = e
        self._tamanho += 1
        self._soma_media_movel += e
        self._medias.append(self._media_movel())
        if not recalculando:
            self._todos_dados.append(e)
        
    def _media_movel(self):#tira a media de todos os itens do deque se o deque possuir um valor none retorna none
        if self._tamanho == len(self._dados):
            return round(self._soma_media_movel/self._janela, 1)
            
        return None

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

    def set_janela(self, janela):
        self._janela = janela
        self._tamanho = 0
        self._inicio = 0
        self._medias = []
        self._soma_media_movel = 0
        self._dados = [None] * janela
        self.recalcular_medias_movel()

    def recalcular_medias_movel(self):
        for i in self._todos_dados:
            self.next(i, True)
