# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabala abaixo:
# - Abaixo de 18.5: Abaixo do Peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso 
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida

altura  = float(input('Informe sua altura: '))
peso    = float(input('Informe seu peso: '))

imc = peso/(altura**2)

if imc < 18.5:
    print('Abaixo do Peso')
elif imc >=18.5 and imc <=25:
    print('Peso ideal')
#elif 30 > imc <=25:
elif imc >=25 and imc <=30:
    print('Sobrepeso')
#elif 40 > imc <= 30:
elif imc >= 30 and imc <= 40:
    print('Obesidade')
else:
    print('Obesidade mórbida!')