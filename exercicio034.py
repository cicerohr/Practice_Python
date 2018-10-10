"""exercicio034.py em 2018-10-09. Projeto Practice Python.

No exercício anterior, criamos um dicionário de aniversários de cientistas famosos.
Neste exercício, modifique seu programa para carregar o dicionário de aniversário de um arquivo JSON no disco,
em vez de ter o dicionário definido no programa.

Bônus: peça ao usuário o nome de outro cientista e o aniversário para adicioná-lo ao dicionário
e atualize o arquivo JSON que você tem no disco com o nome do cientista.
Se você executar o programa várias vezes e continuar adicionando novos nomes,
seu arquivo JSON deverá ficará cada vez maior.

"""
import json
from cicero import cabecalho


def lista_dados(dicionario: dict):
    """Lista as informações do arquivo Json a partir de um dicionário

    :param dicionario: informações do arquivo Json
    :type dicionario: dict
    """
    print()
    for k in dicionario:
        print(f'{str(k).center(60)}')
    print()


def adiciona(dicionario: dict):
    """Adiciona dados no arquivo Json

    :param dicionario: informações lidas do arquivo Json
    :type dicionario: dict
    """
    while True:
        nome = str(input('Nome: ')).strip()
        nascimento = str(input('Nascimento: ')).strip()
        dicionario[nome] = nascimento
        with open('json/cientistas.json', 'w') as f:
            json.dump(dicionario, f)
        print(f'\n{nome} foi adicionado com sucesso.\n')
        pergunta = str(input('Quer adicionar outro cientista? {S/N] \n')).lower().strip()[0]
        if pergunta == 's':
            continue
        else:
            break
    return None


def aniversario(dicionario: dict) -> object:
    """Retorna a consulta no arquivo Json

    :param dicionario: dados do arquivo Json
    :type dicionario: dict
    :return: resultado da pesquisa
    :rtype: object
    """
    nome = str(input('Aniversário de quem você quer saber? ')).strip()
    return f'\n{nome} nasceu em {dicionario.get(nome, f"(sem informações)")}.\n'


def opcoes():
    """Gera as opções para o usuário a partir de um dicionário

    """
    dicionario = {'L': 'Lista os cientistas',
                  'N': 'Mostra a data de nascimento',
                  'A': 'Adiciona mais um cientista',
                  'S': 'Sai do programa'}
    print(' Opções: '.center(30, '-'))
    for k, v in dicionario.items():
        print(f'{k} -> {v}')


def aniversarios():
    """Manipula um arquivo Json (escrita/leitura)

    """
    # lê o arquivo Json e armazena em um dicionário
    with open('json/cientistas.json', 'r') as f:
        cientista = json.load(f)
    cabecalho('Bem-vindo ao dicionário de aniversários. Nós sabemos a data de nascimento de:', 60, ' ')
    lista_dados(cientista)

    while True:
        opcoes()
        pergunta = str(input('\tQual é a sua opção? ')).lower().strip()[0]
        if pergunta == 'l':
            lista_dados(cientista)
        elif pergunta == 'n':
            print(aniversario(cientista))
        elif pergunta == 'a':
            print(adiciona(cientista))
            lista_dados(cientista)
        else:
            cabecalho('Fim', 30, '-')
            break


if __name__ == '__main__':
    cabecalho('Aniversário Com Json')
    aniversarios()
