
#Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.


num = int(input('Me diga um numero qualquer: '))
resultado = num % 2
if resultado == 0:
  print('O numero {} é par!'.format(num))
else:
  print('O numero {} é impar!'.format(num))