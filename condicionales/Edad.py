#clasificador dsegun la edad 

edad = int(input("ingrese su edad: "))

if edad >= 0 and edad <=125:
    if edad < 6:
        etapa = "Infancia"
    elif edad < 12:
        etapa = "Niñez"
    elif edad < 20:
        etapa = "Adolescencia"
    elif edad < 25:
        etapa = "Juventud"
    elif edad < 60:
        etapa = "Adultez"
    else:
        etapa = "Vejez"
    print(f"A sus {edad} años, Usted esta en la etapa de {etapa}")
    
else:
    print("El numero ingresado no es una edad valida")