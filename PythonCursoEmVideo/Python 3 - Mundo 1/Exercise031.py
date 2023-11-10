# Desenvolva um programa que pergunte a distância de uma viagem em KM. 
# Calcule o preço da passagem, cobrando R$0,50 por KM para viagens de até 200KM e R$0,45 para viagens mais longas.

distKM = float(input('Informe a distância da viagem em KM:'))

if distKM <= 200:
    print('O preço da sua passagem ficou: R${:.2f}'.format(distKM*0.50))
else:
    print('O valor da sua passagem baseado no {:.0f} KM é de R${:.2f}' .format(distKM, distKM*0.45))

# preco = distKM*0.50 if distKM <= 200 else preco = distKM*0.45
