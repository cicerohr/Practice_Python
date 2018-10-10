"""exercicio022.py em 2018-10-02. Projeto Practice Python.

Dado um arquivo .txt que tem uma lista de vários nomes, conte quantos de cada nome há no arquivo e
imprima os resultados na tela.

Extra:

Em vez de usar o arquivo .txt acima (ou em vez de, se você quiser o desafio),
pegue este arquivo .txt e conte quantas de cada “categoria” de cada imagem existem.
Esse arquivo de texto é, na verdade, uma lista de arquivos correspondentes ao banco de dados
de reconhecimento de cena do banco de dados SUN e lista a hierarquia de diretórios de arquivos para as imagens.
Uma vez que você dê uma olhada na primeira ou duas linhas do arquivo, ficará claro qual parte
representa a categoria da cena. Para fazer isso, você precisará lembrar um pouco sobre a análise
de strings no Python 3.

"""
from cicero import cabecalho


def ler_arquivo():
    counter_dict = {}
    with open('txt/Training_01.txt') as f:
        line = f.readline()
        while line:
            line = line[3:-26]
            if line in counter_dict:
                counter_dict[line] += 1
            else:
                counter_dict[line] = 1
            line = f.readline()
    print(counter_dict)

    # with open('txt/nomes.txt', 'r', encoding="utf8") as f:
    #     contador = 0
    #     for linha in f:
    #         contador += 1
    # return print(contador)


if __name__ == '__main__':
    cabecalho('Ler do arquivo')
    ler_arquivo()
