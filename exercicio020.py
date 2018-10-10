"""exercicio020.py em 2018-10-02. Projeto Practice Python.

Escreva uma função que receba uma lista ordenada de números
(uma lista onde os elementos estão em ordem, do menor para o maior).
A função decide se o número especificado está dentro da lista e retorna (e imprime) um booleano apropriado.

Extras:

Use busca binária.

"""
from cicero import cabecalho


def buscador(numero: int, lista: list) -> object:
    """Verificador se um número existe em uma lista

    :param numero: número a ser verificado
    :type numero: int
    :param lista: lista com os números
    :type lista: list
    :return: objeto com a verificação booleana
    :rtype: object
    """
    lista_bin = []
    # converte a lista para binario
    for y in range(len(lista)):
        lista_bin.append(bin(y))

    return f'O número {numero} esta na lista? {True if bin(numero) in lista_bin else False}'


if __name__ == '__main__':
    cabecalho('Pesquisa de elemento')
    numeros = list(range(10))
    print(numeros)
    print(buscador(0, numeros))
    print(buscador(1, numeros))
    print(buscador(9, numeros))
    print(buscador(10, numeros))
