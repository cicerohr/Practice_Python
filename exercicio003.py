"""exercicio003.py em 2018-09-29. Projeto Practice Python.

lista de números, operador condicional if

Pegue uma lista, por exemplo:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
e escreva um programa que imprima todos os elementos da lista menores que 5.

Extras:

1. Em vez de imprimir os elementos um por um, crie uma nova lista que tenha todos os elementos menores que 5
dessa lista e imprima essa nova lista.
2. Escreva isso em uma linha do Python.
3. Peça ao usuário um número e retorne uma lista que contenha apenas elementos da lista original que sejam menores que
aquele dado pelo usuário.

"""
from cicero import cabecalho


def menor_que(numero: int) -> object:
    """Verifica se o número é maior que o conteúdo da lista

    :param numero: entrada do usuário
    :type numero: int
    :return: imprime uma lista com os números menores que o número
    :rtype: object
    """
    lista = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    n_lista = []
    for i in lista:
        if numero > i:
            n_lista.append(i)
    return print(n_lista)


if __name__ == '__main__':
    cabecalho('Listar menor que')
    menor_que(int(input('Digite um número inteiro: ')))
