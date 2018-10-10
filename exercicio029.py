"""exercicio029.py em 2018-10-07. Projeto Practice Python.

Desenhe o tabuleiro do jogo-da-velha verificando se o jogo tem um vencedor
Lidar com um movimento do jogador da entrada do usuário
O próximo passo é juntar todos esses três componentes para criar um jogo-da-velha para dois jogadores.
Seu desafio neste exercício é usar as funções desses exercícios anteriores, todas juntas no mesmo programa,
para criar um jogo para dois jogadores que você possa jogar com um amigo.

Aqui estão algumas coisas para manter em mente:

Você deve acompanhar quem ganhou - Se houver um vencedor, mostre uma mensagem de congratulações na tela.
Se não houver mais movimentos, não peça a jogada do próximo jogador!
Como bônus, você pode perguntar aos jogadores se eles querem jogar novamente e manter um registro de quem ganhou mais,
Jogador 1 ou Jogador 2.

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

    def campeoes():
        """Exibe o resultado final

        """
        cabecalho('Resultado final', 30, '-')
        for k, v in campeao.items():
            print(f'{k} -> {v}.'.title())

    def limpa(j: list, c: int, jg: str) -> object:
        """Limpa as variáveis para um novo jogo

        :param j: tabuleiro limpo
        :type j: list
        :param c: limpa contador
        :type c: int
        :param jg: jogador padrão para início de jogo
        :type jg: str
        :return: variáveis limpas
        :rtype: object
        """
        j = [['-' for x in range(3)] for y in range(3)]  # monta a lista
        c = 0
        jg = 'X'
        return j, c, jg

    jogo = [['-' for x in range(3)] for y in range(3)]  # monta a lista
    conta = 0
    jogador = 'X'
    campeao = {'X': 0, 'O': 0, 'empate': 0}
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
                    campeao[jogador] += 1
                    pergunta = str(input('Continuar? [Sim / qualquer tecla sair] ')).strip().lower()[0]
                    if pergunta == 's':
                        jogo, conta, jogador = limpa(jogo, conta, jogador)
                        continue
                    else:
                        campeoes()
                        break

                jogador = inverte(jogador)

                conta += 1
                if conta == 9:
                    cabecalho('Ocorreu um empate', 30, '-')
                    campeao['empate'] += 1
                    pergunta = str(input('Continuar? [Sim / qualquer tecla sair] ')).strip().lower()[0]
                    if pergunta == 's':
                        jogo, conta, jogador = limpa(jogo, conta, jogador)
                        continue
                    else:
                        campeoes()
                        break
            else:
                print(f'\n{cores("vermelho")}Esta coordenada já foi preenchida.{cores("limpa")} tente novamente!\n')
        except (ValueError, IndexError):
            print(f'{cores("vermelho")}')
            print('Erro! Digite uma coordenada válida como "3,1".')
            print(f'{cores("limpa")}')


if __name__ == '__main__':
    cabecalho('Jogo-da-Velha')
    jogar()
