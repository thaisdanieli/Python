# DESAFIO 082 - Dividindo valores em várias listas
# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

listCompleted = []
listPar = []
listImpar = []

while True:
    listCompleted.append(int(input('Digite um número: ')))
    yesNo = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if yesNo == 'N':
        break


for index, value in enumerate(listCompleted):
    if value % 2 == 0:
        listPar.append(value)
    elif value % 2 == 1:
        listImpar.append(value)

print('-='*35)

print(f'A lista completa é {listCompleted}')
print(f'A lista de pares é {listPar}')
print(f'A lista de ímpares é {listImpar}')
