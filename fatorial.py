# Dado um inteiro não negativo n, imprima seu fatorial.

def fatorial (num, valor):
    if(num == 0 or num == 1):
        print(1)
    else:
        for n in range(1, num + 1):
            valor = n * valor
        print(valor)

x = int(input())
fatorial(x, 1)