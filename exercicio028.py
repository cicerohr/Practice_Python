"""exercicio028.py em 2018-10-07. Projeto Practice Python.

Implemente uma função que tome como entrada três variáveis ​​e retorne a maior das três.
Faça isso sem usar a função max() do Python!

O objetivo deste exercício é pensar em alguns internos que o Python normalmente cuida de nós.
Tudo que você precisa é de algumas variáveis ​​e declarações if!

"""
from cicero import cabecalho


def maior(a: int, b: int, c: int) -> str:
    """Verifica o maior de três termos

    :param a: entrada usuário
    :type a: int
    :param b: entrada usuário
    :type b: int
    :param c: entrada usuário
    :type c: int
    :return: resultado da verificação
    :rtype: str
    """
    if b <= a >= c:
        return f'Entre {a},{b} e {c}; {a} é o maior.'
    elif a <= b >= c:
        return f'Entre {a},{b} e {c}; {b} é o maior.'
    else:
        return f'Entre {a},{b} e {c}; {c} é o maior.'


if __name__ == '__main__':
    cabecalho('Maior de três')
    print(maior(3, 2, 4))
    print(maior(3, 2, 3))
    print(maior(3, 3, 2))
    print(maior(3, 3, 3))
