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

1. ¿La IA nombró bien las variables? 
2. ¿Usó las estructuras adecuadas? 
3. ¿Cometió algún error de lógica o no consideró algún caso? 
4. Escribe qué modificaciones le hiciste para que encaje perfectamente con la Fase 4.