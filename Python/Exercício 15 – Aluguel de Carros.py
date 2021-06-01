
#Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Qual foi a distancia percorrida: Km '))
dias = int(input('Com quantos dias ficou com o carro: '))
pdia = dias * 60
pkm = km * 0.15
ptotal = pdia + pkm
print('O preço foi de R$ {:.2f}'.format(ptotal))