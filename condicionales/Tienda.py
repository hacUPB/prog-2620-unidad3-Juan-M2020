'''
Una tienda ofrece una promoción, por la compra de 3 artículos, el costo del elemento de menor valor tiene un descuento del 50%
'''

articulo1 = int(input("ingrese el precio del articulo 1: "))
articulo2 = int(input("ingrese el precio del articulo 2: "))
articulo3 = int(input("ingrese el precio del articulo 3: "))

if articulo1 < articulo2:
    temp = articulo1
else:
    temp = articulo2

if temp < articulo3:
    menor = temp
else:
    menor = articulo3

total = articulo1 + articulo2 + articulo3
total = total - (menor * 0.50)

print("Total a pagar:", total)