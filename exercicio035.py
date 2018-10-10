"""exercicio035.py em 2018-10-09. Projeto Practice Python.

No exercício anterior, salvamos informações sobre nomes e aniversários de cientistas famosos em disco.
Neste exercício, carregue esse arquivo JSON do disco, extraia os meses de todos os aniversários e
conte quantos cientistas têm um aniversário em cada mês.

Seu programa deve produzir algo como:

{
"Maio": 3,
"Novembro": 2,
"Dezembro": 1
}

"""
import json
from collections import Counter
from cicero import cabecalho


def meses():
    """Conta a ocorrência de meses dentro do arquivo Json

    """
    # lê o arquivo Json e armazena em um dicionário
    with open('json/cientistas.json', 'r') as f:
        cientistas = json.load(f)

    lista = []
    # carrega somente os meses para uma lista
    for v in cientistas.values():
        lista.append(str(v).split(' ')[2])

    # faz a contagem de ocorrência dos meses
    print(Counter(lista))

    # faz a contagem de ocorrência dos meses (mais elegante)
    for x, y in Counter(lista).items():
        print(f'{x.rjust(9)}: {y}')


if __name__ == '__main__':
    cabecalho('Meses de aniversário')
    meses()
