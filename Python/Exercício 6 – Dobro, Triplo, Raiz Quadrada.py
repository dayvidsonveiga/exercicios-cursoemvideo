
#Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n1 = int(input('Digite um numero: '))
d = n1 * 2
t = n1 * 3
r = n1 ** (1/2)
print('O dobro, triplo e a raiz quadrada respectivamente: \n {} \n {} \n {:.2f}'.format(d, t, r))