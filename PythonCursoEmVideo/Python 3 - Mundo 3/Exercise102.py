def fatorial(a, show=False):
    """
    -> Calcula o fatorial do número digitado.
    :param n: O número a ser calculado.
    :param show: (opcional) mostrar ou não a conta.
    :return: Retorna o valor de n.
    """

    f = 1
    for c in range(a, 0, -1):
        if show:
            print(f'{c}', end=' ')
            if c != 1:
                print('x', end=' ')
            else: 
                print('=', end = ' ')
        f *= c
    print(f'{f}', end='\n')
    


# PROGRAMA PRINCIPAL

print(fatorial(5,True))
help(fatorial)