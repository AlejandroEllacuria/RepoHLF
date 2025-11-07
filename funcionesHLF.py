from variablesHLF import *
import random

#------------------------------------------------------------------------------
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



def dispararBarco(lstTablero, cordX, cordY, contDisparos):
    print(f"Disparo #{contDisparos} en ({cordX+1}, {cordY+1})")

    boolAcierto = True
    if contDisparos > contDisparosTotales:
        print("Juego terminado, has superado el número de disparos.")
        boolAcierto = False
        return lstTablero,boolAcierto 

    if cordX < 0 or cordX >= TamañoTablero or cordY < 0 or cordY >= TamañoTablero:
        print("Coordenadas fuera del tablero.")
        boolAcierto = False
        return lstTablero,boolAcierto

    valor = lstTablero[cordX][cordY]

    if valor == "B":
        print("¡Tocado!")
        lstTablero[cordX][cordY] = "\033[31mB\033[0m"  # rojo
        boolAcierto = True
    elif valor == "*":
        print("¡Agua!")
        lstTablero[cordX][cordY] = "\033[34mA\033[0m"  # azul
        boolAcierto = False
    elif valor in ["\033[31mB\033[0m", "\033[34mA\033[0m"]:
        print("Ya has disparado aquí.")
        boolAcierto = False
    else:
        print("Error inesperado en dispararBarco.")
        boolAcierto = False

    return lstTablero,boolAcierto

def jugadaMia(lstTablero, contDisparos, bolSeguirJugando, intQuien):
    bolSeguir = True

    while bolSeguir:
        if intQuien == 0:
            print("\nIntroduce coordenadas (1 a", TamañoTablero, ")")
            x = input("Coordenada X: ")
            y = input("Coordenada Y: ")

            if not (x.isdigit() and y.isdigit()):
                print("Debes introducir números válidos.")
                continue
        else:
            x = random.randint(1, TamañoTablero)
            y = random.randint(1, TamañoTablero)

        x = int(x)
        y = int(y)

        contDisparos += 1
        lstTablero, boolPerdido = dispararBarco(lstTablero, x - 1, y - 1, contDisparos)

        if not quedanBarcos(lstTablero):
            print("¡Has hundido todos los barcos!")
            bolSeguirJugando = False
            bolSeguir = False
        elif contDisparos >= 15:
            print("Has agotado tus disparos. Fin del juego.")
            bolSeguirJugando = False
            bolSeguir = False
        elif boolPerdido == False:
            print("Has fallado el tiro.")
            bolSeguir = boolPerdido
        else:
            if intQuien == 0:
                strJugar = input("¿Quieres continuar jugando? (S/N): ")
                if strJugar.upper() == "S":
                    bolSeguir = True
                else:
                    bolSeguir = False
                    bolSeguirJugando = False
            else:
                bolSeguir = False  # la máquina solo hace un disparo

        print("Tablero Actual")
        print("-------------")
        pintarTablero(lstTablero)
        print("")

    return lstTablero, contDisparos, bolSeguirJugando

'''
def jugadaMia (lstTablero,contDisparos,bolSeguirJugando,intQuien):
    
    bolSeguir = True
    
    while bolSeguir:
        if (intQuien == 0):
            print("\nIntroduce coordenadas (1 a", TamañoTablero, ")")
            x = input("Coordenada X: ")
            y = input("Coordenada Y: ")

            
            if not (x.isdigit() and y.isdigit()):
                print("Debes introducir números válidos.")
                continue
        else:
            x = random.randint(1,TamañoTablero)
            y = random.randint(1, TamañoTablero)
            
        x = int(x)
        y = int(y)

        contDisparos += 1
        lstTablero , boolPerdido = dispararBarco(lstTablero, x - 1, y - 1,contDisparos,)
        

        if not quedanBarcos(lstTablero):
            print("¡Has hundido todos los barcos!")
            bolSeguirJugando = False
            bolSeguir = False
        elif contDisparos >= 15:
            print("Has agotado tus disparos. Fin del juego.")
            bolSeguirJugando = False
            bolSeguir = False
        elif boolPerdido == False:
            print("Has Falllado  el tiro.")
            bolSeguir = boolPerdido
        else:
            strJugar = input("¿Quieres continuar jugando? (S/N): ")
            if strJugar.upper() == "S":
                bolSeguir = True
            else:
                bolSeguir = False
                bolSeguirJugando = False
        

       
        print("Tablero Mio")
        print("-------------")
        pintarTablero(lstTablero)
        print("")


    return lstTablero,contDisparos,bolSeguirJugando
'''



#------------------------------------------------------------------------------
