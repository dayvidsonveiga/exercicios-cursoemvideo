
#Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

vel = float(input('Qual a velocidade do carro? '))
if vel > 80:
  print('Voce ultrapassou a velocidade permitida de 80Km/h! Voce foi multado no valor de R$ {:.2f}!'.format((vel - 80) * 7))
print('Tenha um bom dia! Dirija com segurança!')