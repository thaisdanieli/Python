# DESAFIO 069 - Análise de dados do grupo
#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos. 
fim = 'FIM DO PROGRAMA'
inicio = 'CADASTRE UMA PESSOA'

mens = womans = tot =  0

while True:
    print('-'*20)
    print(f'{inicio:^20}')
    print('-'*20)

    idade   = int(input('Idade: '))
    sex     = str(input('Sexo: [M/F]: ')).strip().upper()[0]

    if sex != "M" and sex != "F":
        while True:
            sex     = str(input('Sexo: [M/F]: ')).strip().upper()[0]
            if sex == "M" or sex == "F":
                break

    if sex == "F" and idade < 20:
        womans += 1
    if sex == "M":
        mens += 1
    if idade > 18:
        tot += 1    

    exect = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if exect != "S" and exect != "N":
        while True:
            exect = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
            if exect == "S" or exect == "N":
                break
    if exect == "N":
        break

print(f'{fim:=^30}')
print(f'Total de pessoas com mais de 18 anos: {tot}')
print(f'Ao todo temos {mens} homens cadastrados')
print(f'E temos {womans} mulheres com menos de 20 anos')