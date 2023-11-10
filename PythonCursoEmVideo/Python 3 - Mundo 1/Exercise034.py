# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
# Para salários superiores a R$1.250,00 calcule um aumento de 10%
# Para os inferiores ou iguais, o aumento é de 15%

salario = float(input('Informe seu salário atual: R$'))
print(F'Salário antigo R${salario}')

if salario > 1250:
    salario = ((10/100) * salario) + salario
else: 
    salario = ((15/100) * salario) + salario

print('Seu salário atualizado é de R${:.2f}' .format(salario))