# DESAFIO 046 - Contagem regressiva
# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 até 0. com uma pausa de 1 segundo entre eles.

from time import sleep
import emoji

print(emoji.emojize('Python is :thumbs_up:'))

for t in range(10, -1, -1):
    print(t)
    sleep(1)
print('BUM! BUM! POOW!')
