#generar tablero de ajedres con movimiento mostrando el estado del tablero y registrando  captura de piesas

#crea diccionario(clave "coordenada" valor = " ")
tablero = {
    "a1": "TorreB", #fila 1
    "b1" :"CaballoB",
    "c1":"AlfilB", 
    "d1": "ReinaB", 
    "e1":"ReyB",
    "f1":"AlfilB",
    "g1":"CaballoB",
    "h1":"TorreB",
    # fila 2
    **{f"{columna}2":"PeonB" for columna in "abcdefgh"},
    # fila 3
    **{f"{columna}3": " " for columna in "abcdefgh"},
    # fila 4
    **{f"{columna}4": " " for columna in "abcdefgh"},
    # fila 5
     **{f"{columna}5": " " for columna in "abcdefgh"},
    # fila 6
     **{f"{columna}6": " " for columna in "abcdefgh"},
    # fila 7
    **{f"{columna}7":"PeonN" for columna in "abcdefgh"},

    # fila 8 
    "a8": "TorreN",
    "b8":"CaballoN",
    "c8":"AlfilN", 
    "d8":"ReinaN", 
    "e8":"ReyN",
    "f8":"AlfilN",
    "g8":"CaballoN",
    "h8":"TorreN",
}
# prepara dic con mapa de simbolos  pieza =>caracter

simbolos = {
    # blancas
    "TorreB":"R",
    "CaballoB":"N",
    "AlfilB":"B",
    "ReinaB":"Q",
    "ReyB":"K",
    "PeonB":"P",

    # negras
    "TorreN":"r",
    "CaballoN":"n",
    "AlfilN":"b",
    "ReinaN":"q",
    "ReyN":"k",
    "PeonN":"p"
}

    # mostrar tablero | por cada turno se imperima el tablero
def mostrar_tablero(tablero):
    print(" a b c d e f g h")
    for fila in range (8,0,-1):
        filastr = f"{fila}"
        for col in "abcdefgh":
            clave = f"{col}{fila}"
            pieza = tablero.get(clave,".")
            simbolo = simbolos.get(pieza,".")
            filastr += simbolo + " "
        print(filastr)


mostrar_tablero(tablero)

# pedir movimiento al usuario

while True:
    mostrar_tablero(tablero)
    movimiento = input("Ingrese movimiento(ej:'e2') o salir:")
    
    if movimiento == 'salir':
        break

    try:
        origen, destino = movimiento.split()
    except ValueError:
        print(" Movimiento invalido. Use 'casilla' (ej: e2)")
        continue
# validar las casillas
for casilla in [origen, destino]:
    if len(casilla) != 2 or casilla not in 'abcdefgh' or casilla[1] not in '12345678':
        print(f"Error: '{casilla}' no es una casilla valida" )
        continue
    
#verificar las piesas en el origen
    if origen not in tablero:
        print(f"Error: la casilla{origen} no existe en el tablero")
        continue

#realizar el movimiento
pieza = tablero[origen]
tablero [destino] = pieza
tablero[origen] =' '
print(f"Movimiento:{pieza} de {origen} a {destino}")

