# DESAFIO 063 - Sequência de Fibonacci v1.0
# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.


number = c= int(input('oi: '))

a = 0
aux = b = cd = 0

while c > 0:
    print(aux, end = ' -> ')
    b = a 
    a = aux 
    if c == number:
        aux = 1   
    cd = a + b 
    if c != number:
        aux = cd

    c -= 1
print('FIM')

