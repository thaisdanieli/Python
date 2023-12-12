# DESAFIO 084 - Lista composta e análise de dados
# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.


lista = []
dados = []
totPeople = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))

    if len(lista) == 0:
        maiorPeso = menorPeso = dados[1]
    else:
        if dados[1] > maiorPeso:
            maiorPeso = dados[1]
        if dados[1] < menorPeso:
            menorPeso = dados[1]

    lista.append(dados[:])              # Criou uma copia da lista dados
    dados.clear()
    
    yesNo = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if yesNo == 'N':
        break

print(f'Ao todo, você cadastro {len(lista)} pessoas.')
print(f'O maior peso foi de {maiorPeso}KG. Peso de', end = ' ')
for p in lista:
    if p[1] == maiorPeso:
        print(f'[{p[0]}]', end = ' ')
print(f'\nO menor peso foi de {menorPeso}KG. Peso de', end = ' ')
for p in lista:
    if p[1] == menorPeso:
        print(f'[{p[0]}]', end = ' ')



















