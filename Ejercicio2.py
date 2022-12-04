import random

def agregar (misiones):
    tipo = input("Cual es el tipo de la misión: ")
    planeta = input("En que planeta se realizara la misión: ")
    general = input("Quien ordena la misión: ")

    mision = [tipo, planeta, general]
    misiones.append(mision)

def recursos(misiones):
    scout = 0
    speeder = 0
    storm = 0
    vehiculos = 0
    for mision in misiones:
        if mision[2] == "Palpatine" or mision[2] == "Darth Vader":
            scout = input("Cuantos Scout Troopers se necesitan: ")
            speeder = input("Cuantas Speeper Bike se necesitan: ")
            storm = input("Cuantos Stormtroopers se necesitan: ")
            print("Los vehiculos disponibles son: AT-AT, AT-RT, AT-TE, AT-DP, AT-ST, AT-M6, AT-MP, AT-DT")
            vehiculos = input("Que vehiculos se necesitan: ")
        else: 
            if mision[0] == "exploración":
                scout = 15
                speeder = 2
            elif mision[0] == "contención":
                storm = 30
                vehiculos = [random.choice(["AT-AT", "AT-RT", "AT-TE", "AT-DP", "AT-ST"]) + ", " + random.choice(["AT-AT", "AT-RT", "AT-TE", "AT-DP", "AT-ST"])+ ", " + random.choice(["AT-AT", "AT-RT", "AT-TE", "AT-DP", "AT-ST"])]
            elif mision[0] == "ataque":
                storm = 50
                vehiculos = [random.choice(["AT-AT", "AT-RT", "AT-TE", "AT-DP", "AT-ST", "AT-M6", "AT-MP", "AT-DT"]) + ", " + random.choice(["AT-AT", "AT-RT", "AT-TE", "AT-DP", "AT-ST", "AT-M6", "AT-MP", "AT-DT"]) + ", " +random.choice(["AT-AT", "AT-RT", "AT-TE", "AT-DP", "AT-ST", "AT-M6", "AT-MP", "AT-DT"]) + ", " +random.choice(["AT-AT", "AT-RT", "AT-TE", "AT-DP", "AT-ST", "AT-M6", "AT-MP", "AT-DT"]) + ", " +random.choice(["AT-AT", "AT-RT", "AT-TE", "AT-DP", "AT-ST", "AT-M6", "AT-MP", "AT-DT"]) + ", " +random.choice(["AT-AT", "AT-RT", "AT-TE", "AT-DP", "AT-ST", "AT-M6", "AT-MP", "AT-DT"]) + ", " +random.choice(["AT-AT", "AT-RT", "AT-TE", "AT-DP", "AT-ST", "AT-M6", "AT-MP", "AT-DT"])]
            else:
                print("La misión introducida no es valida")

    print("Los recursos asignados son:")
    print("Scout Troopers: ", scout)
    print("Speeper Bike: ", speeder)
    print("Stormtroopers: ", storm)
    print("Vehiculos: ", vehiculos)

def mostrar(misiones):
    print("Misiones:")
    for mision in misiones:
        print("Tipo:", mision[0])
        print("Planeta: ", mision[1])
        print("General: ", mision[2])


def menu():
    print("1. Agregar misión.")
    print("2. Mostrar los recursos asignados.")
    print("3. Mostrar la información de las misiones.")
    print("4. Salir.")

def programa ():
    misiones = []
    opcion = 0
    while opcion !=4:
        menu()
        opcion= int(input("Ingrese una opción: "))
        if opcion == 1:
            agregar(misiones)
        elif opcion == 2:
            recursos(misiones)
        elif opcion == 3:
            mostrar(misiones)

programa()
