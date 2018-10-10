"""exercicio021.py em 2018-10-02. Projeto Practice Python.

Pegue o código do exercício Decodificar uma página da web e, em vez de imprimir os resultados em uma tela,
escreva os resultados para um arquivo txt.
Em seu código, basta criar um nome para o arquivo para o qual você está salvando.

Extras:

Peça ao usuário para especificar o nome do arquivo de saída que será salvo.

"""
import requests
from bs4 import BeautifulSoup
from cicero import cabecalho


def grava_arquivo():
    """Cria e grava um arquivo

    """
    url = 'http://www.nytimes.com/'
    titulos = []
    soup = BeautifulSoup(requests.get(url).text, features='html.parser')
    titulo = soup.findAll('h2', {'class': 'css-78b01r esl82me2'})
    arquivo = open(f'txt/{input("Digite o nome do arquivo: ")}', 'w', encoding="utf8")

    for linha in titulo:
        titulos.append(linha.text + '\n')

    arquivo.writelines(titulos)
    arquivo.close()


if __name__ == '__main__':
    cabecalho('Escreva em um arquivo')
    grava_arquivo()
