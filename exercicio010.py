"""exercicio010.py em 2018-09-30. Projeto Practice Python.

Pegue duas listas, digamos, por exemplo, estas duas:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
e escreva um programa que retorne uma lista que contenha apenas os elementos comuns entre as listas
(sem duplicatas). Verifique se o seu programa funciona em duas listas de tamanhos diferentes.

"""
from random import sample
from cicero import cabecalho


def intersecao(a: list, b: list) -> object:
    """Faz a interseção entre dois conjuntos

    :param a: lista
    :type a: list
    :param b: lista
    :type b: list
    :return: lista com a interseção
    :rtype: object
    """
    return print(f'Conjunto a = {a}\nConjunto b = {b}\nInterseção = {list(set(a) & set(b))}')


if __name__ == '__main__':
    cabecalho('List Overlap Comprehensions')
    lista1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    lista3 = sample(range(30), 10)
    lista4 = sample(range(30), 12)
    intersecao(lista1, lista2)

#
# https://docs.python.org/3/tutorial/datastructures.html#sets
#
# 5.4. Sets
#
# O Python também inclui um tipo de dados para conjuntos.
# Um conjunto é uma coleção não ordenada sem elementos duplicados.
# Usos básicos incluem testes de associação e eliminação de entradas duplicadas.
# Os objetos do conjunto também suportam operações matemáticas como:
#  união(|), interseção(&), diferença(-) e diferença simétrica(^).
#
# Chaves ou a função set() podem ser usadas para criar conjuntos.
# Nota: para criar um conjunto vazio, você deve usar set() e não {}; o segundo cria um dicionário vazio.
#
#
# Aqui está uma breve demonstração:
#
# >>> cesta = {'maçã', 'laranja', 'maçã', 'pera', 'laranja', 'banana'}
# >>> print (cesta)                     # mostra que as duplicatas foram removidas
# {'laranja', 'banana', 'pera', 'maçã'}
# >>> 'laranja' in cesta                # teste de associação rápida
# True
# >>> 'uva' in cesta
# False
#
# >>> # Demonstrar operações de conjunto em letras únicas de duas palavras
# ...
# >>> a = set ('abracadabra')
# >>> b = set ('alacazam')
# >>> a                                 # letras únicas em a
# {'a', 'r', 'b', 'c', 'd'}
# >>> b                                 # letras únicas em b
# {'z', 'm', 'a', 'c', 'l'}
# >>> a - b                             # letras em a mas não em b (diferença (a - b))
# {'r', 'd', 'b'}
# >>> a | b                             # letras em a ou b ou ambos (união (a U b))
# {'a, c, r, d, b, m, z, l
# >>>a & b                              # letras em a e b (interseção (a ∩ b))
# {'a', 'c'}
# >>> a ^ b                             # letras em a ou b mas não em ambos (diferença simétrica (a ∆ b))
# {'r', 'd', 'b', 'm', 'z', 'l'}
