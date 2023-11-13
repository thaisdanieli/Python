# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa
# o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

home    = float(input('Informe o valor da residência: R$'))
salario = float(input('Informe o salário do comprador: R$'))
meses   = int(input('Informe a quantidade de meses que deseja pagar:'))

meses               = meses * 12
prestacao           = home/meses
verificacaoSalario  = salario*30/100

if prestacao > verificacaoSalario:
    print('Infelizmente não será possível a compra da casa. Prestação ultrapassou os 30% do salário informado.')
else:
    print('Parabéns! Seu empréstimo foi APROVADO!')
    print('Serão {} meses sendo cada parcela no valor de R${:.2f}' .format(meses, prestacao))