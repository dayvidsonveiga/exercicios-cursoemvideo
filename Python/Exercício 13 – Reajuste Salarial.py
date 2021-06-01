
#Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Informe o seu salário: R$ '))
novo = salario + (salario * 15 / 100)
print('O salário atual é R$ {:.2f} e seu novo salário com acréscimo de 15% de aumento passará a ser: R$ {:.2f}'.format(salario, novo))