personas = int(input("Ingresa el numero de personas: "))
cuenta = float(input("Ingrese el valor de la cuenta: "))
porcentaje_propina = int(input("Ingresa el porcentade de propina: "))


# Cálculos
porcentaje_propina = porcentaje_propina / 100
propina = cuenta * porcentaje_propina
total = cuenta + propina
pago_por_persona = total / personas

# Resultados
print("Propina:", propina)
print("Total a pagar:", total)
print("Cada persona paga:", pago_por_persona)