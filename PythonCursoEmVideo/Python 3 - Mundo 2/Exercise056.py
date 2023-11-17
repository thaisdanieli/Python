# DESAFIO 056 - Analisador completo
# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: 
# - A média da idade do grupo.
# - Qual é o nome do homem mais velho. 
# - Quantas mulheres tem menos de 20 anos.

numbMulh = 0
medGruoup = 0
ageMan = 0
AgeName = ''

for c in range(1,5):
    print('{}ª PESSOA' .format(c))
    name = str(input('Nome: ')).strip().upper()
    age  = int(input('Idade: '))
    sex  = str(input('SEXO [M/F]:')).strip().upper()

    medGruoup += age

    if sex == "F" and age < 20:
        numbMulh += 1

    if sex == "M":
        if age > ageMan:
            ageMan = age
            AgeName = name


medGruoup = medGruoup/4

print('A média de idade do grupo é de {:.1f} anos' .format(medGruoup))
print('O homem mais velho tem {} anos e se chama {}' .format(ageMan, AgeName))

if numbMulh == 1:
    print('Apenas 1 mulher com menos de 20 anos')
else:
    print('Ao todo são {} mulheres com menos de 20 anos' .format(numbMulh))






