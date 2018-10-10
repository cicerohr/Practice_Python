"""exercicio030.py em 2018-10-07. Projeto Practice Python.

Neste exercício, a tarefa é escrever uma função que escolha uma palavra aleatória de uma lista de palavras
do dicionário SOWPODS. Baixe este arquivo e salve-o no mesmo diretório do seu código Python.
Este arquivo é a compilação de Peter Norvig do dicionário de palavras usado em torneios profissionais de Scrabble.
Cada linha no arquivo contém uma única palavra.

Dica: use a biblioteca aleatória do Python para escolher uma palavra aleatória.

O que é o SOWPODS?
SOWPODS é uma lista de palavras comumente usada em palavras cruzadas e jogos (como o Scrabble, por exemplo).
É a combinação do Dicionário do Jogador do Scrabble e do Dicionário da Câmara.
https://en.wikipedia.org/wiki/Collins_Scrabble_Words

"""
from random import choice
from cicero import cabecalho


def palavra(nome: str) -> object:
    """Busca uma palavra aleatória em um arquivo

    :param nome: arquivo
    :type nome: str
    :return: palavra aleatória
    :rtype: object
    """
    with open(nome, 'r') as f:
        palavras = list(f)

    return choice(palavras).strip()


if __name__ == '__main__':
    cabecalho('Escolhe uma palavra')
    print(palavra('txt/sowpods.txt'))
