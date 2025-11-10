from variablesHLF import *
import random

'''
En este .JS voy a diseñar las funciones que necesitaran cada uno de los participantes,
tanto el ordenador así como el jugador, para poder desarrollar en juego.

'''

#------------------------------------------------------------------------------
# Definición: Función que creara un tablero de las proporciones solicitas pero modificando la 
# constante se midifiraría el tamaño del tablero,
# Parametros: lista que contiene el t ablero a crear.
# Return: Tablero creado,
def crearTablero(lstTablero):
    for i in range(TamañoTablero):
        fila = ["*"] * TamañoTablero
        lstTablero.append(fila)
    return lstTablero

#------------------------------------------------------------------------------
# Definición: Función que nos pintara el tablero en pantalla.
# Parametros: Tablero a pintar en forma de lista
# Return:
def pintarTablero(lstTablero):
    for fila in lstTablero:
        print(" ".join(str(c) for c in fila))
    print("----------------------------------------")

#------------------------------------------------------------------------------
# Definición: Función que nos dice si queda algún barco sin hundir.
# Parametros: Tablero por el que queremos preguntar
# Return: Booleano que nos indicará si hay objetivos o no.
def quedanBarcos(lstTablero):
    return any("B" in fila for fila in lstTablero)

#------------------------------------------------------------------------------
# Definición: Función que nos pintara en el tablero el barco con las particularidases indicadas.
# Parametros: Tablero a pintar en forma de lista.
#             El nombre que tendra el barco.
#             El Tamaño del barco.
#             La cordenada X en el tablero
#             La cordenada Y en el tablero
# Return: El tablero resultante tras incluir el nuevo barco.
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

#------------------------------------------------------------------------------
# Definición: Función que nos pintara en el tablero el barco con de forma aleatoria.
# Parametros: Tablero a pintar en forma de lista.
#             El nombre que tendra el barco.
#             El Tamaño del barco.
#             La cordenada X en el tablero
#             La cordenada Y en el tablero
# Return: El tablero resultante tras incluir el nuevo barco

def ponerBarcoMac(lstTablero, strNomBarco, intTamano):
    
    while True:
        cordX = random.randint(0, TamañoTablero - 1)
        cordY = random.randint(0, TamañoTablero - intTamano)
        if all(lstTablero[cordX][cordY + i] == "*" for i in range(intTamano)):
            for i in range(intTamano):
                lstTablero[cordX][cordY + i] = "B"
            break
    return lstTablero


#------------------------------------------------------------------------------
# Definición: Función que dispara a un barco y nos indicará si hemos acertado o no, o si hemos fallado,
#   modificando el tablero según las ditintas posiblidades que se pueden dar.
# Parametros: Tablero a pintar en forma de lista.
#             El nombre que tendra el barco.
#             La cordenada X en el tablero.
#             La cordenada Y en el tablero.
#             La cantidad de disparos efectuados.
# Return: El tablero resultante tras incluir el nuevo barco.
#         El resultado del disparo.
def dispararBarco(lstTablero, cordX, cordY, contDisparos):
    print(f"Disparo #{contDisparos} en ({cordX+1}, {cordY+1})")

    boolAcierto = True
    if contDisparos > ContDisparosTotales:
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

#------------------------------------------------------------------------------
# Definición: Nos controlará y facilitará cada una de las jugadas efectuadas durante la partida.
# Parametros: Tablero a pintar en forma de lista.
#             Contador de disparos.
#             Condicional que nos indica si el jugador puede seguir jugando.
#             Quien el el jugador que está jugando
def jugadaMia(lstTablero, contDisparos, bolSeguirJugando, intQuien):
    bolSeguir = True
    acierto = False


# Mientras la condicion sea cierta seguimos jugando
    while bolSeguir:
        # Dependiendo quien este jugando intQuien tendra un avlor u otro
        # 0 Jugador
        # 1 maquina
        if intQuien == 0:
            # Se solicitan las cooerdenass aljugador
            print("\nIntroduce coordenadas (1 a", TamañoTablero, ")")
            x = input("Coordenada X: ")
            y = input("Coordenada Y: ")

            if not (x.isdigit() and y.isdigit()):
                print("Debes introducir números válidos.")
                continue
        else:
            # Se calculan las cooerdenass para la mmaquina
            x = random.randint(1, TamañoTablero)
            y = random.randint(1, TamañoTablero)

        x = int(x)
        y = int(y)
        # Sumanos un disparo nuevo
        contDisparos += 1

        lstTablero, acierto = dispararBarco(lstTablero, x - 1, y - 1, contDisparos)

        # Para el caso que ya no queden barcos
        if not quedanBarcos(lstTablero):
            print("¡Has hundido todos los barcos!")
            bolSeguirJugando = False
            bolSeguir = False
        # Para el caso de que el jugador haya extralimitado el numero de disparos
        elif contDisparos >= 15:
            print("Has agotado tus disparos. Fin del juego.")
            bolSeguirJugando = False
            bolSeguir = False
        # Para el caso que ya no haya acertado el disparo
        elif not acierto:
            print("Has fallado el tiro.")
            bolSeguir = False  
        # y si no se dan el resto de condiciones 
        else:
        
            if intQuien == 0:
                strJugar = input("¡Has acertado! ¿Quieres continuar jugando? (S/N): ")
                if strJugar.upper() == "S":
                    bolSeguir = True 
                else:
                    bolSeguir = False
                    bolSeguirJugando = False
            else:
                bolSeguir = True  
                
        # Pintamos el resultado de la jugada
        print("Tablero Actual")
        print("-------------")
        pintarTablero(lstTablero)
        print("")

    return lstTablero, contDisparos, bolSeguirJugando, acierto
#------------------------------------------------------------------------------
