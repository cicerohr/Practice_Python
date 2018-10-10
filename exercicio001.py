"""exercicio001.py em 2018-09-29. Projeto Practice Python.

tipos de strings de entrada int

Crie um programa que peça ao usuário para inserir seu nome e sua idade. Imprima uma mensagem endereçada a eles,
informando o ano em que completará 100 anos.

"""
from datetime import datetime
from cicero import cabecalho


def idade_100(nome: str, idade: int) -> object:
    """Obtem nome e idade e retorna o ano em que fará 100 anos

    :param nome: nome do usuário
    :type nome: str
    :param idade: idade do usuário
    :type idade: int
    :return: ano em que completará 100 anos
    :rtype: object
    """
    return print(f'Olá {nome}! Você completará 100 anos em {(datetime.now().year - idade) + 100}.')


if __name__ == '__main__':
    cabecalho('Entrada de dados')
    n = str(input('Digite seu nome: '))
    i = int(input('Digite sua idade: '))
    idade_100(n, i)
