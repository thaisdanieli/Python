"""
 Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
 e todos os dicionários em uma lista. No final, mostre:

 A) Quantas pessoas foram cadastradas;
 B) A média de idade;
 C) Uma lista com as mulheres;
 D) Uma lista de pessoas com idade acima da média.

"""

list_ = list()
listAux = list()
dict_ = dict()
media = 0

while True:
    dict_['Nome'] = input('Nome: ')
    dict_['Sexo'] = input('Sexo: [F/M] ').upper()[0]
    dict_['Idade'] = int(input('Idade: '))

    media += dict_['Idade']

    if dict_['Sexo'] == "F":
        listAux.append(dict_['Nome'])
    
    list_.append(dict_.copy())
    dict_.clear()

    yesNo = input('Deseja coninuar? [S/N] ').strip().upper()[0]
    if yesNo == "N":
        break

for c in range(0,len(listAux)):
	print(listAux[c], end=' ')
print()

media = media/ len(list_)

for c in range(0, len(list_)):
	if list_[c]['Idade'] > media:
		print(list_[c])
