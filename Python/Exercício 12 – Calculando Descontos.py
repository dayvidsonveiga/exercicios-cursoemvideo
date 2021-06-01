
#Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preço = float(input('Informe o valor do produto: R$ '))
desconto = preço - (preço * 5 / 100)
print('Seu produto custa R$ {:.2f} e com desconto de 5% passará a custar: R$ {:.2f}'.format(preço, desconto))