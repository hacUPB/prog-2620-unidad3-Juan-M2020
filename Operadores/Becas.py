promedio = float(input("Ingresa el promedio: "))
nivel = float(input("Ingrese si nivel socioeconomico: "))


# Evaluación
tiene_beca = (promedio >= 9.0) or (nivel == 1 and promedio > 8.0)

# Resultado
print(tiene_beca)