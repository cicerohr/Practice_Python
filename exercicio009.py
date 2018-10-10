"""exercicio009.py em 2018-09-30. Projeto Practice Python.

Gere um número aleatório entre 1 e 9 (incluindo 1 e 9).
Peça ao usuário para adivinhar o número e, em seguida, diga se ele adivinhou muito baixo, muito alto ou
exatamente.

Extras:

Mantenha o jogo até que o usuário digite "sair"
Acompanhe quantas adivinhações foram feitas pelo usuário e, quando o jogo terminar, imprima isso.

"""
from random import randint
from cicero import cabecalho


def mensagem(contagem: int, msg: str = 'sair') -> object:
    """Mensagem para o usuário

    :type contagem: int
    :param msg: mensagem
    :type msg: str
    :return: impressão da mensagem
    :rtype: object
    """
    if msg == 'maior':
        print('Mais baixo.')
        return contagem + 1
    elif msg == 'menor':
        print('Mais alto')
        return contagem + 1
    elif msg == 'igual':
        return str(input(f'Você acertou! Você fez {contagem} tentativa(s).\nQuer jogar de novo? [S/N]')).lower()[0]
    else:
        return print(f'Você fez {contagem} tentativa(s). Foi bom jogar com você!')


def adivinhar() -> object:
    """Jogo para adivinhar de 1 a 9

    :rtype: object
    """
    conta = 0
    computador = str(randint(1, 9))
    while True:
        usuario = str(input('Digite um número de 1 a 9 ou [sair]: ')).strip().lower()
        if usuario == 'sair':
            return mensagem(conta)
        else:
            if usuario == computador:
                conta += 1
                usuario = mensagem(conta, 'igual')
                if usuario == 'n':
                    return print('\nFoi bom jogar com você!')
                else:
                    conta = 0
                    computador = str(randint(1, 9))
                    continue
            if usuario > computador:
                conta = mensagem(conta, 'maior')
            if usuario < computador:
                conta = mensagem(conta, 'menor')


if __name__ == '__main__':
    cabecalho('Jogo de adivinhação 1')
    adivinhar()
