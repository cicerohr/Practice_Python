"""exercicio004.py em 2018-09-29. Projeto Practice Python.

Crie um programa que peça ao usuário um número e depois imprima uma lista de todos os divisores desse número.
(Se você não sabe o que é um divisor, é um número que divide uniformemente em outro número.
Por exemplo, 13 é um divisor de 26 porque 26/13 não tem nenhum resto.)

"""
from cicero import cabecalho


def divisor(numero: int) -> object:
    """Verifica todos os divisores do número

    :param numero: entrada do usuário
    :type numero: int
    :return: imprime uma lista com todos os divisores
    :rtype: object
    """
    divisores = []
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores.append(i)
    return print(f'{numero} é divisível por {divisores}')


if __name__ == '__main__':
    cabecalho('Divisores')
    divisor(int(input('Digite um número: ')))
