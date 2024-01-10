"""

 Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização
 de detalhes do aproveitamento de cada jogador.

"""
"""
 Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador
 e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso
 será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

"""

list_ = list()
dict_ = dict()
listAux = list()
tot = 0

Cod = 'COD'
Nome = 'NOME'
Gols = 'GOLS'
Total = 'TOTAL'


while True:
    dict_['Nome'] = input('Nome do Jogador? ')
    jogadas = int(input(f'Quantas partidas {dict_['Nome']} jogou? '))

    for c in range(0,jogadas):
        listAux.append(int(input(f'Quantos gols na partida {c+1}? ')))
        tot += listAux[c]

    dict_['Gols'] = listAux[:]
    dict_['Total'] = tot
    list_.append(dict_.copy())
    listAux.clear()
    dict_.clear()
    

    yesNo = input('Deseja continuar? [S/N]').strip().upper()[0]
    if yesNo in 'Nn':
        break

print('-=' * 30)

Nome = 'NOME'
print(f'{Cod} {Nome:^10} {Gols:^15} {Total:^20}')

h = 0

for c in list_:
    for k, v in c.items():
        if k == 'Nome':
            print(h, end='')
            h += 1
            print(f'{v:^17}', end='')
        elif k == 'Gols':
            print(f'{c['Gols']}', end='')
        elif k == 'Total':
            print(f'{v:^30}', end='')
    print()

print('-'*40)

while True:
    number = int(input('Mostrar dados de qual jogador? (999 para parar) '))

    if number == 999:
        break

    if not list_[number]:
        print(f'ERRO! Não existe jogador com o código {number}!')
        number = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    else:

        print(f' - LEVANTAMENTO DO JOGADOR {list_[number]['Nome']}: ')

        for c in range(0, len(list_[number]['Gols'])):
            print(f'    No jogo {c+1} fez {list_[number]['Gols'][c]} gols.')

    print('-'*40)