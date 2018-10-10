"""exercicio019.py em 2018-10-02. Projeto Practice Python.

Usando as solicitações e as bibliotecas do BeautifulSoup Python, imprima na tela o texto completo do artigo
neste site: http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.

O artigo é longo, então é dividido entre 4 páginas.
Sua tarefa é imprimir o texto na tela para que você possa ler o artigo completo sem ter que clicar em nenhum botão.

Isso apenas imprimirá o texto completo do artigo na tela.
Não facilitará a leitura, portanto, no próximo exercício, aprenderemos a escrever esse texto em um arquivo .txt.

url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
titulos = []

soup = BeautifulSoup(requests.get(url).text, features='html.parser')
titulo = soup.findAll('section', {'class': 'content-section'})
for linha in titulo:
    titulos.append(linha.text)

"""
#
#
import requests
from bs4 import BeautifulSoup
from cicero import cabecalho

if __name__ == '__main__':
    cabecalho('Decodificar uma página da Web 2')
