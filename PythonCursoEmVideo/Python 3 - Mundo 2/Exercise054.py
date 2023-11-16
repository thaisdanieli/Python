# Crie um programa que leia o ano da nascimento de sete pessoas. No final, mostra quantas pessoas ainda não atingiram a maioridade < quantas já sÃO maiores.

from datetime import datetime

maior = 0
menor = 0

for c in range(0, 7):
    year = int(input('Em que ano a {} ª pessoa nasceu?' .format(c)))
    idade = datetime.now().year - year
    if idade >= 21:
        maior += 1
    else:
        menor += 1

print('Ao todo tivemos {} pessoas maiores de idade' .format(maior))
print('E também tivemos {} pessoas menores de idade' .format(menor))


