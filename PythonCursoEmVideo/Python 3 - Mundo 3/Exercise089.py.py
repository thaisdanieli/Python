"""
Crie um programa que leia nome e duas notas de vários alunos
e guarde tudo em uma lista composta.

No final, mostre um boletim contendo a média de cada um
e permita que o usuário possa mostrar as notas de cada aluno individualmente

Cria um programa que lê nome e duas notas de vários alunos
e guarda-os numa lista completa.
"""
import time

listaNota = []
listaMedia = []
dados = []

cod = 'CÓD.'
name = 'NOME'
nota = 'NOTA'

h = 0

while True:
    dados.append(str(input('Informe o nome do aluno: ')))
    dados.append(float(input('Informe a primeira nota: ')))
    dados.append(float(input('Informe a segunda nota: ')))
    listaNota.append(dados[:])
    dados.clear()

    yesNo = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if yesNo == "N":
        break
    else:
        print()

print('-='*16)
print(f'{cod} {name:^10} {nota:^20}')
print('-'*32)
for r in range(0,len(listaNota)):
    if r == h:
        print(r, end = '')
        print(f'{listaNota[r][0]:^20}', end ='')
        aux = (listaNota[r][1]+listaNota[r][2])/2
        print(f'{aux:^9}')
        h += 1
print('-='*16)

while True:
    num = int(input('Mostrar notas de qual aluno (999 interrompe): '))
    if num == 999:
        print('FINALIZANNDO...')
        time.sleep(0.5)
        print('VOLTE SEMPRE!!!')
        break
    else:
        print(f'Notas de {listaNota[num][0]} são', end=' ')
        print(f'[{listaNota[num][1]}, {listaNota[num][2]}]')

