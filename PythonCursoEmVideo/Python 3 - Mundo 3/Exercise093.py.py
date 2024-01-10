"""
 Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador
 e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso
 será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

"""

from time import sleep

dict_ = dict()
list_ = list()
tot = 0

dict_['Nome do Jogador'] = str(input('Nome do Jogador: '))
quant = int(input(f'Quantas partidas {dict_['Nome do Jogador']} jogou? '))

for c in range(0,quant):
    number = int(input(f'Quantos gols na partida {c+1}? '))
    list_.append(number)
    tot += list_[c]
    
dict_['Gols'] = list_
dict_['Total'] = tot

print('-=' * 30)
print(dict_)
print('-=' * 30)

for k, v in dict_.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)

print(f'O Jogador {dict_['Nome do Jogador']} jogou {quant} partidas.')
for c in range(0,quant):
    print(f' => Na partida {c+1}, fez {list_[c]} gols.')

print(f'Foi um total de {tot} gols.')