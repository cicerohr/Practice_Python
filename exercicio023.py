"""exercicio023.py em 2018-10-02. Projeto Practice Python.

Dados dois arquivos .txt que possuem listas de números, encontre os números sobrepostos.
Um arquivo .txt tem uma lista de todos os números primos abaixo de 1000, e o outro arquivo .txt
tem uma lista de números felizes até 1000 (https://pt.wikipedia.org/wiki/Número_feliz).

"""
from cicero import cabecalho


def cria_lista(arquivo: str) -> list:
    """Lê o arquivo de números e o converte em uma lista

    :param arquivo: nome com caminho
    :type arquivo: str
    :return: lista com números inteiros
    :rtype: list
    """
    lista = []
    with open(arquivo, 'r', encoding="utf8") as f:
        line = f.readline()
        z = True
        while line:
            # obs.: os arquivos foram gravados em encoding utf-8; se for gravado em ansi não é necessário a linha abaixo
            # retira caracteres de encoding no início da primeira linha
            if z:
                line = line[1:]
                z = False
            # converte string para inteiro e adiciona na lista
            lista.append(int(line))
            line = f.readline()
        print(lista)
    return lista


def overlap(a: str, b: str) -> list:
    """Faz a verificação da intersecção entre dois conjuntos

    :return: lista ordenada
    :rtype: list
    """
    return sorted(list(set(cria_lista(a)) & set(cria_lista(b))))


if __name__ == '__main__':
    cabecalho('Sobreposição em arquivos')
    primos = 'txt/numerosPrimos.txt'
    felizes = 'txt/numerosFelizes.txt'
    print(overlap(primos, felizes))
