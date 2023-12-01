# DESAFIO 074 - Maior e menor valores em Tupla
# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

import random

numeros = tuple(random.randint(0,9) for _ in range(0,5))

print('Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n}', end ='')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')