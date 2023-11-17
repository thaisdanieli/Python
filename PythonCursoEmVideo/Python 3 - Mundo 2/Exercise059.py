# DESAFIO 059 - Criando um Menu de Opções
# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep
value1 = int(input('Primeiro valor: '))
value2 = int(input('Segundo Valor: '))

opcao = False

while not opcao:
    print('[1] SOMAR')
    print('[2] MULTIPLICAR')
    print('[3] MAIOR')
    print('[4] NOVOS NÚMEROS')
    print('[5] SAIR DO PROGRAMA')
    op = int(input('>>>>> Qual é a sua opção? '))

    if op == 1:
        print('A soma entre {} + {} é {}' .format(value1, value2, value1+value2))
    elif op == 2:
        print('O resultado é {} x {} é {}' .format(value1, value2, value1*value2))
    elif op == 3:
        if value1 > value2:
            maior = value1
        else:
            maior = value2
        print('Entre {} e {} o maior valor é {}' .format(value1, value2, maior))
    elif op == 4:
        print('Informe os números novamente:')
        value1 = int(input('Primeiro valor: '))
        value2 = int(input('Segundo Valor: '))
    elif op == 5:
        opcao = True
        print('FINALIZANDO...')
    else:
        print('OPÇÃO INCORRETA! Por favor inseria uma opção válida.')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')