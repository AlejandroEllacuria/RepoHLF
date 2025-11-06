from variablesHLF import *
import random

def crearTablero(lstTablero):
    for i in range(TamañoTablero):
        fila = ["*"] * TamañoTablero
        lstTablero.append(fila)
    return lstTablero


def pintarTablero(lstTablero):
    for fila in lstTablero:
        print(" ".join(str(c) for c in fila))
    print("----------------------------------------")


def quedanBarcos(lstTablero):
    return any("B" in fila for fila in lstTablero)


def ponerBarco(lstTablero, strNomBarco, intTamano, cordX, cordY):
    if cordY + intTamano > TamañoTablero or cordX >= TamañoTablero:
        print("El barco no cabe en esa posición")
        return lstTablero

    for i in range(intTamano):
        if lstTablero[cordX][cordY + i] == "B":
            print("Ya está ocupada esa posición")
            return lstTablero

    for i in range(intTamano):
        lstTablero[cordX][cordY + i] = "B"

    return lstTablero


def ponerBarcoMac(lstTablero, strNomBarco, intTamano):
    while True:
        cordX = random.randint(0, TamañoTablero - 1)
        cordY = random.randint(0, TamañoTablero - intTamano)
        if all(lstTablero[cordX][cordY + i] == "*" for i in range(intTamano)):
            for i in range(intTamano):
                lstTablero[cordX][cordY + i] = "B"
            break
    return lstTablero


def ponerTodosBarcoMac(lstTablero):
    lstTablero = ponerBarco(lstTablero, "Barco4", 4, 1, 1)
    lstTablero = ponerBarco(lstTablero, "Barco31", 3, 4, 1)
    return lstTablero


def dispararBarco(lstTablero, cordX, cordY, contDisparos):
    print(f"Disparo #{contDisparos} en ({cordX+1}, {cordY+1})")

    if contDisparos > 15:
        print("Juego terminado, has superado el número de disparos.")
        return lstTablero

    if cordX < 0 or cordX >= TamañoTablero or cordY < 0 or cordY >= TamañoTablero:
        print("Coordenadas fuera del tablero.")
        return lstTablero

    valor = lstTablero[cordX][cordY]

    if valor == "B":
        print("¡Tocado!")
        lstTablero[cordX][cordY] = "\033[31mB\033[0m"  # rojo
    elif valor == "*":
        print("¡Agua!")
        lstTablero[cordX][cordY] = "\033[34mA\033[0m"  # azul
    elif valor in ["\033[31mB\033[0m", "\033[34mA\033[0m"]:
        print("Ya has disparado aquí.")
    else:
        print("Error inesperado en dispararBarco.")

    return lstTablero

