#pseudocodigo
#INICIO
#    Leer n
#    factorial = 1
#    Para i desde 1 hasta n
#    factorial = factorial * i
#    Mostrar factorial
#FIN
#python
n = int(input("Ingresa un número entero: "))
factorial = 1

for i in range(1, n + 1):
    factorial *= i

print("El factorial es:", factorial)