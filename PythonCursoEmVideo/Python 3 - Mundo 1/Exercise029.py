# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80KM/H, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada KM acima do limite.

velocidade = int(input('Informe a velocidade do carro:'))

if velocidade > 80:
    print('Você ultrapassou a velocidade permitida!')
    print('Você será multado!')
    print(f'A multa é no valor de R${(velocidade-80)*7},00')
else:
    print('Tenha um bom dia! Dirija com segurança! :)')