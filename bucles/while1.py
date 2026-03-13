 # Desde 100 hasta el 50, pero unicamente los impares

numero = 100
while numero > 50:
    res = numero % 2
    if res == 1:
        print(numero)
    numero -= 1      #numero = numero + 5