"""exercicio008.py em 2018-09-30. Projeto Practice Python.

Faça um jogo Pedra-Papel-Tesoura para dois jogadores.
(Dica: Peça para os jogadores jogarem (usando entrada), compare-os, imprima uma mensagem de felicitações ao vencedor e
pergunte se os jogadores querem começar um novo jogo)

Lembre-se das regras:

Pedra bate tesoura
Tesoura bate papel
Papel bate pedra

"""
from random import randint
from cicero import cabecalho


def jogar(dicionario: dict, resposta: str = 's') -> object:
    """Jogo Papel-Pedra-Tesoura

    :param dicionario: opções em um dicionário
    :type dicionario: dict
    :param resposta: retorno usuário
    :type resposta: str
    :rtype: object
    """
    while True:
        if resposta in 'n':
            return print('\nFoi bom jogar com você!')
        elif resposta in 's':
            # mostra as opções para o usuário
            for k, v in dicionario.items():
                print(f'{k}. {v}')
            computador = randint(1, 3)
            usuario = int(input('Escolha um número: '))
            if (dicionario[usuario] == 'Pedra' and dicionario[computador] == 'Tesoura') \
                    or (dicionario[usuario] == 'Tesoura' and dicionario[computador] == 'Papel') \
                    or (dicionario[usuario] == 'Papel' and dicionario[computador] == 'Pedra'):
                print('Parabéns! Você venceu.')
            elif dicionario[usuario] == dicionario[computador]:
                print('Houve um empate.')
            else:
                print('Você perdeu!')
            print(f'Você = {dicionario[usuario]}\nComputador = {dicionario[computador]}\n')
        else:
            print('Digite S ou N. Tente novamente!')
        resposta = str(input('Quer jogar novamente? [S/N] ')).strip().lower()[0]


if __name__ == '__main__':
    cabecalho('Pedra-Papel-Tesoura')
    opcoes = {1: 'Pedra', 2: 'Papel', 3: 'Tesoura'}
    jogar(opcoes)
