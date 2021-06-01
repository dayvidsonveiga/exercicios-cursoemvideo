
#Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.


distancia = float(input('Qual é a distancia da sua viagem? '))
print('Voce esta prestes a comecar uma viagem de {}Km.')
if distancia <= 200:
  preço = distancia * 0.50
else:
  preço = distancia * 0.45
print('E o preço de sua passagem será de R${:.2f}'.format(preço))