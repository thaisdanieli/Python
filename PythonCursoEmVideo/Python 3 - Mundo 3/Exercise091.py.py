"""
 Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
 Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que
 o vencedor tirou o maior número no dado.

"""

from random import randint
from time import sleep
from operator import itemgetter

dit = dict()

dit['Jogador_1'] = randint(1,6)
dit['Jogador_2'] = randint(1,6)
dit['Jogador_3'] = randint(1,6)
dit['Jogador_4'] = randint(1,6)

ranking = list()

print('Valores Sorteados: ')

for k, v in dit.items():
    print(f'O {k} tirou {v} no dado')
    sleep(1)

ranking = sorted(dit.items(), key=itemgetter(1), reverse=True) # Se for itemgetter (0) ele ordenará por ordem de chaves, itemgetter (1) ele ordenará por ordem de valor
print('-=' * 30)
print('   == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'    {i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)