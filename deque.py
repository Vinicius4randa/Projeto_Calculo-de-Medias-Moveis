class Data_Intercection:

    JANELA_PADRAO = 7

    def __init__(self):
        self.dados = [None] * Data_Intercection.JANELA_PADRAO
        self._tamanho = 0
        self._inicio = 0
        self._medias = []
        self._janela = Data_Intercection.JANELA_PADRAO
        self._todosdados = []
        self._soma_media_movel = 0

    def __len__(self):
        return self._tamanho
    def is_empty(self):
        return self._tamanho == 0
    
    def last(self):
        return self.dados[(self._inicio + self._tamanho-1) % len(self.dados)]
    
    def first(self):
        return self.dados[self._inicio]
    
    def next(self, e, recalculando=False):#Adiciona um valor na ultima posição do deque
        if self._tamanho == len(self.dados):
            primeiro_valor = self._dequeue()
            self._soma_media_movel -= primeiro_valor
        
        #COMANDOS PARA ADICIONAR UM NOVO ITEM AO DEQUE(ACHO QUE DA PRA MELHORAR ISSO)
        disponivel = (self._inicio + self._tamanho) %len(self.dados)
        self.dados[disponivel] = e
        self._tamanho += 1
        self._soma_media_movel += e
        self._medias.append(self._media_movel())
        if not recalculando:
            self._todosdados.append(e)
        
    def _media_movel(self):#tira a media de todos os itens do deque se o deque possuir um valor none retorna none
        if self._tamanho == len(self.dados):
            return round(self._soma_media_movel/self._janela, 1)
            
        return None

    def show_media_movel(self):
        return self._medias
    
    def _dequeue(self):#_privado: retira o valor da primeira posição do deque e põe none no lugar
        if self.is_empty():
            raise FilaVazia('A Fila está vazia')
        result = self.dados[self._inicio]
        self.dados[self._inicio] = None
        self._inicio = (self._inicio + 1) %len(self.dados)
        self._tamanho -= 1
        return result

    def set_janela(self, janela):
        self._janela = janela
        self._limpardados()
        self.recalcular_medias_movel()

    def reseta_intersecao(self):
        self._limpardados()
        self._todosdados = []

    def _limpardados(self):
        self._tamanho = 0
        self._inicio = 0
        self._medias = []
        self._soma_media_movel = 0   
        self.dados = [None] * self._janela

    def recalcular_medias_movel(self):
        for i in self._todosdados:
            self.next(i, True)
