""" Faça um programa que leia nome e média de um aluno,
guardando também a situação em um dicionário.

No final, mostre o conteúdo da estrutura na tela."""


dic = dict()
dic['name'] = str(input('Informe o nome do aluno: '))
dic['media'] = float(input(f'Informe a média do aluno {dic['name']}: '))

if dic['media'] >= 7:
    dic['result'] = 'APROVADO'
else:
    dic['result'] = 'REPROVADO'

print(f'A situação do aluno {dic['name']} é {dic['result']}')