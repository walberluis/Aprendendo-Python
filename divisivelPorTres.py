# O problema envolve achar a quantidade de divisores de um número que são divisíveis por 3.

def contando(numero, caixinha):
    for valor in range(3, numero, 3):
        
        auxiliar = valor
        if(numero % auxiliar == 0):
            caixinha += 1
    
    return caixinha + 1


numero = int(input())

conferir = numero%3
if(conferir != 0):
    print("O numero nao possui divisores multiplos de 3!\n")
else:
    print(contando(numero, 0))