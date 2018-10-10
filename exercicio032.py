"""exercicio032.py em 2018-10-08. Projeto Practice Python.

Neste exercício, terminaremos de construir o Hangman. No jogo do Hangman, o jogador tem apenas 6 palpites incorretos
(cabeça, corpo, 2 pernas e 2 braços) antes de perder o jogo.

Na Parte 1, nós carregamos uma lista de palavras aleatórias e escolhemos uma palavra dela.
Na Parte 2, escrevemos a lógica para adivinhar a carta e exibir essa informação para o usuário.
Neste exercício, temos que juntar tudo e adicionar lógica para lidar com os palpites.

Copie seu código das partes 1 e 2 para um novo arquivo como ponto de partida. Agora adicione os seguintes recursos:

Apenas deixe o usuário adivinhar 6 vezes e diga ao usuário quantos palpites ainda restam.
Acompanhe as letras que o usuário adivinhou. Se o usuário adivinhar uma carta que eles já adivinharam, não os penalize.
Deixe-os adivinhar novamente.
Adições opcionais:

Quando o jogador ganha ou perde, deixe-o começar um novo jogo.
Em vez de dizer ao usuário "Você tem 4 palpites incorretos restantes", exiba algumas imagens para o Hangman.
Isso é um desafio - faça as outras partes do exercício primeiro!

"""
from random import choice
from cicero import cabecalho, cores


def monta_hangman(desenho: list, lista: list, conta: int):
    """Monta o boneco e as letras acertadas

    :param desenho: lista com partes do boneco
    :type desenho: list
    :param lista: lista com as letras já acertadas
    :type lista: list
    :param conta: numero de erros
    :type conta: int
    """
    for k, v in enumerate(desenho):
        print()
        for x, y in enumerate(desenho[k]):
            print(f'{desenho[k][x]}', end='')
    print(f'\t\t{conta} erro(s).')

    for z in lista:
        print(z, end=' ')


def sorteio(nome: str) -> object:
    """Busca uma palavra aleatória em um arquivo

    :param nome: arquivo
    :type nome: str
    :return: palavra aleatória
    :rtype: object
    """
    with open(nome, 'r') as f:
        palavras = list(f)
    return choice(palavras).strip()


def hangman():
    cabecalho('Bem-vindo ao Hangman!', 30, '-')
    palavra = str(sorteio('txt/sowpods.txt'))
    total_letras = len(palavra)
    letras = ['_' for y in range(total_letras)]
    boneco = [[' ', 'O', ' '], ['/', '|', '\\'], ['/', ' ', '\\']]
    acertos = erros = 0
    monta_hangman(boneco, letras, erros)
    while True:
        print()
        print(palavra)
        letra = str(input('\nAdivinhe uma letra: ')).strip().upper()
        if letra in palavra:
            if letra not in letras:
                # coloca as letras corretas na lista letras
                for k, v in enumerate(palavra):
                    if v == letra:
                        letras[k] = v
                        acertos += 1
                monta_hangman(boneco, letras, erros)
            else:
                monta_hangman(boneco, letras, erros)
                print(f'{cores("azul")}Você já usou esta letra. Tente outra!{cores("limpa")}')
        else:
            erros += 1
            # indice da lista dentro da lista
            cont = 0
            # retira partes do boneco
            while True:
                if boneco[0][cont] != ' ':
                    # apaga parte do boneco
                    boneco[0][cont] = ' '
                    if len(set(boneco[0])) == 1:
                        # apaga a lista de índice '0' dentro da lista
                        del boneco[0]
                    break
                cont += 1
            monta_hangman(boneco, letras, erros)
            print(f'\t{cores("vermelho")}Incorreto!{cores("limpa")}')
            if erros == 6:
                print()
                pergunta = str(input('Quer jogar de novo? [S/ outra tecla para sair] ')).strip().lower()[0]
                if pergunta == 's':
                    # limpa dados para recomeçar
                    palavra = str(sorteio('txt/sowpods.txt'))
                    total_letras = len(palavra)
                    letras = ['_' for y in range(total_letras)]
                    boneco = [[' ', 'O', ' '], ['/', '|', '\\'], ['/', ' ', '\\']]
                    acertos = erros = 0
                    monta_hangman(boneco, letras, erros)
                    continue
                else:
                    cabecalho('Fim', 30, '-')
                    break
        if acertos == total_letras:
            print(f'{cores("verde")}Parabéns!{cores("limpa")}')
            cabecalho('Fim', 30, '-')
            break


if __name__ == '__main__':
    cabecalho('Hangman')
    hangman()
