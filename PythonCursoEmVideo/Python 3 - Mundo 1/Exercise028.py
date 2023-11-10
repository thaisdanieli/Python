# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 
# Peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

number = random.randint(0,5)
num = int(input('Informe um número de 0 a 5:'))
if num == number:
    print('PARABÉNS! VOCÊ ACERTOU!')
else:
    print('Não foi dessa vez, mas não desista!')

