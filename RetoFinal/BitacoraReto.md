# A350
**DATOS DE ENTRADA**

|Entrada| descripcion |
|-------|---------|
|COMBUSTIBLE | cantidad de combistible al despegar en kg|
|DISTANCIA | distancia que debe recorrer el avion Km |
|WAYPOINT |puntos de control del vuelo
|VIENTO| si hay viento en contra o viento a favor |
|PESO | peso del avion al despegar|
|ALTITUD| Altitud de vuelo |

**DATOS INTERMEDIOS**

| Proceso     | Descripción   |
| ----------- | ------------- |
| CONSUMO | calcula combustible usado en el tramo |
| VIENTO | aumenta o reduce consumo según viento |
| PESO | modifica consumo según peso total |
| ALTITUD| modifica consumo según altitud |
| COMBUSTIBLE | resta el consumo al combustible restante |
| PESO RECALCULADO  | suma el del peso avion + combustible actual |
| RESERVA | revisa si el combustible está por debajo de la reserva |
| ABORTAR | detiene el ciclo del vuelo |



**DATOS DE SALIDA**

| Salida| Descripción|
| -------- | ------------- |
| CONSUMO| combustible consumido en el tramo       |
| COMBUSTIBLE | combustible que queda después del tramo |
| PESO | peso actual del avión                   |
| ALERTA| alerta si se baja de la reserva legal   |
| ABORTO | aviso de desvío a aeropuerto alterno    |
| EXITOSO | vuelo completado correctamente          |





.


>**PSEUDOCODIGO**    
```

INICIO

    DEFINIR CONSUMO_BASE = 6.4
    DEFINIR RESERVA_LEGAL = 3000

    ESCRIBIR "Sistema de Monitoreo de Combustible y Seguridad en Ruta"

    LEER combustible_inicial
    LEER peso_avion

    combustible_actual = combustible_inicial

    PARA tramo DESDE 1 HASTA 5 HACER

        ESCRIBIR "Tramo ", tramo

        LEER distancia_tramo
        LEER viento
        LEER altitud

        peso_total = peso_avion + combustible_actual

        consumo = calcular_consumo_tramo(distancia_tramo, viento, peso_total, altitud)

        combustible_actual = combustible_actual - consumo

        ESCRIBIR "Consumo del tramo: ", consumo
        ESCRIBIR "Combustible restante: ", combustible_actual
        ESCRIBIR "Peso total del avion: ", peso_total

        SI combustible_actual <= RESERVA_LEGAL ENTONCES

            ESCRIBIR "ALERTA CRITICA"
            ESCRIBIR "Combustible por debajo de la reserva legal"
            ESCRIBIR "Desviarse al aeropuerto alterno"

            TERMINAR CICLO

        FIN SI

    FIN PARA

    SI combustible_actual > RESERVA_LEGAL ENTONCES

        ESCRIBIR "Vuelo completado con exito"

    FIN SI

FIN

```



>**INFORMACION DEL PROYECTO**

**1. ¿La IA nombró bien las variables?**

Sí, en general la IA utilizó nombres de variables claros, lo cual facilita la comprensión del programa con palabras como:

- combustible_actual
- distancia_tramo
- peso_total
- altitud
- calcular_consumo_tramo

Estos nombres son adecuados porque representan directamente el propósito de cada variable dentro del sistema.
Sin embargo, se realizó un pequeño ajuste para mantener mayor coherencia:

Se separó peso_avion y peso_total, permitiendo diferenciar entre el peso estructural y el peso dinámico durante el vuelo.

**2. ¿Usó las estructuras adecuadas?**

la IA utilizó correctamente las estructuras fundamentales de programación requeridas en el proyecto:

Funciones: para calcular el consumo (calcular_consumo_tramo)
Bucles (for): para simular los tramos del vuelo
Condicionales (if, elif): para:
evaluar el tipo de viento
ajustar el consumo
verificar la reserva legal
Uso de break: para detener el programa en caso de emergencia

**3. ¿Cometió algún error de lógica o no consideró algún caso?** 
La lógica general fue correcta, pero sí hubo algunos aspectos que se mejoraron:

Inicialmente, el peso del avión no se actualizaba dinámicamente con el consumo de combustible.
No se diferenciaba claramente entre peso estructural (peso_avion) y peso total (peso_total).
No se contemplaba explícitamente que el viento puede cambiar en cada tramo (aunque luego se corrigió al pedirlo dentro del ciclo).

También se identificó que:

No se validaban entradas del usuario (por ejemplo, si escribe mal el tipo de viento), aunque esto no era obligatorio para el reto.

**4. Escribe qué modificaciones le hiciste para que encaje perfectamente con la Fase 4.**

Se realizaron las siguientes mejoras al código original:

Se agregó el peso del avión como entrada inicial, para hacerlo más realista.
Se implementó el cálculo dinámico del peso total:
peso_total = peso_avion + combustible_actual

Esto permite que el consumo cambie a medida que el avión se vuelve más ligero.

Se integraron todos los factores en la función calcular_consumo_tramo:
- distancia
- viento
- peso
- altitud

Se ubicaron correctamente las entradas dentro del bucle, permitiendo que:
el viento cambie por tramo
la altitud cambie por tramo
Se aseguró el uso correcto del condicional de seguridad:
```
SI combustible_actual ≤ RESERVA_LEGAL
```
junto con el uso de break para abortar la simulación.

Se mejoró la organización del código, separando:
- constantes
- entradas
- función
- lógica principal


## REFLEXION

Durante el desarrollo del proyecto SMCS se utilizó inteligencia artificial como apoyo para la construcción inicial del algoritmo y su implementación en Python. Sin embargo, el uso de esta herramienta no fue copiar y pegar, sino que implicó un análisis crítico del código generado.

**Análisis de variables**

La IA propuso nombres de variables adecuados y descriptivos, como combustible_actual, distancia_tramo y consumo. Estos nombres facilitan la comprensión del programa.

pero, se identificó una mejora importante: la separación entre peso_avion y peso_total. Inicialmente, la IA no consideraba el peso como una variable dinámica, por lo que se modificó el modelo para calcular:

peso_total = peso_avion + combustible_actual

Esto permitió representar de forma más realista el comportamiento del avión.

**Análisis de estructuras**

La IA utilizó correctamente las estructuras fundamentales de programación:

- funciones (def)
- ciclos (for)
- condicionales (if, elif)
- uso de break para detener la ejecución

Estas estructuras son apropiadas para simular el comportamiento del sistema.

Sin embargo, fue necesario reorganizar el flujo del programa para asegurar que las entradas como viento y altitud se solicitaran dentro del bucle, permitiendo que cambien en cada tramo.

**Análisis de errores y limitaciones**

Aunque la lógica general era correcta, se identificaron algunas limitaciones:

el peso del avión no se actualizaba dinámicamente
no se modelaba la reducción de consumo al disminuir el peso
no se consideraba explícitamente el cambio de condiciones en cada tramo
no se validaban las entradas del usuario
Estos aspectos fueron corregidos para mejorar la calidad del modelo.

**Modificaciones realizadas**

Para adaptar el código a los requisitos del proyecto, se realizaron las siguientes mejoras:

Se agregó el peso del avión como entrada inicial.
Se implementó el cálculo dinámico del peso total.
Se integraron los factores de viento, altitud y peso en la función de consumo.
Se ajustó la estructura del programa para permitir cambios por tramo.
Se implementó correctamente la verificación de la reserva legal con una estructura condicional.
Se mejoró la organización del código para mayor claridad.


# Codigo inicial por la IA
```
# Sistema de Monitoreo de Combustible y Seguridad en Ruta
# Avión: Airbus A350

CONSUMO_BASE = 6.4   # kg por km
RESERVA_LEGAL = 3000 # kg


def calcular_consumo_tramo(distancia, viento):

    consumo = distancia * CONSUMO_BASE

    if viento == "headwind":
        consumo = consumo * 1.15
    elif viento == "tailwind":
        consumo = consumo * 0.90
    else:
        consumo = consumo

    return consumo


combustible_actual = float(input("Ingrese combustible inicial (kg): "))

for tramo in range(1, 6):

    print("\nTramo", tramo)

    distancia = float(input("Distancia del tramo (km): "))
    viento = input("Tipo de viento (headwind/tailwind/crosswind): ")

    consumo = calcular_consumo_tramo(distancia, viento)

    combustible_actual = combustible_actual - consumo

    print("Consumo del tramo:", consumo, "kg")
    print("Combustible restante:", combustible_actual, "kg")

    if combustible_actual <= RESERVA_LEGAL:
        print("ALERTA CRÍTICA")
        print("Combustible por debajo de reserva legal")
        print("Desviarse a aeropuerto alterno")
        break


if combustible_actual > RESERVA_LEGAL:
    print("\nVuelo completado con éxito")

```

# imagenes del programa

![imagen1](../RetoFinal/Captura%20de%20pantalla%202026-03-26%20160949.png)
>VUELO EXITOSO
-----------------------------
![imagen1](../RetoFinal/Captura%20de%20pantalla%202026-03-26%20161208.png)
>ALERTA CRITICA
-----------------------------