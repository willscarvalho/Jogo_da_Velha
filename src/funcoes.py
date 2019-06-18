
def criar_tabuleiro():
    """
    Função que cria o tabuleiro das posições do jogo.
    Return: retorno uma listas contendo outra 3 listas respectivamente
    com os valores vazio do tabuleiro -> representação de matriz em python.
    """
    tabuleiro = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    return tabuleiro


def definir_ganhador(ganhador, jogador1, jogador2):
    """
    Função para definir quem ganhou o jogo, caso não há ganhador retorna velha.
    ganhador: Variável do loop que identifica se o ganhador e X ou Y antes das
    9 jogadas.
    jogador1: variável jo primeiro jogador
    jogador2: variavel do segundo jogador:
    Obs: exibi a menssagem de acordo com o ganhador ou empate.
    """
    print('{}'.format(ganhador))
    if ganhador == jogador1:
        print('O Jogador1 = {}, GANHOU!'.format(ganhador))
    else:
        if ganhador == jogador2:
            print('O Jogador2 = {}, GANHOU!'.format(ganhador))
        else:
            print('Deu VELHA!')


def definir_posicao_jogada():
    """
    Função para definir as entradas da linha e coluna no tabuleiro.
    return: retornará os inteiros da linah e coluna para as variáveis que
    chamam a função.
    """
    linha = int(input('Linha: '))
    coluna = int(input('Coluna: '))
    return linha, coluna


def efetuar_jogada(jogador, tabuleiro):
    """
    Função para efetuar a jogada no tabuleiro.
    jogador = jogador atual da rodada.
    tabuleiro = tabuleiro do jogo a cada jogada.
    return: tabuleiro atualizado com a jogada na posição.
    """
    linha = coluna = validar = 0
    while True:
        linha, coluna = definir_posicao_jogada()
        validar = verificar_jogada(linha, coluna, tabuleiro)
        if validar == 1:
            tabuleiro[linha][coluna] = jogador
            log_jogada(jogador, linha, coluna)
            mostrar_tabuleiro(tabuleiro)
            break
    return tabuleiro


def escolher_jogador():
    """
    Função para escolher qual variável cada jogador irá jogar.
    return: as variáveis dos jogadores respectivamente para a
    variáveis que chamam essa função.
    """
    while True:
        jog1 = ' '
        jog2 = ' '
        print('1° Jogador, Ecolhe X ou O : ')
        opcao = str(input('')).strip().upper()[0]
        if opcao in 'xX' or opcao in 'oO':
            if opcao in 'xX':
                jog1 = opcao
                jog2 = 'O'
            elif opcao in 'oO':
                jog1 = opcao
                jog2 = 'X'
            print('Jogador 1 = {}.'.format(jog1))
            print('Jogador 2 = {}.'.format(jog2))
            break
        else:
            print('Entrada inválida.')
    return jog1, jog2


def inicio():
    """
    Função para exibir na tela o início do jogo.
    """
    print('{}{}{}'.format('.', '-'*40, '.'))
    print('{:<15}JOGO DA VELHA{:>14}'.format('|', '|'))
    print('{}{}{}'.format("'", '-'*40, "'"))


def jogo_loop(tabuleiro, jogador1, jogador2, ganhador):
    """
    Função que fará o loop das 9 jogadas possíveis no tabuleiro.
    tabuleiro = tabuleiro do jogo.
    jogador1 = primeiro jogador coma variável definida.
    jogador2 = segundo jgoador com a variável definida.
    ganhador = ganhado em branco, para receber a função de verificação do
    ganhador.
    Obs: Essa função chamam as demais funções do jogo.
    """
    for i in range(1, 10):
        print('{}{}{}'.format('.', '-'*40, '.'))
        print('{}{:>17}° Jogada{:>16}'.format('|', i, '|'))
        print('{}{}{}'.format("'", '-'*40, "'"))
        if i % 2 == 1:
            tabuleiro = efetuar_jogada(jogador1, tabuleiro)
            jogador = jogador1
        elif i % 2 == 0:
            tabuleiro = efetuar_jogada(jogador2, tabuleiro)
            jogador = jogador2
        if i >= 5:
            ganhador = verificar_ganhador(tabuleiro, jogador)
            if ganhador == 'X' or ganhador == 'O':
                break
    definir_ganhador(ganhador, jogador1, jogador2)


def log_jogada(jogador, linha, coluna):
    """
    Função para exibir as jogadas de cada jogador.
    jogador = jogador respectivamente da jogada atual.
    linha = linha escolhida do tabuleiro.
    coluna = escolhida do tabuleiro.
    """
    print('O jogador {} realizou a jogada.'.format(jogador))
    print('Na linha {} e Coluna {}.'.format(linha, coluna))


def mostrar_tabuleiro(tab):
    """
    Função para exibir o tabuleiro atualizado.
    tab = tabuleiro atual no momento que chamar a função.
    """
    print('\n')
    print('\t  {}  |  {}  |  {} '.format(tab[0][0], tab[0][1], tab[0][2]))
    print('\t-----|-----|-----')
    print('\t  {}  |  {}  |  {} '.format(tab[1][0], tab[1][1], tab[1][2]))
    print('\t-----|-----|-----')
    print('\t  {}  |  {}  |  {} '.format(tab[2][0], tab[2][1], tab[2][2]))
    print('\n')


def mostrar_tabuleiro_inicial():
    """
    Função para exibir o tabuleiro inicial com as
    numerações de linha e coluna respectivamente de cada posição.
    """
    print('\n')
    print('\t  {}  |  {}  |  {} '.format('00', '01', '02'))
    print('\t------|------|------')
    print('\t  {}  |  {}  |  {} '.format('10', '11', '12'))
    print('\t------|------|------')
    print('\t  {}  |  {}  |  {} '.format('20', '21', '22'))
    print('\n')


def verificar_jogada(linha, coluna, tabuleiro):
    """
    Função para verificar se a jogada é possível.
    linha = linha da jogada.
    coluna = coluna da jogada.
    tabuleiro = do jogo.
    return a permissão da jogada, 0 não permitida e 1 para permitida.
    """
    permissao = 0
    if tabuleiro[linha][coluna] in 'xX' or tabuleiro[linha][coluna] in 'oO':
        print('Jogada não permitida.')
    else:
        permissao = 1
    return permissao


def verificar_ganhador(t, jog):
    """
    Função para verificar o ganhador.
    t = tabuleiro do jogo.
    jogador = jogado da rodada.
    return o ganhador, caso há.
    """
    ganhador = ''
    # Verificando Colunas:
    if (t[0][0] == jog and t[1][0] == jog and t[2][0] == jog) \
        or (t[0][1] == jog and t[1][1] == jog and t[2][1] == jog) \
            or (t[0][2] == jog and t[1][2] == jog and t[2][2] == jog):
        ganhador = jog
    # Verificando Linhas:
    elif (t[0][0] == jog and t[0][1] == jog and t[0][2] == jog) \
        or (t[1][0] == jog and t[1][1] == jog and t[1][2] == jog) \
            or (t[2][0] == jog and t[2][1] == jog and t[2][2] == jog):
        ganhador = jog
    # Verificando Diagonais:
    elif (t[0][0] == jog and t[1][1] == jog and t[2][2] == jog) \
            or (t[2][0] == jog and t[1][1] == jog and t[0][2] == jog):
        ganhador = jog
    else:
        ganhador = 'NaN'
    return ganhador.upper()
