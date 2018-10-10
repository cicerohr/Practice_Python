"""exercicio015.py em 2018-09-30. Projeto Practice Python.

Escreva um programa (usando funções!) Que pede ao usuário uma longa seqüência contendo várias palavras.
Imprima de volta para o usuário a mesma string, exceto com as palavras em ordem inversa. Por exemplo,
digamos que eu digite a string:

  Meu nome é Michele
Então eu veria a string:
  Michele é nome Meu

"""
from cicero import cabecalho


def inverte(frase: str) -> object:
    """Inverte a frase

    :param frase: entrada usuário
    :type frase: str
    :return: frase invertida
    :rtype: object
    """
    # return ' '.join(frase.split()[::-1]) # alternativa
    return ' '.join(reversed(frase.split()))


if __name__ == '__main__':
    cabecalho('Ordem inversa da frase')
    print(inverte(str(input('Digite uma frase: '))))
