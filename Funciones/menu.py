# Funcion menu: imprime un menu de opciones y retorna la
#opcion elegida por el usuario

def menu():
    opcion = 0
    while opcion < 1 or opcion > 4:
    # no se debe permitir seleccionar una opcion que no esta 
        print("1. Suma\n2. Resta\n3. Multiplicacion\n4. Division")
        opcion = int(input("seleccione una opcion: "))
        if opcion < 1 or opcion > 4:
            print("Opcion elegid no valida...\n")
    return opcion


operacion = menu()
print (f"El usuario eligio la opcion {operacion}")
