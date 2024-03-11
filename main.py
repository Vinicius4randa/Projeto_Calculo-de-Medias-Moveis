from deque import Data_Intercection

deque = Data_Intercection()

def inserirDadosViaTeclado():
    print('Inserção de dados via teclado!')
    global deque
    while True:
        dado = input('Digite um valor (ou "v" para voltar ao menu): ')
        if dado.lower() == 'v':
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

def salvarMediasCalculadasEmArquivo():
    path_arquivo = input('Digite o caminho do arquivo: ')
    with open(path_arquivo, 'w') as arquivo:
        for media in deque.show_media_movel():
            arquivo.write(str(media) + '\n')


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
            5 - Acessar dados inseridos.  
            6 - Salvar em arquivo as médias móveis calculadas.
            7 - Sair.
            ''')

        opcao = input('Digite a opção desejada: ')
    
        match opcao:
            case '1':
                inserirDadosViaTeclado()
            case '2':
                inserirDadosViaArquivo()
            case '3':
                janela = int(input('Digite o novo período da média móvel: '))
                deque.set_janela(janela)
                print('Período alterado!')
                if not deque.is_empty(): 
                    print('As médias foram recalculadas de acordo com novo período!')
            case '4':
                print('Média móvel calculada: ', deque.show_media_movel())     
            case '5': 
                print('Dados inseridos:', deque.dados)
                manter = input('Deseja manter esses dados? S ou N ')
                if manter.upper() == 'N':
                    deque.reseta_intersecao()
            case '6':
                salvarMediasCalculadasEmArquivo()
            case '7':
                print('Saindo...')
                exit(0)
            case _:
                print('Opção inválida')
