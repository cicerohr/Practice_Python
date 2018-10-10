"""exercicio006.py em 2018-09-29. Projeto Practice Python.

Peça ao usuário uma string e imprima se essa string é um palíndromo ou não.
(Um palíndromo é uma string que se lê de trás para frente e de frente para trás.)

"""
from cicero import cabecalho


def palindromo() -> object:
    """Verifica se o inverso da palavra/frase é igual

    :return: impressão do resultado
    :rtype: object
    """
    palavra = str(input('Digite uma palavras: ')).strip().lower().replace(' ', '')
    if palavra == palavra[::-1]:
        return print(f'A palavra {palavra} é um palíndromo.')
    else:
        return print(f'A palavra {palavra} NÃO é um palíndromo.')


if __name__ == '__main__':
    cabecalho('Palíndromo')
    palindromo()
