# Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. 
#Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random

print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
number = random.randint(1,10)
corret = False
cont = 0
while not corret:
    cont += 1
    n = int(input('Qual é seu palpite? '))  
    if n == number:
        corret = True
    else:
        if n < number:
            print('Mais... Tente mais uma vez.')
        elif n > number:
            print('Menos... Tente mais uma vez.')

print('Acertou com {} tentativas. Parabéns!' .format(cont))