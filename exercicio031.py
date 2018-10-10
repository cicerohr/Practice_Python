"""exercicio031.py em 2018-10-07. Projeto Practice Python.

Vamos continuar construindo o Hangman.
No jogo do carrasco, uma palavra de pista é dada pelo programa que o jogador tem que adivinhar, letra por letra.
O jogador adivinha uma letra de cada vez até que toda a palavra tenha sido adivinhada.
(No jogo atual, o jogador só pode adivinhar 6 letras incorretamente antes de perder).

Digamos que a palavra que o jogador tenha que adivinhar é "EVAPORATE".
Para este exercício, escreva a lógica que pede a um jogador que adivinhe uma letra e exiba letras na palavra de pista
que foram adivinhadas corretamente. Por enquanto, deixe o jogador adivinhar um número infinito de vezes até obter a
palavra inteira. Como bônus, acompanhe as letras que o jogador adivinhou e mostre uma mensagem diferente
se o jogador tentar adivinhar essa carta novamente.
Lembre-se de parar o jogo quando todas as letras tiverem sido adivinhadas corretamente!
Não se preocupe em escolher uma palavra aleatoriamente ou manter o controle do número de palpites
que o jogador ainda tem - lidaremos com aqueles em um exercício futuro.

Um exemplo de interação pode ser assim:

Bem-vindo ao Hangman!
_ _ _ _ _ _ _ _ _
Adivinha sua carta: S
Incorreta!
Adivinha sua carta: E
E _ _ _ _ _ _ _ E
...
E assim por diante, até que o jogador receba a palavra.

"""
from cicero import cabecalho, cores


def monta_hangman(lista):
    for x in lista:
        print(x, end=' ')


def hangman(palavra):
    cabecalho('Bem-vindo ao Hangman!', 30, '-')
    total_letras = len(palavra)
    letras = ['_' for y in range(total_letras)]
    conta = 0
    monta_hangman(letras)
    while True:
        print()
        letra = str(input('\nAdivinhe uma letra: ')).strip().upper()
        if letra in palavra:
            if letra not in letras:
                for k, v in enumerate(palavra):
                    if v == letra:
                        letras[k] = v
                        conta += 1

                monta_hangman(letras)
            else:
                monta_hangman(letras)
                print(f'{cores("azul")}Você já usou esta letra. Tente outra!{cores("limpa")}')
        else:
            monta_hangman(letras)
            print(f'{cores("vermelho")}Incorreto! Tente novamente!{cores("limpa")}')
        if conta == total_letras:
            print(f'{cores("verde")}Parabéns!{cores("limpa")}')
            cabecalho('Fim', 30, '-')
            break


if __name__ == '__main__':
    cabecalho('Adivinha Letras')
    hangman('EVAPORATE')
