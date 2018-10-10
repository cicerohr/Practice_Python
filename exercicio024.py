"""exercicio024.py criado por Cicero em 2018-10-03. Projeto Practice Python.

 --- --- ---
|   |   |   |
 --- --- ---
|   |   |   |
 --- --- ---
|   |   |   |
 --- --- ---
Este é 3x3 (como no jogo-da-velha).
Obviamente, eles vêm em muitos outros tamanhos (8x8 para xadrez, 19x19 para Go e muitos mais).

Pergunte ao usuário qual tamanho do tabuleiro de jogo que ele deseja desenhar e
desenhe para ele na tela usando a declaração de impressão do Python.

Lembre-se que no Python 3, a impressão na tela é realizada por
  print ("Coisa para mostrar na tela")

Dica: isso requer algum uso de funções, como discutido anteriormente e em outros lugares na Internet,
como este link do TutorialsPoint (http://www.tutorialspoint.com/python/python_functions.htm).

"""
from cicero import cabecalho


def tabuleiro(tamanho=3):
    """Desenha um tabuleiro de jogo

    :param tamanho: dimensão do tabuleiro
    :type tamanho: int
    """
    for linha in range(tamanho):
        print(' --- ' * tamanho)
        print('|    ' * (tamanho + 1))
        if linha == tamanho - 1:
            print(' --- ' * tamanho)


def main():
    cabecalho('Desenhar tabuleiro de jogo')
    tabuleiro(int(input('Digite o tamanho do tabuleiro: ')))
    tabuleiro()
    # tabuleiro(1)
    # tabuleiro(8)
    # tabuleiro(19)
    print(__doc__)
    print(tabuleiro.__name__)
    print(tabuleiro.__defaults__)
    print(tabuleiro.__doc__)


if __name__ == '__main__':
    main()
