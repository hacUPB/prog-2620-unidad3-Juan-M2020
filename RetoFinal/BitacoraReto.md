# A350
**DATOS DE ENTRADA**

|Nombre| descripcion |
|-------|---------|
|COMBUSTIBLE | cantidad de combistible al despegar en kg|
|DISTANCIA | distancia que debe recorrer el avion Km |
|WAYPOINT |puntos de control del vuelo
|TIPO DE VIENTO| si hay viento en contra o viento a favor |
|PESO | peso del avion al despegar|
|ALTITUD| 

**DATOS INTERMEDIOS**

|Nombre| descripcion |
|-------|---------|
|COMBUSTIBLE | combustible gastado del avion |
|DISTANCIA|distancia recorrida por el avion |
|VIENTO| variaciones del viento|
|


**DATOS DE SALIDA**
|Nombre| descripcion |
|-------|---------|
|COMBUSTIBLE | combustible restante del avion |
|DISTANCIA| distancia recorrida del avion|
|ALERTA | combustible de reserva si se termina el principal |
|CONSUMO |consumo que lleva el avion en el recorrido| 






.


># PSEUDOCODIGO    
```
INICIO 
    MOSTRAR : A350
    ESCRIBIR "ingrese el combustible que lleva el avion"
    LEER combustible1

    ESCRIBIR "Peso del avion con el que despega"
    LEER peso

    ESCRIBIR "ingrese la distacia a recorrer"
    LEER distacia
    
    ESCRIBIR "ingrese la cantidad de waypoints que hay en la ruta "

    conbustibleActual = conbustible1 - consumo

        SI conbustible < 

FIN
```