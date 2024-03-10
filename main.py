from deque import Data_Intercection

deque = Data_Intercection()

def inserirDadosViaTeclado():
    print('Inserção de dados via teclado!')
    global deque
    while True:
        dado = input('Digite um valor (ou "s" para sair): ')
        if dado.lower() == 's':
            break
        deque.next(int(dado))

def inserirDadosViaArquivo():
    print('Inserção de dados via arquivo!')
    global deque
    path_arquivo = input('Digite o caminho do arquivo: ')
    with open(path_arquivo, 'r') as arquivo:
        dados = arquivo.readlines()
        for dado in dados:
            deque.next(int(dado))


if __name__ == '__main__':
    print()
    print('### Cálculo de média móvel ###')
    
    while True:
        print('''
        Opções:
            1 - Inserir dados via teclado.
            2 - Inserir dados via arquivo.
            3 - Alterar períodos de média móvel.
            4 - Exibir as médias móveis calculadas.
            5 - Salvar em arquivo as médias móveis calculadas.
            6 - Sair.
            ''')

        opcao = input('Digite a opção desejada: ')
    
        match opcao:
            case '1':
                inserirDadosViaTeclado()
            case '2':
                inserirDadosViaArquivo()
            case '3':
                print('Alteração de períodos de média móvel')
            case '4':
                print('Média móvel calculada: ', deque.show_media_movel())                
            case '5':
                print('Salvando em arquivos as médias móveis calculadas')
            case '6':
                print('Saindo...')
                exit(0)
            case _:
                print('Opção inválida')
