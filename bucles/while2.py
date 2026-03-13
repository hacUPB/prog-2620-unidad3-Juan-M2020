# solicitar dos numeros al usuario e imprimir valores pares que hay entre dichos numeros

n1 = int(input("ingresar el primer numero"))
n2 = int(input("ingresar el segundo numero"))

if n1 > n2: 
    mayor = n1
    menor = n2

else:
    mayor = n2
    menor= n1
 
while menor <= mayor:  
    if menor % 2 == 0:
        print(numero)
    numero += 1
