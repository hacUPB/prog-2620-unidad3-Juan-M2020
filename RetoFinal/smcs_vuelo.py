CONSUMO_BASE = 6.4
RESERVA_LEGAL = 3000

peso_avion = float(input("Peso del avión sin combustible (kg): "))
combustible_actual = float(input("Combustible inicial (kg): "))

def calcular_consumo_tramo(distancia, viento, peso_total, altitud):

    consumo = distancia * CONSUMO_BASE

    if viento == "headwind":
        consumo *= 1.15
    elif viento == "tailwind":
        consumo *= 0.90

    if peso_total > 250000:
        consumo *= 1.10
    elif peso_total < 200000:
        consumo *= 0.95

    if altitud < 30000:
        consumo *= 1.10
    elif altitud > 40000:
        consumo *= 0.95

    return consumo


for tramo in range(1,6):

    print("\nTramo", tramo)

    distancia = float(input("Distancia del tramo (km): "))
    viento = input("Tipo de viento (headwind/tailwind/crosswind): ")
    altitud = float(input("Altitud (ft): "))

    peso_total = peso_avion + combustible_actual

    consumo = calcular_consumo_tramo(distancia, viento, peso_total, altitud)

    combustible_actual -= consumo

    print("Consumo:", round(consumo,2))
    print("Combustible restante:", round(combustible_actual,2))

    if combustible_actual <= RESERVA_LEGAL:

        print("ALERTA CRITICA")
        print("Desviarse al aeropuerto alterno")

        break


if combustible_actual > RESERVA_LEGAL:
    print("Vuelo completado con éxito")