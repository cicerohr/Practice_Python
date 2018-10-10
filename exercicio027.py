"""exercicio027.py em 2018-10-05. Projeto Practice Python.

Em um exercício anterior, exploramos a ideia de usar uma lista de listas como uma “estrutura de dados” para armazenar
informações sobre um jogo-da-velha.
No jogo-da-velha, o “servidor de jogo” precisa saber onde os Xs e Os estão no tabuleiro,
para saber se o jogador 1 ou o jogador 2 (ou quem é X ou O) ganhou.

Também tem um exercício sobre como desenhar o tabuleiro de jogo-da-velha usando caracteres de texto.

O próximo passo lógico é lidar com a manipulação da entrada do usuário.
Quando um jogador (digamos, jogador 1, quem é X) quer colocar um X na tela,
ele não pode simplesmente clicar em um terminal.
Então, vamos aproximar esse clique simplesmente pedindo ao usuário uma coordenada de onde deseja colocar a peça.

Como lembrete, o nosso jogo-da-velha é realmente uma lista de listas. O jogo começa com um tabuleiro vazio como este:

jogo = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

O computador pergunta ao jogador 1 (X) qual é o movimento dele (no formato linha, coluna) e ele digita 1, 3.
Então o jogo seria impresso

jogo = [[0, 0, X],
        [0, 0, 0],
        [0, 0, 0]]

E pergunte ao Jogador 2 por sua jogada, imprimindo um O naquele lugar.

Coisas para observar:

Para este exercício, assuma que o jogador 1 (o primeiro jogador a se mover) será sempre X e
o jogador 2 (o segundo jogador) será sempre O.
Observe como no exemplo eu dei coordenadas para onde eu quero mover a partir de (1, 1) em vez de (0, 0).
Para as pessoas que não programam, começar a contar com 0 é um conceito estranho,
então é melhor para a experiência do usuário se a contagem de linhas e contagens de coluna começarem em 1.
Isso não é necessário, mas da maneira que você escolher para implementar , deve ser explicado ao jogador.
Peça ao usuário para inserir as coordenadas no formulário “linha, coluna” - um número, depois uma vírgula e,
em seguida, um número. Então você pode usar suas habilidades em Python para descobrir em qual linha e coluna
elas querem que sua parte esteja.
Não se preocupe em verificar se alguém ganhou o jogo, mas se um jogador tentar colocar uma peça em uma posição do jogo
onde já existe outra peça, não permita que esta peça seja colocada.

Bônus:
Para o exercício "padrão", não se preocupe em "encerrar" o jogo - não é necessário acompanhar quantos quadrados estão
cheios. Em uma versão bônus, acompanhe quantos quadrados estão cheios e pare automaticamente de pedir movimentos
quando não houver mais movimentos válidos.

"""
from cicero import cabecalho, cores


def jogar():
    """Preenchimento do tabuleiro do jogo-da-velha e verificação do vencedor

    """

    def vencedor(v: str) -> bool:
        """Verifica o ganhador do jogo-da-velha

        :param v: string do vencedor
        :type v: str
        :return: booleano
        :rtype: bool
        """
        if jogo[0] == [v, v, v] or jogo[1] == [v, v, v] or jogo[2] == [v, v, v]:  # linhas
            return True
        elif jogo[0][0] == v and jogo[1][0] == v and jogo[2][0] == v:  # coluna
            return True
        elif jogo[0][1] == v and jogo[1][1] == v and jogo[2][1] == v:  # coluna
            return True
        elif jogo[0][2] == v and jogo[1][2] == v and jogo[2][2] == v:  # coluna
            return True
        elif jogo[0][0] == v and jogo[1][1] == v and jogo[2][2] == v:  # diagonal
            return True
        elif jogo[0][2] == v and jogo[1][1] == v and jogo[2][0] == v:  # diagonal
            return True
        else:
            return False

    def inverte(i: str) -> str:
        """Inverte o jogador

        :param i: jogador atual
        :type i: str
        :return: jogador invertido
        :rtype: str
        """
        if i == "X":
            n_jogador = 'O'
            return n_jogador
        else:
            n_jogador = 'X'
            return n_jogador

    def tabuleiro():
        """Imprime o tabuleiro do jogo-da-velha

        """
        for linhas in range(len(jogo)):
            for colunas in range(len(jogo)):
                print(jogo[linhas][colunas], end=' ')
            print()
        print()

    jogo = [['-' for x in range(3)] for y in range(3)]  # monta a lista
    conta = 0
    jogador = 'X'
    while True:
        try:
            coordenadas = str(input(f'"{jogador}" joga (linha, coluna): ')).strip()
            linha = int(coordenadas.split(',')[0]) - 1
            coluna = int(coordenadas.split(',')[1]) - 1
            if jogo[linha][coluna] not in 'XO':

                if conta % 2 == 0:
                    jogo[linha][coluna] = 'X'
                else:
                    jogo[linha][coluna] = 'O'

                tabuleiro()

                if vencedor(jogador):
                    cabecalho(f'O vencedor foi "{jogador}"', 30, '-')
                    break

                jogador = inverte(jogador)

                conta += 1
                if conta == 9:
                    cabecalho('Ocorreu um empate', 30, '-')
                    break
            else:
                print(f'\n{cores("vermelho")}Esta coordenada já foi preenchida.{cores("limpa")} tente novamente!\n')
        except ValueError:
            print(f'{cores("vermelho")}')
            print('Erro! Digite uma coordenada válida como "3,1".')
            print(f'{cores("limpa")}')


if __name__ == '__main__':
    cabecalho('jogo-da-velha')

    jogar()
