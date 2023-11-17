# DESAFIO 057 - Validação de Dados
# faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.


sex = str(input('Informe seu sexo: [M/F]: ')).strip().upper()[0]

while sex != "M" and sex != "F":
    sex = str(input('Dados inváidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso' .format(sex))