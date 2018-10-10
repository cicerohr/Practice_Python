"""exercicio026.py em 2018-10-05. Projeto Practice Python.

O jogo-da-velha é representado como uma lista de listas, da seguinte forma:

jogo = [[1, 2, 0],
        [2, 1, 0],
        [2, 1, 1]]

onde um '0' significa um quadrado vazio, o '1' significa que o jogador 1 ocupou o espaço e
o '2' significa que o jogador 2 ocupou o espaço.

Sua tarefa: dada uma lista de 3 por 3 de listas, que representa um tabuleiro do jogo-da-velha,
diga-me se alguém ganhou, e me diga qual jogador ganhou, se houver.
Para ganha no jogo-da-velha é necessário ocupar 3 espaços; seja na linha, na coluna ou na diagonal.
Não se preocupe com o caso em que DUAS pessoas ganhem; presuma que em todas as jogadas haverá apenas um vencedor.

Aqui estão mais alguns exemplos para trabalhar:

vencedor_2 = [[2, 2, 0],
              [2, 1, 0],
              [2, 1, 1]]

vencedor_1 = [[1, 2, 0],
              [2, 1, 0],
              [2, 1, 1]]

vencedor_1_novamente = [[0, 1, 0],
                        [2, 1, 0],
                        [2, 1, 1]]

sem_vencedor_1 = [[1, 2, 0],
                  [2, 1, 0],
                  [2, 1, 2]]

sem_vencedor_2 = [[1, 2, 0],
                  [2, 1, 0],
                  [2, 1, 0]]

"""
from cicero import cabecalho


def jogar(tabuleiro: list) -> str:
    """Analise tabuleiro do jogo-da-velha

    :param tabuleiro: lista com as jogadas
    :type tabuleiro: list
    :return: o resultado
    :rtype: str
    """
    # linhas
    for x in range(3):
        linha = {tabuleiro[x][0], tabuleiro[x][1], tabuleiro[x][2]}
        if len(linha) == 1 and tabuleiro[x][0] != 0:
            return f'Vencedor: jogador {tabuleiro[x][0]}'

    # colunas
    for x in range(3):
        coluna = {tabuleiro[0][x], tabuleiro[1][x], tabuleiro[2][x]}
        if len(coluna) == 1 and tabuleiro[0][x] != 0:
            return f'Vencedor: jogador {tabuleiro[0][x]}'

    # diagonais
    diagonal_1 = {tabuleiro[0][0], tabuleiro[1][1], tabuleiro[2][2]}
    diagonal_2 = {tabuleiro[0][2], tabuleiro[1][1], tabuleiro[2][0]}
    if (len(diagonal_1) == 1 or len(diagonal_2) == 1) and tabuleiro[1][1] != 0:
        return f'Vencedor: jogador {tabuleiro[1][1]}'

    return f'Não houve vencedores'


if __name__ == '__main__':
    cabecalho('jogo-da-velha')
    vencedor_1 = [[1, 2, 0],
                  [2, 1, 0],
                  [2, 1, 1]]

    vencedor_1_1 = [[1, 1, 1],
                    [2, 2, 0],
                    [2, 1, 2]]

    vencedor_1_2 = [[0, 1, 0],
                    [2, 1, 0],
                    [2, 1, 1]]

    vencedor_2 = [[2, 2, 0],
                  [2, 1, 0],
                  [2, 1, 1]]

    sem_vencedor_1 = [[1, 2, 0],
                      [2, 1, 0],
                      [2, 1, 2]]

    sem_vencedor_2 = [[1, 2, 0],
                      [2, 1, 0],
                      [2, 1, 0]]

    print(jogar(vencedor_2))
