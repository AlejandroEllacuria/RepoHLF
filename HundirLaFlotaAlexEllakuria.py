from variablesHLF import *
from funcionesHLF import *
import time

import random
import sys
import os

'''
Hundir la Flota es un juego de tablero  en el que dos jugadores disponen de una flota de barcos colocados dentro de una 
cuadrícula.
Cada jugador, por turnos, dispara a coordenadas del tablero enemigo intentando acertar y hundir todos los barcos del oponente.
El primer jugador que logre hundir todos los barcos del rival gana la partida.

'''

# Defino las variables necesarias.
lstTableroMac = []
lstTableroMio = []
contDisparosMio = 0
contDisparosMac = 0
contTableroMac = 0

# Cargo el tablero con los barcos que corresponden al jugador.
lstTableroMio = crearTablero(lstTableroMio)
lstTableroMio = ponerBarcoMac(lstTableroMio,"Barco4Mio",4)
lstTableroMio = ponerBarcoMac(lstTableroMio,"Barco31Mio",3)
lstTableroMio = ponerBarcoMac(lstTableroMio,"Barco32Mio",3)
lstTableroMio = ponerBarcoMac(lstTableroMio,"Barco21Mio",2)
lstTableroMio = ponerBarcoMac(lstTableroMio,"Barco22Mio",2)
lstTableroMio = ponerBarcoMac(lstTableroMio,"Barco23Mio",2)
lstTableroMio = ponerBarcoMac(lstTableroMio,"Barco4Mio",1)
lstTableroMio = ponerBarcoMac(lstTableroMio,"Barco4Mio",1)
lstTableroMio = ponerBarcoMac(lstTableroMio,"Barco4Mio",1)
lstTableroMio = ponerBarcoMac(lstTableroMio,"Barco4Mio",1)

# Cargo el tablero con los barcos que corresponden al ordenador.
lstTableroMac = crearTablero(lstTableroMac)
lstTableroMac = ponerBarcoMac(lstTableroMac,"Barco4",4)
lstTableroMac = ponerBarcoMac(lstTableroMac,"Barco31",3)
lstTableroMac = ponerBarcoMac(lstTableroMac,"Barco32",3)
lstTableroMac = ponerBarcoMac(lstTableroMac,"Barco21",2)
lstTableroMac = ponerBarcoMac(lstTableroMac,"Barco22",2)
lstTableroMac = ponerBarcoMac(lstTableroMac,"Barco23",2)
lstTableroMac = ponerBarcoMac(lstTableroMac,"Barco4",1)
lstTableroMac = ponerBarcoMac(lstTableroMac,"Barco4",1)
lstTableroMac = ponerBarcoMac(lstTableroMac,"Barco4",1)
lstTableroMac = ponerBarcoMac(lstTableroMac,"Barco4",1)

os.system('cls' if os.name == 'nt' else 'clear')

# Pinta el tablero del jugador.
print("Tablero Jugador")
print("-------------")
pintarTablero(lstTableroMac)
print("")

# Pinta el tablero del ordenador.
print("Tablero Ordenador")
pintarTablero(lstTableroMio)
print("")

# Cuerpo principal de la aplicación, en la cual se atiende los jugadores hasta que, bien por una situación del juego, 
# o bien por cualquier que se pudiera dar el juego finalice. 
# 0 = jugador, 1 = máquina

try:
    turno = 0  

    while bolSeguirJugando:
        if turno == 0:
            print("\n Turno del JUGADOR")
            lstTableroMac, contDisparosMio, bolSeguirJugando, acierto = jugadaMia(
                lstTableroMac, contDisparosMio, bolSeguirJugando, 0 )
            if not bolSeguirJugando:
                break
            if not acierto:
                turno = 1
        else:
            print("\n Turno de la MÁQUINA")
            lstTableroMio, contDisparosMac, bolSeguirJugando, acierto = jugadaMia(
                lstTableroMio, contDisparosMac, bolSeguirJugando, 1 )
            if not acierto:
                turno = 0
    
except Exception as e:
    print("Ha surgido un problema:", e)