"""exercicio014.py em 2018-09-30. Projeto Practice Python.

Escreva um programa (função!) Que recebe uma lista e retorna uma nova lista que contém todos os elementos da
primeira lista menos os duplicados.

Extras:

Escreva duas funções diferentes para fazer isso - uma usando um loop e construindo uma lista, e
outra usando conjuntos.

"""
from cicero import cabecalho


def sem_duplicatas(lista: list) -> list:
    """Retira as duplicatas da lista com a função set()

    :param lista: entrada
    :type lista: list
    :return: lista sem duplicatas
    :rtype: list
    """
    return list(set(lista))


def sem_duplicatas2(lista: list) -> list:
    """Executa um loop para retirar as duplicatas

    :param lista: entrada
    :type lista: list
    :return: lista sem duplicatas
    :rtype: list
    """
    lista_sem_duplicatas = []
    for x in lista:
        if x not in lista_sem_duplicatas:
            lista_sem_duplicatas.append(x)
    return lista_sem_duplicatas


if __name__ == '__main__':
    cabecalho('Remover Duplicados da Lista')
    a = [1, 1, 2, 2, 3, 3]
    b = [1, 2, 3, 4, 3, 2, 1]
    print(sem_duplicatas(a))
    print(sem_duplicatas2(b))
