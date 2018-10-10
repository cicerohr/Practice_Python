"""exercicio033.py em 2018-10-09. Projeto Practice Python.

Para este exercício, acompanharemos quando são os aniversários de nossos amigos e
poderemos encontrar essas informações com base em seus nomes.
Crie um dicionário (em seu arquivo) de nomes e aniversários.
Quando você executa seu programa, ele deve pedir ao usuário para inserir um nome e retornar o aniversário
dessa pessoa. A interação deve ser algo como isto:

Bem-vindo ao dicionário de aniversários. Nós sabemos os aniversários de:
    Albert Einstein
    Benjamin Franklin
    Ada Lovelace
Aniversário de quem você quer procurar?
    Benjamin Franklin
O aniversário de Benjamin Franklin é 17/01/1706.

"""
from cicero import cabecalho


def aniversario():
    """Busca o aniversário em um dicionário

    """
    aniversarios = {'Albert Einstein': '14 de março de 1879',
                    'Benjamin Franklin': '17 de janeiro de 1706',
                    'Ada Lovelace': '10 de dezembro de 1815'}
    print('Bem-vindo ao dicionário de aniversários. Nós sabemos os aniversários de:')
    for k, v in aniversarios.items():
        print(f'\t\t\t{k}')
    nome = str(input('Aniversário de quem você quer saber? ')).strip()
    print()
    print(f'{nome} nasceu em {aniversarios.get(nome, f"(sem informações)")}.')


if __name__ == '__main__':
    cabecalho('Dicionários de aniversários')
    aniversario()
