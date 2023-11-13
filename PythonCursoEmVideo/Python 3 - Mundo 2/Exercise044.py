# Elabora um programa que calcule o valor a ser pago por um produto. considerando o seu preço normal e condição de pagamento:
# - À vista dinheiro/ cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - em até 2x no cartão: preço Normal
# - 3x ou mais no cartão: 20% de juros


preco = float(input('Preço das compras: R$'))

print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
opcao = int(input('Qual é a opção? '))

if opcao == 1:
    value = preco - (preco *10/ 100)
    print('Sua compra de R${:.2f} vai custar R${:.2F} no final.' .format(preco, value))
elif opcao == 2:
    value = preco - (preco * 5 /100)
    print('Sua compra de R${:.2f} vai custar R${:.2F} no final.' .format(preco, value))
elif opcao == 3:
    value = preco / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS' .format(value))
    print('Sua compra de R${:.2f} vai custar R${:.2F} no final.' .format(preco, value))
elif opcao == 4:
    parcelas  = int(input('Quantas parcelas? '))
    precJuros = preco + (preco * 20 / 100)
    value     =  precJuros / parcelas
    print('Sua compra será parcelada em {}x de R${:.2F} COM JUROS' .format(parcelas, value))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.' .format(preco, precJuros))
else:
    preco = 0
    print('Opção inválida de pagamento. Tente novamente!')