"""exercicio012.py em 2018-09-30. Projeto Practice Python.

Escreva um programa que tenha uma lista de números (por exemplo, a = [5, 10, 15, 20, 25]) e
faça uma nova lista apenas com o primeiro e o último elemento da lista dada.
Para praticar, escreva este código dentro de uma função.

"""
from cicero import cabecalho


def extremos_lista(lista: list) -> list:
    """retorna uma lista com o primeiro e o último elemento

    :param lista: uma lista
    :type lista: list
    :return: lista com com os dois itens
    :rtype: list
    """
    return [lista[0], lista[-1]]


if __name__ == '__main__':
    cabecalho('Fim da lista')
    a = [5, 10, 15, 20, 25]
    print(extremos_lista(a))
