# Leia um inteiro N.
# Depois, leia até 20 inteiros X0, X1, ..., X20. Seu programa deve imprimir quantas vezes o inteiro N aparece nos X inteiros.

i = int(input())
caixinha = 0
for n in range (0, 20):
    numero = int(input())
    if(numero == -1):
        print(f"{i} aparece {caixinha} vezes\n")
        break

    if(numero == i):
        caixinha += 1
