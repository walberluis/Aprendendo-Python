# pegue todos os 10 primeiros múltiplos do número da entrada, sem usar condicional(if)

i = int(input())

for n in range(1, 11, 1):
    #print(i)
    aux = i * n
    print(aux)
