"""cicero.py em 2018-10-04. Projeto Practice Python.

Funções para uso geral

"""


def so_numero(mensagem: str) -> int:
    """ Verifica se a entrada é um valor inteiro

    :param mensagem: string com uma mensagem
    :type mensagem: str
    :return: valor inteiro ou mensagem de erro
    :rtype: int
    """
    while True:
        try:
            entrada_usuario = int(input(mensagem))
        except ValueError:
            print('Digite um número inteiro. Tente novamente!')
            continue
        else:
            return entrada_usuario


def cabecalho(titulo: str, caracteres: int = 50, tipo: str = '='):
    """Imprime um cabeçalho

    :param titulo: título
    :type titulo: str
    :param caracteres: número de caracteres do título
    :type caracteres: int
    :param tipo: tipo de caracter de prenchimento
    :type tipo: str
    """
    print()
    print(f' {titulo} '.title().center(caracteres, tipo))
    print()


def cores(cor: str) -> str:
    """dicionário com códigos de escape sequence ANSI para configurar cores

    :param cor: nome da cor
    :type cor: str
    :return: cor do dicionário
    :rtype: str
    """
    dicionario = {'limpa': '\033[m',
                  'vermelho': '\033[1;31m',
                  'verde': '\033[1;32m',
                  'amarelo': '\033[1;33m',
                  'azul': '\033[1;34m',
                  'sublinhado': '\033[4m',
                  'bold': '\033[1;30m',
                  'pretoBranco': '\033[7;30m'}
    return dicionario[cor]


# -------------------- programa de teste --------------------

def _gerador_teste(n, funcao, args):
    from time import time
    print(n, 'vezes', funcao.__name__)
    t0 = time()
    for i in range(n):
        funcao(*args)
    t1 = time()
    print(round(t1 - t0, 3), 'segundos,')


def _teste(n=2000):
    _gerador_teste(n, so_numero, 'Digite um número: ')


if __name__ == '__main__':
    print(f'{cores("sublinhado")}teste{cores("limpa")}')
    print(f'{cores("azul")}teste{cores("limpa")}')
    print(f'{cores("pretoBranco")}teste{cores("limpa")}')
    print(__doc__)
    print()
    print(so_numero.__name__)
    print(so_numero.__doc__)
    print(f'Defaults: {so_numero.__defaults__}')
    print()
    print(cabecalho.__name__)
    print(cabecalho.__doc__)
    print(f'Defaults: {cabecalho.__defaults__}')
    print()
    print(cores.__name__)
    print(cores.__doc__)
    print(f'Defaults: {cores.__defaults__}')
    # _teste()
