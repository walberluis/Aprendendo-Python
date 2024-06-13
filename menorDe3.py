# Faça um programa que leia 3 números inteiros e imprima o menor deles.

lista = []

for n in range(0, 3, 1):
    num = int(input())
    lista.insert(n, num)

lista.sort()
print(lista[0])