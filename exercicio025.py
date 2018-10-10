"""exercicio025.py em 2018-10-04. Projeto Practice Python.

Você, o usuário, terá em sua cabeça um número entre 0 e 100.
O programa adivinhará um número e você, o usuário, dirá se ele está muito alto, muito baixo ou o seu número.
No final deste intercâmbio, o seu programa deve imprimir quantos palpites foram necessários para obter o seu número.

Como o escritor deste programa, você terá que escolher como seu programa irá adivinhar estrategicamente.
Uma estratégia ingênua pode ser simplesmente começar a adivinhação em 1 e continuar (2, 3, 4, etc.) até atingir
o número. Mas essa não é uma estratégia de adivinhação ideal.
Uma estratégia alternativa pode ser adivinhar 50 (bem no meio do intervalo) e, em seguida, aumentar / diminuir em 1,
conforme necessário. Depois de escrever o programa, tente encontrar a estratégia ideal!

"""
from cicero import cabecalho


def adivinhar(palpites: int = 0) -> object:
    """Encontra um número dividindo uma lista pela metade (https://pt.wikipedia.org/wiki/Pesquisa_binária#Código_em_C)

    :param palpites: quantidade de tentativas para encontrar o número
    :type palpites: int
    :return: imprime a quantidade de tentativa
    :rtype: object
    """
    usuario = ' '
    numeros = list(range(0, 101))

    while not (len(numeros) == 1 or usuario == '='):
        usuario = ' '
        metade = len(numeros) // 2
        # palpite é o índice da medade da lista
        palpite = numeros[metade]
        while usuario not in '<>=':
            usuario = str(input(f'O numero é maior(>), menor(<) ou igual(=) a {palpite}? ')).strip()[0]
        if usuario == '>':
            # a lista passa a ter a metade maior dos valores
            numeros = numeros[(metade + 1):]
            palpites += 1
        elif usuario == '<':
            # a lista passa a ter a metade menor dos valores
            numeros = numeros[:metade]
            palpites += 1
    return print(f'Total de palpites: {palpites}')


if __name__ == '__main__':
    cabecalho('Jogo de adivinhação 2')
    adivinhar()
