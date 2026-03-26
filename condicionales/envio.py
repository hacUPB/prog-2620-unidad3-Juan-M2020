'''
Un almacén cobra $9 000 por costos de envío, pero ofrece el envío a domicilio gratis para compras superiores a $100 000.En caso contrario, no hay ningún descuento. Solicite al usuario el valor de la compra y calcule el valor total a pagar.
'''
#la moneda es en pesos colombianos
compra = int(input("ingrese el valor de la compra: "))
#total = compra + 9000
# if compr > 100000
#   total = compra
envio = 0
compra = int(input("Ingrese el valor de la compra>> "))
if compra < 100000:
	envio = 9000
total = compra + envio
print(f"El total de la compra es {total}")