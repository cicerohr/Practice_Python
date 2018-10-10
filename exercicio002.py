"""exercicio002.py em 2018-09-29. Projeto Practice Python.

entrada se tipos int números de comparação de igualdade mod

Peça ao usuário um número.
Dependendo se o número é par ou ímpar, imprima uma mensagem apropriada para o usuário.
Dica: como um número par / ímpar reage diferentemente quando dividido por 2?

Extras:

Se o número for um múltiplo de 4, imprima uma mensagem diferente.
Peça ao usuário dois números: um número para marcar (chame de num) e um número para dividir por (check).
Se a verificação se for divisível por num, informe isso ao usuário. Caso contrário,
imprima uma mensagem apropriada diferente.

"""
from cicero import cabecalho


def par_impar(numero: int, divisor: int) -> object:
    """Verifica se o número é par ou ímpar; se par verifica se é múltiplo de 4.
    Verifica se o numero é divisível pelo divisor sem resto

    :param numero: estrada do usuário
    :type numero: int
    :param divisor: entrada do usuário
    :type divisor: int
    :return: par ou impar; se é múltiplo de 4 e se o número é divisível pelo divisor sem resto
    :rtype: object
    """
    if numero % 2 == 0:
        if numero % 4 == 0:
            msg = f'O número {numero} é par e multiplo de 4.'
        else:
            msg = f'O número {numero} é par.'
    else:
        msg = f'O número {numero} é impar.'

    if numero % divisor == 0:
        return print(f'{msg}\nOs números {num} e {check} são múltiplos entre si.')
    else:
        return print(f'{msg}\nOs números {num} e {check} NÃO são múltiplos entre si.')


if __name__ == '__main__':
    cabecalho('Par ou ímpar')
    num = int(input('Digite um número: '))
    check = int(input('Digite um número para ser divisor: '))
    par_impar(num, check)
