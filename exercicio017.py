"""exercicio017.py em 2018-10-01. Projeto Practice Python.

Use o BeautifulSoup e solicite pacotes Python para imprimir uma lista de todos os títulos de artigos na
página inicial do New York Times.

"""
import requests
from bs4 import BeautifulSoup
from cicero import cabecalho


def decodificador(url: str):
    """Imprime os títulos do NY Times

    :param url: endereço de pesquisa no NY Times
    :type url: str
    """
    titulos = []

    soup = BeautifulSoup(requests.get(url).text, features='html.parser')
    titulo = soup.findAll('h2', {'class': 'css-78b01r esl82me2'})
    for linha in titulo:
        titulos.append(linha.text)

    for i in range(len(titulos)):
        print(titulos[i])


if __name__ == '__main__':
    cabecalho('Decodificar uma página da web')
    decodificador('http://www.nytimes.com/')
