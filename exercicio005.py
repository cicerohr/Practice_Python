"""exercicio005.py em 2018-09-29. Projeto Practice Python.

Pegue duas listas, digamos, por exemplo, estas duas:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
e escreva um programa que retorne uma lista que contenha apenas os elementos comuns entre as listas (sem duplicatas).
Verifique se o seu programa funciona em duas listas de tamanhos diferentes.

Extras:

Aleatoriamente, gere duas listas para testar
Escreva isso em uma linha do Python.
Listar propriedades

"""
from random import sample
from cicero import cabecalho


def sobrepor(lista1: list, lista2: list) -> object:
    """verifica itens iguais entre duas listas

    :param lista1: uma lista
    :type lista1: list
    :param lista2: uma lista
    :type lista2: list
    :return: imprime lista com sobreposição
    :rtype: object
    """
    lista = []
    for item in lista1:  # carrega lista1 em item
        if item in lista2:  # compara item com lista2
            if item not in lista:  # verifica se o item não esta na lista para não repetir
                lista.append(item)

    return print(f'Lista a = {lista1}\nLista b = {lista2}\nLista sobreposta = {lista}')


if __name__ == '__main__':
    cabecalho('Solução para sobreposição de lista')
    a = sample(range(30), 10)
    b = sample(range(30), 12)
    sobrepor(a, b)

    #
    #
    cabecalho('Alternativa')
    print(f'>>> print(list(set(sample(range(30), 10)) & set(sample(range(30), 12))))')
    #
    # a1 = set(sample(range(30), 10))
    # a2 = set(sample(range(30), 12))
    # lista = list(a1 & a2)
    # print(a1)
    # print(a2)
    # print(lista)
    print(list(set(sample(range(30), 10)) & set(sample(range(30), 12))))

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
    # >>> # TODO Demonstrar operações de conjunto em letras únicas de duas palavras
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
