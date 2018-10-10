"""exercicio007.py em 2018-09-30. Projeto Practice Python.

Digamos que eu forneça uma lista salva em uma variável: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
Escreva uma linha de Python que pegue esta lista e faça uma nova lista que tenha apenas os elementos pares dessa lista.

"""
from cicero import cabecalho


def lista(a: list) -> object:
    """
    a =  = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    b = []
    for i in a:
        if i % 2 == 0:
            b.append(i)
    print(b)

        ou em List Comprehensions

    print([i for i in a if i % 2 == 0])

    :param a: lista
    :type a: list
    :return: resultado da List Comprehensions
    :rtype: object
    """
    return print([i for i in a if i % 2 == 0])


if __name__ == '__main__':
    cabecalho('List Comprehensions')
    c = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    lista(c)
    d = list(range(1, 11))
    lista(d)

    #
    # https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    #
    # List Comprehensions fornece uma maneira concisa de criar listas.
    # Aplicações comuns são para fazer novas listas onde cada elemento é o resultado de algumas operações aplicadas
    # a cada membro de outra seqüência ou iterável, ou para criar uma subsequência daqueles elementos que satisfazem
    # uma determinada condição.
    #
    # Por exemplo, suponha que queremos criar uma lista de quadrados, como:
    #
    # >>>
    # >>> quadrados = []
    # >>> for x in range(10):
    # ...     quadrados.append (x ** 2)
    # ...
    # >>> quadrados
    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    #
    # Observe que isso cria (ou sobrescreve) uma variável chamada x que ainda existe após a conclusão do loop.
    # Podemos calcular a lista de quadrados da mesma forma usando:
    #
    # quadrados = list(map(lambda x: x ** 2, range(10)))
    #
    # ou equivalente:
    #
    # quadrados = [x ** 2 for x in range(10)]
    # que é mais conciso e legível.
