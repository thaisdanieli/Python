'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.

O programa vai perguntar quantos jogos serão gerados
e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta.
'''

from random import randint

lista = []

number = int(input('Quantos jogos? '))

for i in range(0,number):
    num = randint(1,60)

    if len(lista) == 0:
        lista.append(num)
    else:
        for j in range(0,len(lista)):
            if lista[j] == num:
                num = randint(1,60)
            j+=1
        lista.append(num)
    
print(lista)