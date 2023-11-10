# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo
# Regra matemática: Cada um desses segmentos tem que ser menor que a soma dos outros dois.

print('-='*20)
print('ATIVIDADE 035')
print('-='*20)

valor1 = float(input('Primeiro segmento: '))
valor2 = float(input('Segundo segmento: '))
valor3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + e3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')