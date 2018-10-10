"""exercicio018.py em 2018-10-01. Projeto Practice Python.

Crie um programa que jogue o jogo "vacas e touros" com o usuário. O jogo funciona assim:

Gerar aleatoriamente um número de 4 dígitos. Peça ao usuário para adivinhar um número de 4 dígitos.
Para cada dígito que o usuário adivinhou corretamente no lugar correto, eles têm uma "vaca".
Para cada dígito que o usuário adivinhou corretamente no lugar errado é um "touro".
Toda vez que o usuário faz uma suposição, diga-lhes quantas "vacas" e "touros" eles têm.
Quando o usuário adivinha o número correto, o jogo acabou.
Acompanhe o número de palpites que o usuário faz ao longo do jogo e informe ao usuário no final.

Digamos que o número gerado pelo computador seja 1038. Um exemplo de interação poderia ser assim:

  Bem-vindo ao jogo das vacas e dos touros!
  Digite um número:
  >>> 1234
  2 vacas, 0 touros
  >>> 1256
  1 vaca, 1 touro
  ...
Até que o usuário adivinhe o número.

"""
from random import randint
from cicero import cabecalho


def comparador(lista1: list, lista2: list) -> str:
    """Compara números entre listas

    :param lista1: numeros do usuário
    :type lista1: list
    :param lista2: numeros gerados
    :type lista2: list
    :return: quantos números encontrados
    :rtype: str
    """
    vaca = touro = 0
    for x in range(len(gerador)):
        if lista1[x] == lista2[x]:
            vaca += 1
        elif lista1[x] in lista2[:]:
            touro += 1
    return f'{vaca} vaca(s); {touro} touro(s)'


if __name__ == '__main__':
    cabecalho('Bem-vindo ao jogo das vacas e dos touros!')
    gerador = list(str(randint(1000, 9999)))
    conta = 0
    print(gerador)
    while True:
        numero = list(str((input('Digite um número de 4 digitos: '))))
        conta += 1
        if numero == gerador:
            print(f'Parabéns! Você acertou o número {gerador} em {conta} tentativa(s).')
            break
        else:
            print(comparador(numero, gerador))
