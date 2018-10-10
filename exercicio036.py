"""exercicio036.py em 2018-10-09. Projeto Practice Python.

No exercício anterior, contamos quantos aniversários há em cada mês em nosso dicionário de aniversários.

Neste exercício, use a biblioteca Python bokeh para traçar um histograma em que meses os cientistas têm aniversários!
Como levaria muito tempo para você inserir os meses de vários cientistas, você pode usar meu arquivo JSON
de aniversário dos cientistas. Basta analisar os meses (se você não sabe como, sugiro olhar para o exercício anterior
ou sua solução) e desenhar seu histograma.

Se você estiver usando uma interface puramente baseada na Web para codificação, este exercício não funcionará para você,
pois é necessário instalar o pacote bokeh Python.
Agora pode ser uma boa hora para instalar o Python em seu próprio computador.

"""
import json
from bokeh.plotting import figure, show, output_file
from collections import Counter
from cicero import cabecalho


def plot():
    """Faz plotagem dos dados do arquivo Json

    """
    # lê o arquivo Json e armazena em um dicionário
    with open('json/cientistas.json', 'r') as f:
        cientistas = json.load(f)

    lista = []
    x = []
    y = []
    # carrega somente os meses para uma lista
    for v in cientistas.values():
        lista.append(str(v).split(' ')[2])
    # cria listas para plotagem dos meses e ocorrências
    for k, v in Counter(lista).items():
        x.append(k)
        y.append(v)
    y = sorted(y, reverse=True)
    # cria a plotagem
    output_file('html/aniversarios.html')
    x_categories = list(Counter(lista))
    p = figure(x_range=x_categories)
    p.vbar(x=x, top=y, width=0.5)
    show(p)


if __name__ == '__main__':
    cabecalho('Aniversários')
    plot()
