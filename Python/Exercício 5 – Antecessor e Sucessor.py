
#Exercício Python 5: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

n1 = int(input('Digite o primeiro numero: '))
ant = n1 - 1
suc = n1 + 1
print('O numero digitado foi {} , seu antecessor é {} e o seu sucessor é {}'.format(n1, ant, suc))