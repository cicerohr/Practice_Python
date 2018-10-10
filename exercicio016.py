"""exercicio016.py em 2018-10-01. Projeto Practice Python.

Escreva um gerador de senha no Python.
Seja criativo com a maneira como você gera senhas - as senhas fortes têm uma combinação
de letras minúsculas, letras maiúsculas, números e símbolos.
As senhas devem ser aleatórias, gerando uma nova senha toda vez que o usuário solicitar uma nova senha.
Inclua seu código de tempo de execução em um método principal.

Extra:

Pergunte ao usuário o quão forte eles querem que sua senha seja.

"""
from random import sample
from string import digits, ascii_letters, punctuation
from cicero import cabecalho


def senha1(tamanho: int = 8) -> str:
    """Gera senhas aleatórias

    :param tamanho: quantidades de caracteres para a senha
    :type tamanho: int
    :return: senha
    :rtype: str
    """
    simbolos = '!"#$%&()*+,-./:;<=>?@[\]^_`{|}~'
    letras = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digitos = '0123456789'
    return ''.join(sample(simbolos + letras + digitos, tamanho))


def senha2(tamanho: int = 8, caracteres: str = ascii_letters + digits + punctuation) -> str:
    """Gera senhas aleatórias

    :param tamanho: quantidades de caracteres para a senha
    :type tamanho: int
    :param caracteres: caracteres para gerar a senha
    :type caracteres: str
    :return: senha
    :rtype: str
    """
    return ''.join(sample(caracteres, tamanho))


if __name__ == '__main__':
    cabecalho('Gerador de senhas')
    print(senha1())
    print(senha1(14))
    print(senha1(int(input('Quantos caracteres terá a sua senha? '))))
    print('-' * 40)
    print(senha2())
    print(senha2(14, '<- Cícero_Henrique_Rodrigues 1234567890 ->'))
    print(senha2(int(input('Quantos caracteres terá a sua senha? '))))
    cabecalho('Teste')
