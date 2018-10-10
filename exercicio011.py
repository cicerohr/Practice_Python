"""exercicio011.py em 2018-09-30. Projeto Practice Python.

Peça ao usuário um número e determine se o número é primo ou não.

"""
from cicero import cabecalho


def eh_primo(numero: int) -> object:
    """Verifica se um número é primo

    :param numero: entrada usuário
    :type numero: int
    :return: imprime mensagem para o usuário
    :rtype: object
    """
    conta = 0
    for x in range(1, numero + 1):
        if numero % x == 0:
            conta += 1
    if conta == 2:
        return print(f'O número {numero} é primo.')
    else:
        return print(f'O número {numero} NÃO é primo.')


if __name__ == '__main__':
    cabecalho('Números Primos')
    eh_primo(int(input('Digite um número: ')))
