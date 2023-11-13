# Escrava um programa que leia dois números inteiros e compare-OS, mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois SÃO iguais

number1 = int(input('Informe o primeiro número:'))
number2 = int(input('Informe o segundo número:'))

if number1 > number2:
    print('O número {} é maior que o número {}'.format(number1, number2))
elif number2 > number1:
    print('O número {} é maior que o número {}'.format(number2, number1))
else:
    print('Não existe valor maior, os dois SÃO iguais!')
