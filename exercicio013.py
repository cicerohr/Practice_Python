"""exercicio013.py em 2018-09-30. Projeto Practice Python.

Escreva um programa que pergunte ao usuário quantos números de Fibonacci serão gerados.
Aproveite esta oportunidade para pensar sobre como você pode usar funções.
Certifique-se de pedir ao usuário para inserir o número de números na seqüência para gerar.
(Dica: A seqüência Fibonacci é uma seqüência de números onde o próximo número na seqüência
é a soma dos dois números anteriores na seqüência. é assim: 1, 1, 2, 3, 5, 8, 13,…)
                                                               a +b =c

"""
from cicero import cabecalho


def fibonacci(numero: int) -> str:
    """Gera uma sequência de Fibonacci

    :param numero: quantidade de números da sequência
    :type numero: int
    :return: sequência
    :rtype: str
    """
    # valores iniciais
    a = b = 1
    sequencia = '1 -> 1 -> '
    for x in range(1, numero - 1):
        c = a + b
        a = b
        b = c
        if x == (numero - 2):
            sequencia += f'{c}'
        else:
            sequencia += f'{c} -> '
    return sequencia


def fibonacci_n(n: int) -> object:
    """Retorna o Fn da sequência de Fibonacci (Fn = Fn-1 + Fn-2)

    :param n: n-ésimo número
    :type n: int
    :return: n-ésimo número da sequência
    :rtype: object
    """
    if n < 2:
        return n
    else:
        return fibonacci_n(n - 1) + fibonacci_n(n - 2)


if __name__ == '__main__':
    cabecalho('Fibonacci')
    print(fibonacci(int(input('Quantos números da sequência você deseja ver? '))))
    print(fibonacci_n(int(input('N-ésimo número da sequência: '))))
